#!/usr/bin/env python3
"""Aggregate, non-identifying descriptors of the frozen cohort and the human reference.

Reads the local snapshot and writes only counts and summary statistics to
datos/cohort_aggregates.json. No patient_id, reviewer mapping or clinical text
is written. Standard library only.

    python3 scripts/cohort_aggregates.py [SNAPSHOT_DIR] [FORM199_DIR]
"""
from __future__ import annotations
import collections
import itertools
import json
import random
import statistics
import sys
from pathlib import Path

SNAPSHOT = Path(sys.argv[1] if len(sys.argv) > 1 else
                '/Users/fabianortega/Library/Application Support/epicrisis-experiments/concordancia-50-20260923')
FORM199 = Path(sys.argv[2] if len(sys.argv) > 2 else
               '/Users/fabianortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1')
OUT = Path(__file__).resolve().parent.parent / 'datos' / 'cohort_aggregates.json'
SEED, BOOT = 20260923, 5000

sys.path.insert(0, str(FORM199))
from protocol import catalog, groups  # noqa: E402


def describe(values):
    q = statistics.quantiles(values, n=4)
    return {'median': statistics.median(values), 'q1': q[0], 'q3': q[2],
            'min': min(values), 'max': max(values), 'sum': sum(values)}


def cross_group_relations(fields):
    group_of = {f['key']: g['name'] for g in groups(fields) for f in g['fields']}
    parent_child = [(f['key'], a['key']) for f in fields for a in f['ancestors']
                    if a['type'] == 'leaf' and a['key'] in group_of]
    exclusions = {tuple(sorted((f['key'], o))) for f in fields
                  for o in f.get('mutuallyExclusiveWith', []) if o in group_of}
    crossing = [(c, p) for c, p in parent_child if group_of[c] != group_of[p]]
    return {'parent_child': len(parent_child), 'parent_child_crossing_groups': len(crossing),
            'children_with_crossing_parent': len({c for c, _ in crossing}),
            'exclusion_pairs': len(exclusions),
            'exclusion_pairs_crossing_groups': sum(group_of[a] != group_of[b] for a, b in exclusions)}


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    p1 = sum(a for a, _ in pairs) / n
    p2 = sum(b for _, b in pairs) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2)
    return po, (po - pe) / (1 - pe) if pe < 1 else float('nan')


def specific_agreement(pairs):
    yy = sum(a and b for a, b in pairs)
    nn = sum((not a) and (not b) for a, b in pairs)
    dis = sum(a != b for a, b in pairs)
    return 2 * yy / (2 * yy + dis), 2 * nn / (2 * nn + dis)


def main():
    fields = catalog(json.loads((FORM199 / 'form_schema.json').read_text()))
    leaf = [f['key'] for f in fields if f['type'] == 'leaf']
    manifest = json.loads((SNAPSHOT / 'input/documents_manifest.json').read_text())
    notes = [json.loads(l) for l in (SNAPSHOT / 'input/notes.jsonl').read_text().splitlines() if l.strip()]
    submissions = json.loads((SNAPSHOT / 'reference/submitted_annotations.json').read_text())
    assignments = json.loads((SNAPSHOT / 'reference/assignments.json').read_text())

    out = {
        'schema': {'variables': len(fields),
                   'types': dict(collections.Counter(f['type'] for f in fields)),
                   'with_leaf_ancestor': sum(any(a['type'] == 'leaf' for a in f['ancestors']) for f in fields),
                   'with_mutual_exclusion': sum(bool(f.get('mutuallyExclusiveWith')) for f in fields),
                   'groups': [{'name': g['name'], 'size': len(g['fields'])} for g in groups(fields)],
                   'relations': cross_group_relations(fields)},
        'notes': {k: describe([r[k] for r in manifest]) for k in ('pages', 'spans', 'characters')},
    }
    out['notes']['nonempty_lines'] = describe(
        [sum(1 for x in n['text'].splitlines() if x.strip()) for n in notes])

    per_case = collections.Counter(s['patient_id'] for s in submissions)
    out['annotation'] = {
        'planned_assignments': len(assignments),
        'reviewers_assigned': len({a['reviewer_id'] for a in assignments}),
        'submissions': len(submissions),
        'reviewers_submitting': len({s['reviewer_id'] for s in submissions}),
        'cases_by_submissions': {str(k): sum(1 for pid in {a['patient_id'] for a in assignments}
                                             if per_case.get(pid, 0) == k) for k in range(4)},
        'criteria_per_submission': sorted({len(s['annotations']) for s in submissions}),
        'leaf_states': dict(collections.Counter(
            'unanswered' if x['is_present'] is None else ('doubt' if x['is_unknown'] else
                                                          ('yes' if x['is_present'] else 'no'))
            for s in submissions for x in s['annotations'] if x['criterion_name'] in leaf)),
        'yes_with_evidence_text': sum(1 for s in submissions for x in s['annotations']
                                      if x['criterion_name'] in leaf and x['is_present'] and x['evidence_text']),
    }
    yes_counts = sorted(sum(1 for x in s['annotations'] if x['criterion_name'] in leaf and x['is_present'])
                        for s in submissions)
    out['annotation']['yes_per_submission'] = describe(yes_counts)
    ever_yes = {x['criterion_name'] for s in submissions for x in s['annotations'] if x['is_present']}
    out['annotation']['leaf_never_yes'] = sum(1 for k in leaf if k not in ever_yes)

    # Pairwise agreement: every pair of submissions on the same case, boolean leaves only,
    # excluding unanswered items. Case-level bootstrap because items within a case correlate.
    by_case = collections.defaultdict(list)
    for s in submissions:
        by_case[s['patient_id']].append({x['criterion_name']: x['is_present'] for x in s['annotations']})
    pairs, excluded = collections.defaultdict(list), 0
    for pid, subs in by_case.items():
        for a, b in itertools.combinations(subs, 2):
            for k in leaf:
                if a.get(k) is None or b.get(k) is None:
                    excluded += 1
                else:
                    pairs[pid].append((k, a[k], b[k]))
    flat = [(a, b) for rows in pairs.values() for _, a, b in rows]
    po, k = kappa(flat)
    psa, nsa = specific_agreement(flat)
    rng = random.Random(SEED)
    cases = sorted(pairs)
    boot = []
    for _ in range(BOOT):
        sample = [(a, b) for c in rng.choices(cases, k=len(cases)) for _, a, b in pairs[c]]
        boot.append((kappa(sample)[1], specific_agreement(sample)[0]))
    ks, ps = sorted(b[0] for b in boot), sorted(b[1] for b in boot)
    lo, hi = int(0.025 * BOOT), int(0.975 * BOOT) - 1
    by_domain = {}
    for domain in dict.fromkeys(k.split('.')[0] for k in leaf):
        rows = [(a, b) for r in pairs.values() for key, a, b in r if key.split('.')[0] == domain]
        if rows:
            d_po, d_k = kappa(rows)
            by_domain[domain] = {'item_pairs': len(rows), 'observed_agreement': round(d_po, 3),
                                 'kappa': round(d_k, 3), 'positive_agreement': round(specific_agreement(rows)[0], 3)}
    out['inter_annotator'] = {
        'unit': 'submission pair x boolean variable', 'cases': len(cases),
        'submission_pairs': sum(len(list(itertools.combinations(s, 2))) for s in by_case.values()),
        'item_pairs': len(flat), 'excluded_unanswered': excluded,
        'observed_agreement': round(po, 3), 'cohen_kappa_pooled': round(k, 3),
        'kappa_ci95_case_bootstrap': [round(ks[lo], 3), round(ks[hi], 3)],
        'positive_specific_agreement': round(psa, 3),
        'psa_ci95_case_bootstrap': [round(ps[lo], 3), round(ps[hi], 3)],
        'negative_specific_agreement': round(nsa, 3),
        'bootstrap': {'replicates': BOOT, 'seed': SEED}, 'by_domain': by_domain,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out['inter_annotator'], indent=2))


if __name__ == '__main__':
    main()
