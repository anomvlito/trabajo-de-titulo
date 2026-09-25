# Reference index — LLM clinical information extraction (paper_harness)

Built 2026-09-23. Metadata was checked against Crossref, PubMed E-utilities, the PMC ID Converter, the arXiv API, the medRxiv API and ACL Anthology BibTeX. Summaries were written from the full texts in `md/`.

Batch 2 (#14–#27) was added on 2026-09-24 with the same method; see "Metadata corrections (batch 2)" at the end of this file. Texts from JATS XML in batch 2 (psych2stage2026, twophaseexam2025) and the blog post (thinkingmachines2025nondeterminism) have no page numbers; cite them by section. In batch 2, *[Relevance]* lines refer to **arm C** (a first call builds a shared, evidence-validated case model that is injected into the 18 parallel variable-group calls) and to nondeterminism in vLLM runs.

## How to read this file

- Each entry (a "ficha") covers design, data, annotation, output schema, prompting, models, grounding, results, code and limitations. Its fields are written in English and are based only on what the paper states. "Not reported" means the paper does not say.
- **Citable claims** are verbatim quotes of at most 2 sentences. Every quote was machine-checked against `md/<key>.md` (see the end of this file). Quotes are exact except for whitespace and line-break artifacts from PDF conversion.
- **Page references:**
  - For PDF-derived texts, `<!-- page N -->` markers in the `.md` file are the PDF page index. When the journal or proceedings page differs, both are given, e.g. "p. 2001 (PDF p. 4)".
  - Texts from JATS XML (llmie2025, promptstotable2025, liu2020consortai, rivera2020spiritai) have no page numbers; cite them by section.
- The target use case throughout is comparing **monolithic extraction** (199 variables in one LLM call) with a **multi-call harness** that extracts groups of variables. Comments marked *[Relevance]* are the compiler's reading, not the authors' claims.

## Overview

| # | Key | Reference (verified) | Full text | Text source |
|---|---|---|---|---|
| 1 | agrawal2022fewshot | Agrawal et al., EMNLP 2022, pp. 1998–2022 | yes | ACL Anthology PDF |
| 2 | promptstotable2025 | Hein et al., medRxiv 2025 (preprint of #7), PMID 39990557 | yes | Europe PMC XML (v2); PDF = v1 |
| 3 | privacy2024structured | Wiest et al., npj Digit Med 2024;7:257 | yes | nature.com PDF |
| 4 | scoping2024radiology | Reichenpfader et al., npj Digit Med 2024;7:222 | yes | nature.com PDF |
| 5 | fornasiere2024medical | Fornasiere et al., ICNLSP 2024, pp. 456–466 | yes | ACL Anthology PDF |
| 6 | llmie2025 | Hsu & Roberts, JAMIA Open 2025;8(2):ooaf012 | yes | Europe PMC XML (no PDF: Cloudflare) |
| 7 | iterativerefine2025 | Hein et al., npj Digit Med 2025;8:301 | yes | nature.com PDF |
| 8 | clinicalentityretrieval2024 | Lopez et al., npj Digit Med **2025**;8:45 | yes | nature.com PDF |
| 9 | spaanderman2025structured | Spaanderman et al., arXiv:2511.10658v1 (2025) | yes | arXiv PDF (81 pp. incl. supplement) |
| 10 | gallifant2025tripodllm | Gallifant et al., Nat Med 2025;31(1):60–69 | yes | nature.com PDF |
| 11 | collins2024tripodai | Collins et al., BMJ 2024;385:e078378 | yes | BMJ PDF via UCL Discovery repository |
| 12 | liu2020consortai | Liu et al., BMJ 2020;370:m3164 | yes | Europe PMC XML (no PDF: Cloudflare) |
| 13 | rivera2020spiritai | Cruz Rivera et al., BMJ 2020;370:m3210 | yes | Europe PMC XML (no PDF: Cloudflare) |
| 14 | psych2stage2026 | Chen et al., JMIR Form Res 2026;10:e94454, PMID 42560822 | yes | Europe PMC XML (no PDF: JMIR/PMC bot challenge) |
| 15 | clinicirca2026 | Zhang et al., arXiv:2609.19585v1 (2026), preprint | yes | arXiv PDF (34 pp. incl. appendices) |
| 16 | promptplanextract2026 | Pathak et al., arXiv:2606.19852v2 (2026), preprint | yes | arXiv PDF (v2) |
| 17 | cancerregistrymas2026 | Aal Abdulsalam et al. (Anthology order; PDF byline: Jeeballah et al.), BioNLP 2026, pp. 531–551 | yes | ACL Anthology PDF |
| 18 | twophaseexam2025 | Abumelha et al., JMIR Med Inform 2025;13:e78432, PMID 41171081 | yes | Europe PMC XML (no PDF: JMIR/PMC bot challenge) |
| 19 | skeletonofthought2024 | Ning et al., ICLR 2024 (poster); arXiv:2307.15337v3 | yes | arXiv PDF v3 (51 pp. incl. appendices) |
| 20 | erman1980hearsay | Erman et al., ACM Comput Surv 1980;12(2):213–253 | yes (ACM OCR text) | ACM PDF (free backfile) via Internet Archive capture; dl.acm.org blocked by Cloudflare |
| 21 | nii1986blackboard | Nii, AI Magazine 1986;7(2):38–53 ("Part One") | yes (OCR) | AAAI OJS PDF (scan, no text layer); OCR with Apple Vision |
| 22 | blackboardllm2025 | Salemi et al., arXiv:2510.01285v2 (2025), preprint | yes | arXiv PDF v2 (44 pp. incl. appendices) |
| 23 | blackboardmas2025 | Han & Zhang, arXiv:2507.01701v1 (2025), preprint | yes | arXiv PDF (15 pp. incl. appendices) |
| 24 | hisccg2026 | Tian et al., Sci Rep 2026, Article in Press | yes (unedited manuscript) | nature.com "Article in Press" PDF; the HTML page has the abstract only |
| 25 | trialgpt2024 | Jin et al., Nat Commun 2024;15:9074 | yes | nature.com PDF |
| 26 | thinkingmachines2025nondeterminism | He & Thinking Machines Lab, blog, 10 Sep 2025 (**grey literature**) | yes | Official blog HTML, captured 2026-09-24 |
| 27 | atil2024nondeterminism | Atıl et al., Eval4NLP 2025, pp. 135–148 (arXiv:2408.04667) | yes | ACL Anthology PDF (Eval4NLP version) |

**Not downloaded:** supplementary files, except the Spaanderman supplement, which is inside the arXiv PDF. The Wiest supplement was checked online: it has no agreement coefficient (see #3).

**Batch 2, not downloaded:** supplementary files (e.g. JMIR Multimedia Appendix 1 of #14). All 14 batch-2 works were obtained in full text.

---

## Fichas

### agrawal2022fewshot — Large language models are few-shot clinical information extractors

*Agrawal, Hegselmann, Lang, Kim, Sontag. EMNLP 2022, pp. 1998–2022. doi:10.18653/v1/2022.emnlp-main.130; arXiv:2205.12689. Page refs: proceedings p. (PDF p.).*

- **Design:** A methods and benchmark study. GPT-3 is prompted zero-shot or one-shot on five clinical/biomedical IE tasks.
  - Short, task-specific **resolvers** map the free-text output to structured labels.
  - Comparisons: supervised, zero-shot and few-shot baselines, plus distillation into PubMedBERT (§3–7).
- **Language and documents:** English only (Limitations, p. 2006 (PDF p. 9)).
  - CASI clinical-note snippets (multi-specialty, University of Minnesota-affiliated hospitals).
  - MIMIC-III reverse-substitution set (test only).
  - EBM-NLP PubMed abstracts (Table 1, p. 1999).
- **Dataset size:**
  - Acronyms: CASI 18,164 examples (41 acronyms) and MIMIC 8,912.
  - Arm identification: 187 test abstracts, plus 20 for arm identification.
  - Three new CASI sets of 105 snippets each: coreference; medication status (340 medication–status pairs); medication attributes (313 medications, 533 attributes).
  - There is no LLM training. Prompts were designed on about 5 validation examples per task (§3.1).
- **Annotators and agreement:**
  - Two authors with clinical-NLP or medical backgrounds labelled the same 105 examples independently, then adjudicated jointly (§3.2, p. 2001).
  - No agreement coefficient is reported for the new CASI sets. Arm identification was "perfect agreement".
  - κ = 0.59 refers to the pre-existing EBM-NLP token labels (§5).
- **Output schema:** Free text or bulleted lists, turned by resolvers into:
  - an acronym expansion (multiple choice);
  - token labels;
  - a list of trial arms;
  - a coreference antecedent;
  - a medication plus its status (active/discontinued/neither);
  - a medication plus 5 attributes: dosage, route, frequency, reason, duration.
  
  There is no JSON.
- **Prompting:**
  - One prompt per example. Several tasks query a single item per prompt, such as one acronym or one pronoun.
  - **Guided prompt design:** a one-shot example in the target format plus a primed answer prefix (§3.1).
  - Medications and their statuses are requested **together in one prompt** (§7.1). Two separate status-specific prompts were tried and abandoned (Limitations).
  - Greedy decoding. No chain-of-thought.
- **Models:** GPT-3 through the OpenAI API (text-davinci-edit-001, InstructGPT text-davinci-002), which is closed. Distilled PubMedBERT (open). Baselines include T-Few (T0-11B), PubMedBERT-CRF and ScispaCy.
- **Grounding:** No verifier LLM. The resolvers are deterministic and map output back to the input: highest character overlap with the answer options (§4), and "input-consistency checking" that drops tokens absent from the input (App. C.4, p. 2020 (PDF p. 23)).
- **Key results:**
  - **Acronyms** (Table 2, p. 2002): CASI accuracy 0.86, macro-F1 0.69; 0.90/0.76 after distillation.
  - **Medication extraction** (Table 5, p. 2004): one-shot recall 0.90, precision 0.92, vs ScispaCy 0.73/0.67.
  - **Medication status** (Table 6): macro-F1 0.62 one-shot, 0.71 when the example shows all classes.
  - **Medication attributes, relation-level F1** (Table 7, p. 2005): dosage 0.80, route 0.63, frequency 0.60, reason 0.34, duration 0.16.
  - **Cost:** API cost under $100 (App. D).
- **Code and data:** Annotated data at https://huggingface.co/datasets/mitclinicalml/clinical-ie (p. 1998, footnote 1). Code not reported.
- **Author-stated limitations** (p. 2006):
  - hard to make the LLM match an exact schema or multi-page guidelines;
  - bias toward non-empty answers;
  - CASI is not representative;
  - English only;
  - inference cost;
  - no cohort-stratified evaluation.

**Citable claims**
- "The required complexity of the resolver depends largely on the cleanliness of the prompt output, and by extension the prompt itself. We introduce _guided prompt design_ to simplify the resolver required for complex output." (p. 2000 (PDF p. 3), §3.1)
- "Our prompt asked the model to simultaneously output the list of medications and the status of each." (p. 2004 (PDF p. 7), §7.1)
- "First, it is still difficult to guide a LLM to match an exact schema—clinical annotation guidelines are often multiple pages." (p. 2006 (PDF p. 9), Limitations)
- "However, if there were two active medications and none discontinued, the LLM primed with the discontinuation prompt tended to try to find an output and usually resorted to listing one or more active medications." (p. 2006 (PDF p. 9), Limitations)
- "For example, this could be achieved via (i) chaining multiple prompts, e.g., first asking if a certain entity type exists in the input, before asking for a list (Li et al., 2019b; Wu et al., 2022) or (ii) using an output structure like the sequence tagging approach." (p. 2006 (PDF p. 9), Limitations)
- "The next step in the resolver is to _denoise_ the individual strings in each list by first stripping dosage and route information (e.g., “10 mg” or “patch”) and then performing inputconsistency checking by removing tokens that do not appear in the input." (p. 2020 (PDF p. 23), App. C.4; "inputconsistency" [sic] as printed in the PDF)

*[Relevance]* This paper is evidence both ways. It asks for a joint output (medications plus status in one prompt) and warns that task-specific prompts create a non-empty-answer bias. It also suggests chaining prompts and admits that long schemas are hard to follow.

---

### promptstotable2025 — Prompts to Table (medRxiv preprint; preprint of #7)

*Hein D, Christie A, Holcomb M, Xie B, Jain AJ, Vento J, Rakheja N, Hamza Shakur A, Christley S, Cowell LG, Brugarolas J, Jamieson AR, Kapur P. medRxiv 2025, doi:10.1101/2025.02.11.25322107 (v1 13 Feb 2025; v2 1 Apr 2025); PMID 39990557; PMC11844613. The text in `md/` is v2 (Europe PMC XML); `pdf/` holds v1. Cite by section.*

- **Design:** A single-institution retrospective study (UT Southwestern).
  - A human-in-the-loop pipeline was refined over 6 iterations on a 152-report development set.
  - It was then applied to 3,520 internal reports and ported to public TCGA reports.
  - The authors say there was no static held-out test set covering all fields (§Discussion).
- **Language and documents:** Kidney-tumour pathology reports, free-text parts only: final diagnosis, ancillary studies, comments, addenda. The TCGA BRCA/PRAD reports are OCR text. The language is not stated; all excerpts are English.
- **Dataset size:**
  - Development: 152 reports, giving 1,413 gold entities (152 diagnoses, 651 specimen-level labels, 610 IHC/FISH results).
  - Internal: 3,520 reports (Apr 2019–Apr 2024), of which 2,297 had templated EMR data used as reference.
  - TCGA: BRCA 53 of 757 reports and PRAD 253 of 333 (§Results).
- **Annotators:** A data scientist (5 years' experience) and a statistician (13 years), with a board-certified GU pathologist (23 years) for ambiguous cases. **No IAA reported**; the authors say iterative development was "precluding formal inter-reviewer agreement metrics" (§Discussion).
- **Output schema:**
  - What is extracted: report-level diagnosis; per-specimen histology, procedure and site; IHC/FISH results for "30+ assays" at specimen/block level.
  - Controlled vocabularies (ICD-10/CAP) plus an "Other-<as per report>" option.
  - The LLM returns JSON; Python converts it to a long table (report, specimen/block, item, label).
  - There is no fixed variable count.
- **Prompting:**
  - A Microsoft Prompt flow DAG with **three template sets, one per entity class**: feature-report, feature-specimen and IHC/FISH.
  - Each set runs segmentation prompt(s), then a standardization prompt, then Python parsing.
  - Entity-specific schema text is "hot-swapped" into placeholders.
  - Every prompt generates reasoning first, which is passed forward (chain-of-thought). JSON format examples are included.
  - The number of variables per call is not stated in the text.
- **Models:**
  - Development: GPT-4o 2024-05-13 through the Azure API, temperature 0.
  - Application: GPT-4o 2024-08-06.
  - Local open-weight: Llama 3.3 70B and Qwen2.5 72B.
  - The preprint's Results section labels one GPT-4o run "2024-08-06", which contradicts its own Methods; the journal version fixes this.
- **Grounding:** No automated span verification. Segmented source text plus reasoning is carried to standardization. Humans review discrepancies, and there is a histology–IHC consistency check.
- **Error ontology:** Discrepancy source (LLM / annotation / schema issue) × severity (major / minor) × context label.
- **Key results:**
  - Development set, final iteration: major LLM error 0.99% (14/1,413).
  - Backbones, exact match: GPT-4o 84.1%, Qwen 78.1%, Llama 70.1%. Fuzzy: 90.0 / 86.1 / 82.0.
  - Internal validation: macro-F1 0.99 across six subtypes, F1 0.97 for metastasis. 27 corrections to the existing structured data, all confirmed by a pathologist.
  - TCGA: BRCA 89% after 3 schema-only iterations; PRAD 98% on the first run.
- **Code and data:** https://github.com/DavidHein96/prompts_to_table. Institutional data not shared. TCGA OCR text at https://data.mendeley.com/datasets/hyg5xkznpx/1.
- **Author-stated limitations** (§Discussion):
  - risk of overly specific one-off rules;
  - human review is time-intensive;
  - output only semi-structured (guided decoding suggested);
  - no IAA;
  - no exhaustive held-out benchmark;
  - the major/minor grading depends on intended use.

**Citable claims**
- "We developed three distinct template sets, each optimized for a specific class of entity: The ‘feature report’ set for entities with a single label per report, such as diagnosis; The ‘feature specimen’ set for entities with one label per specimen/subpart; And an IHC/FISH specific set as it uniquely requires matching any number of specimens, blocks, test names, and test results; see Figure 1B." (§Methods › Prompt Templates)
- "All template sets include initial prompts to segment and organize text, a subsequent standardization prompt to normalize labels and produce structured output, and a final python step for parsing into tabular data. The full output from segmentation steps, both reasoning and the segmented text, is passed to subsequent steps." (Figure 1 caption)
- "We also observed that major errors in IHC/FISH extraction, primarily missing results, were more prevalent in reports containing a high volume of tests (>10), and ambiguity arose in defining the severity of missing results when tests were mentioned by name but potentially not performed; STable 1.2." (§Results › Report Complexities)
- "Schema issues represent instances where the LLM and gold-standard were discordant, yet both appeared to have adhered to the provided instructions. In these cases, the instructions themselves were found to be insufficient or ambiguous." (§Methods › Creating an Error Ontology)
- "The standard was developed iteratively by the core team to refine complex task specifications, precluding formal inter-reviewer agreement metrics and limiting assessment of absolute annotation reliability." (§Discussion)

---

### privacy2024structured — Privacy-preserving LLMs for structured medical information retrieval

*Wiest IC, Ferber D, Zhu J, van Treeck M, Meyer SK, Juglan R, Carrero ZI, Paech D, Kleesiek J, Ebert MP, Truhn D, Kather JN. npj Digit Med 2024;7:257. doi:10.1038/s41746-024-01233-2; PMID 39304709. PDF page = article page.*

- **Design:** A retrospective evaluation of an open-source pipeline built on a local LLM. It compares 3 Llama-2 sizes and several prompt variants against an expert reference standard (p. 1; §Methods p. 6).
- **Language and documents:** English "present medical history" sections of MIMIC-IV notes (p. 2, p. 6). Other languages are untested (§Discussion).
- **Dataset size:** The first 500 histories (p. 6). No split reported. Prevalence (p. 2): abdominal pain 209/500, SOB 130/500, ascites 20, "cirrhos" 29.
- **Annotators:** Three blinded medical experts; disagreements resolved by discussion to consensus (p. 7).
  - **No IAA coefficient** appears in the main text.
  - The supplement the text points to (Supplementary Tables 1–2, checked online) has feature definitions and consensus rules, but no agreement statistic.
- **Output schema:** Five binary features: liver cirrhosis, ascites, abdominal pain, shortness of breath, confusion. Each is JSON `{"excerpt": …, "present": true/false}`, converted to CSV (p. 6).
- **Prompting:**
  - One report per inference, with a fixed prompt plus a grammar (Fig. 5, p. 7).
  - The example output is one JSON keyed by feature, so all 5 features appear to be requested together. The number of calls per report is **not explicitly stated**.
  - Variants tested: zero-shot, one-shot, feature definitions, grammar-enforced "excerpt-then-answer" chain-of-thought, and system vs user prompt placement (pp. 4–5).
- **Models:** Llama-2 7B, 13B and 70B (open-weight), run locally with llama.cpp (p. 6). Quantization and hardware are not given in the main text.
- **Grounding:** The grammar forces an **excerpt** from the report before each binary answer, for explainability. There is **no check that the excerpt exists in the source**. A hallucinated excerpt from the 7B model is reported (p. 3).
- **Metrics and results:** Sensitivity, specificity, PPV, NPV and accuracy, with a 1,000-sample bootstrap (p. 7).
  - 70B zero-shot with definitions (Table 1, p. 4), in the order cirrhosis/ascites/pain/SOB/confusion: sensitivity 1.00/0.95/0.84/0.87/0.76; accuracy 0.96/0.95/0.95/0.94/0.93.
  - PPV is low for rare features: ascites 0.44, confusion 0.54.
  - 70B one-shot accuracy (Table 2, p. 5): 0.98/0.99/0.92/0.94/0.93.
  - 7B accuracy ranges from 0.71 to 0.87.
  - The abstract gives SOB specificity as 97%; the text and Table 1 give 0.96.
- **Code and data:** https://github.com/I2C9W/fromtexttotables/releases/tag/v0.5.0 (p. 7). MIMIC-IV requires credentialed access through PhysioNet.
- **Author-stated limitations** (pp. 5–6):
  - worse recall for implicit features (confusion);
  - gender-inference bias;
  - English only;
  - residual hallucination (fine-tuning or RAG suggested).

**Citable claims**
- "Our study successfully demonstrates the capability of locally deployed LLMs to extract clinical information from free text with low hardware requirements." (p. 1, Abstract)
- "Initially, the model was prompted to give JavaScript Object Notation (JSON) formatted output, but the model’s JSON output was inconsistent and defective. The model output missed relevant parenthesis displaying non-escaped characters that could not be parsed." (p. 6, §Model details and data processing)
- "Thus, we enforced the JSON format generation using llama.cpp’s grammar-based sampling, which dictates text generation through specific grammatical rules to ensure valid JSON." (p. 6, §Model details and data processing)
- "Requesting an excerpt from the text followed by a binary answer (Chain-of-thought prompting) did not yield improved results." (p. 4, §Prompt engineering enhances accuracy, especially in smaller sized models)
- "For explainability reasons, we nevertheless forced the model with the grammar (which is outlined in detail in the github repository) to provide, first, an excerpt, and only then the binary outcome and found that this did not adversely affect performance." (p. 4, same section)
- "In summary, these data show that prompt engineering can help improve performance especially in the smallest model, whereas larger model sizes demonstrated greater robustness, with remarkably high performance of simple prompts, improving only marginally through prompt engineering." (p. 5, same section)

---

### scoping2024radiology — Scoping review: LLM-based IE from radiology reports

*Reichenpfader D, Müller H, Denecke K. npj Digit Med 2024;7:222. doi:10.1038/s41746-024-01219-0; PMID 39182008. PDF page = article page.*

- **Design:** A scoping review (JBI Manual, PRISMA-ScR, PRISMA-S) with a published protocol.
  - Five databases were searched on 01/08/2023: PubMed, IEEE Xplore, ACM DL, Web of Science, Embase. Reference lists were also screened, and the search was not updated.
  - Peer-reviewed work after 2017 only.
  - The review defines an "LLM" as a deep-learning model with more than 1M parameters trained on unlabelled text, so BiLSTMs are included (pp. 8–9).
- **Language and documents:** Radiology reports.
  - Language is inferred from the corresponding author's country: English 21 (62%), Chinese 6, German 4, Japanese 2, Spanish 1.
  - Modalities: CT 16, MRI 15, X-ray 14 (pp. 5–6).
- **Dataset size:** 1,237 records → **34 included studies**, 9 of them found through reference lists (p. 2, Fig. 1). The included studies fine-tuned on 50–10,155 reports (p. 4).
- **Reviewers:**
  - Two authors screened after two calibration batches of 25 records (2 and 3 conflicts). Any record included once was retained.
  - One author charted all data; two studies were double-extracted as a pilot.
  - **No agreement statistic reported** (p. 9).
- **Output schema (included studies):**
  - Tasks: NER in 21 studies (10 with relation extraction); document-level multi-label classification in 9.
  - Concepts per study: 1 to 64.
  - Only 3 of 34 normalize or structure their output. 21 (62%) give no details of how the information model was developed (p. 2).
- **Prompting:** Not applicable. **No generative or prompt-based study was included** (p. 7). The post-cutoff generative work is discussed only narratively (pp. 7–8).
- **Models:** 28 of 34 transformer-based (27 BERT-type), 6 BiLSTM (p. 3).
  - Open vs closed is not classified.
  - Data-protection rules restrict GPT-4, and Llama-2 70B needs more compute than on-premise hospital infrastructure provides (p. 7).
- **Grounding:** Not addressed. The authors argue encoder models "cannot hallucinate" (p. 6).
- **Key quantitative findings (pp. 4–5):**
  - F1 ranges from 68.76 to 98.00, and the values are not comparable across studies (Table 4).
  - Inter-annotator agreement: reported by 23 studies (68%), with values given by 16 (Cohen's κ 81%–93.7%).
  - Annotation guidelines: not mentioned by 23 (68%).
  - Code available: 10 (29%). External validation: 7 (21%).
  - Largest external-validation drop: 35%.
- **Code and data:** Extraction table on OSF, doi:10.17605/OSF.IO/RWU5M (p. 9).
- **Author-stated limitations** (p. 7):
  - contested definitions of IE and of LLM;
  - non-exhaustive search (no arXiv or ACL Anthology, not updated);
  - heterogeneity, so the synthesis is descriptive only;
  - single-author data charting.
- **Caveats:** The review is internally inconsistent in places:
  - "15 out of 35 papers" although 34 studies were included;
  - "up to 64" concepts while Table 4 lists 75;
  - external-validation counts of 7, 6 and 7.

**Citable claims**
- "No generative models and therefore no approaches based on generative models (including few-, single- or zero-shot learning) are included in the search results." (p. 7, §Discussion)
- "However, due to the sensitive nature of patient data, utilization of publicly serviced models, e.g., GPT-4, is restricted due to data protection rules. Until the cut-off time of this review, state-of-the-art, open-source generative models, e.g., LLama 2 (70B), had still required vast computational resources, restricting the possibilities of on-premise deployment within hospital infrastructures." (p. 7, §Discussion)
- "Performance measures reported in Table 4 cannot be compared due to differences in datasets, number of extracted concepts and the heterogeneity of applied performance measures." (p. 5, §Discussion)
- "Considering the periodical publication of larger, more capable generative models, transparent and verifiable reporting of all aspects described in this review is essential to compare and identify successful approaches." (p. 8, §Discussion)
- "We furthermore suggest future research to focus on the optimization and standardization of annotation processes to develop few-shot prompts. Currently, the correlation between annotation quality, quantity and model performance is unknown." (p. 8, §Discussion)

---

### fornasiere2024medical — Medical Information Extraction with Large Language Models

*Fornasiere R, Brunello N, Scotti V, Carman M(J). ICNLSP 2024, pp. 456–466 (ACL Anthology 2024.icnlsp-1.47; no DOI). Page refs: proceedings p. (PDF p.).*

- **Design:** A system/pipeline paper with a small experiment.
  - It compares zero-shot, few-shot and sequential prompting for **medication extraction** and **timeline (date) extraction**.
  - The pipelines are deployed in a demo web app (§3, §5).
  - No comparison with published baselines (§6).
- **Language and documents:** Discharge summaries. n2c2 and i2b2 sets are English. A synthetic set (SD) was generated with ChatGPT-4 in English and Italian (§4, p. 461). Whether the Italian SD is included in the results is not stated.
- **Dataset size:**
  - "N2C2": 1,243 summaries, 251 annotated (§4.1, p. 459).
  - I2B2: 310 summaries (p. 460).
  - The size of SD and the evaluated subsets are not reported.
  - Few-shot uses 2 examples (medication) and 4 (timeline).
- **Annotators:** No new human annotation; the challenge gold standards are reused, and the SD labels were generated by ChatGPT-4. **No IAA.**
- **Output schema:**
  - **Medication:** CSV or JSON with name, dose, mode, frequency and line. Scored either as "name only" or as the concatenated "full medication".
  - **Timeline:** a JSON array of {dateValue, dateString, event} plus a line number; only the dates are evaluated (§3.3, §5).
- **Prompting:**
  - Chat format: the document goes in the system message and the task in the user message, with a prefilled answer start.
  - **Medication:** all fields in **one call** ("extract all the information at once").
  - **Timeline:** **sequential 3-turn prompting**: count the events, build the JSON array, then add line numbers (§3.3).
  - Experimental grid: {zero-shot, few-shot, sequential} × {JSON, CSV} × {whole document, chunked}.
- **Models:** Mistral 7B only (open-weight). The variant and hardware are not reported (§5).
- **Grounding:** **Line-number referencing.** The document is fed with numbered rows, and the LLM is asked for the row that supports each extraction (§3.2, p. 458). The correctness of these line references is **not evaluated**.
- **Key results (precision/recall/F1, string match):**
  - **Medication, name only** (Table 1, p. 463 (PDF p. 8)): best F1 0.683 (few-shot, JSON, chunked; P 0.965, R 0.547); zero-shot JSON 0.513.
  - **Medication, full medication:** F1 0.166–0.378 across all settings.
  - **Timeline F1 (Table 2):** I2B2 zero-shot 0.651, few-shot 0.790, sequential 0.660. SD best 0.931 (few-shot, chunked).
- **Code:** The authors "pledge" to release it; no URL is given (Ethics).
- **Author-stated limitations:**
  - focus on the pipeline rather than exhaustive experiments;
  - one model only;
  - small datasets, hence high variance (Limitations, p. 464);
  - synthetic data may miss real-world nuance;
  - sensitivity to format and prompts; string-match metrics (§7).
- **Caveats:**
  - §6.1 interprets precision and recall the opposite way from the standard definitions.
  - The dataset labelled "N2C2" cites Uzuner et al. 2010, i.e. the 2009 i2b2 medication challenge.

**Citable claims**
- "Concerning medication extraction, we task the model to extract all the information at once from a reference document." (p. 459 (PDF p. 4), §3.3)
- "We broke down the task into three steps: counting the events mentioned in the document, generating a JSON array with the chronologically ordered events and generating the line number for each event on the array." (p. 459 (PDF p. 4), §3.3)
- "We have a separate pipeline ingesting the clinical document to analyse decorated with the rows numbers. In this way, we can interrogate the LLM automatically asking to point out the number of the row connected to a specific extraction (e.g., where is a specific drug mentioned or where is a specific event mentioned)." (p. 458 (PDF p. 3), §3.2)
- "Moreover, results using full medication information are consistently lower, indicating that, as expected, extracting detailed information is harder than simply identifying the medication." (p. 462 (PDF p. 7), §6.1)
- "The higher results on chunked documents seem to indicate that, in this case, using longer documents negatively affects the ability to extract the time information." (p. 463 (PDF p. 8), §6.2)
- "This hints that the sequential approach helped the LLM capture better the target task and output format." (p. 463 (PDF p. 8), §6.2; in Table 2 sequential prompting did not beat few-shot)

---

### llmie2025 — LLM-IE: a Python package for biomedical generative IE

*Hsu E, Roberts K. JAMIA Open 2025;8(2):ooaf012. doi:10.1093/jamiaopen/ooaf012; PMID 40078164. Text from Europe PMC JATS XML; cite by section.*

- **Design:** A software paper (a Python package), benchmarked on public clinical challenge corpora (§Methods, §Benchmarking).
- **Language and documents:** Clinical notes from the 2012 i2b2 temporal-relations, 2014 i2b2 de-identification and 2018 n2c2 Track 2 (ADE/medication) corpora. The language is not stated.
- **Dataset size:** **Not reported.** The text gives no document counts or splits.
- **Annotators:** Not applicable; the existing challenge gold standards are reused. No IAA.
- **Output schema:**
  - The LLM emits JSON per the prompt template. Post-processing turns it into "frames": ID, entity text, spans and attributes.
  - Relations between frame pairs can be binary or multi-class.
  - Benchmarked targets: EVENT/TIMEX with attributes (2012); PHI (2014); drugs and ADEs (2018).
  - The number of fields per prompt is not reported.
- **Prompting:** Three frame extractors:
  - **Basic:** one prompt on the whole document.
  - **Review:** an extra prompt asking the model to amend and correct its first output.
  - **Sentence:** splits the document into sentences and prompts sentence by sentence.
  
  Entity spans and attributes are extracted end-to-end in the same prompt. Relation extractors prompt once per candidate frame pair; an optional rule function skips impossible pairs. The benchmark uses 8-shot prompts. A "Prompt Editor" LLM agent helps draft templates.
- **Models:** Llama-3.1-70B, 8-shot, served with vLLM on A100 GPUs (open-weight, self-hosted). The package also supports Ollama, HuggingFace, llama.cpp, vLLM and the OpenAI API.
- **Grounding:** Frames carry spans. Data-type validation checks overlaps, redundancy and relation consistency. Malformed JSON elements are discarded. The Review extractor gives self-correction, and a visualizer supports manual checking. No dedicated span-verification step is described.
- **Key results (Table 2), F1 Sentence vs Basic:**

  | Corpus / task | Sentence | Basic |
  |---|---|---|
  | 2012 EVENT | 0.7799 | 0.4364 |
  | 2012 TIMEX | 0.8071 | 0.5147 |
  | 2014 PHI (strict) | 0.7014 | 0.5755 |
  | 2018 (strict) | 0.7154 | 0.478 |

  - The gain is mostly recall: EVENT recall 0.6824 vs 0.2841.
  - Sentence costs about 2–2.6× the GPU time per note (e.g. 132.9 s vs 67.5 s).
  - Attribute extraction: Sentence 0.5505–0.678 vs Basic 0.2589–0.3236.
  - Sentence lenient F1 on 2018 is 0.8053, against 0.8051 for the average supervised n2c2 participant (§Discussion).
- **Code:** https://github.com/daviden1013/llm-ie; benchmark code at https://github.com/daviden1013/LLM-IE_Benchmark; https://pypi.org/project/llm-ie/.
- **Author-stated limitations** (§Discussion):
  - still in active development;
  - users must still finalize prompts;
  - depends on correctly formatted LLM output;
  - only Llama 3.1 benchmarked;
  - few-shot performance is below supervised systems on some tasks.

**Citable claims**
- "The Sentence frame extractor splits the target document into sentences and prompts sentence by sentence to improve recall and entity span detection accuracy." (§Package design and architecture)
- "In general, the Sentence Frame Extractor is more suitable for “dense” tasks in which a document contains many entities, while the Basic Frame Extractor is more efficient for “sparse” tasks with fewer entities." (§Building information extraction pipelines with LLM-IE APIs)
- "For the NER and EA tasks, the Sentence Frame Extractor achieved the best F1 scores (>0.701 for NER tasks, ∼0.600 for most AE tasks), while consuming more GPU time (up to 2 minutes per note)." (§Results › Benchmarking; "AE" is the paper's typo for EA)
- "The Review frame extractor prompts LLM to generate initial outputs and prompt again for amendment and correction." (§Package design and architecture)
- "The post-processing relies on the LLM to output in the correct format. Inconsistent elements in the JSON list are discarded." (§Discussion)

*[Relevance]* This is the clearest head-to-head evidence that splitting the input into many smaller calls (per sentence) raises recall substantially over a single whole-document call, at roughly double the compute.

---

### iterativerefine2025 — Iterative refinement and goal articulation (npj Digit Med)

*Hein D, Christie A, Holcomb M, Xie B, Jain AJ, Vento J, Rakheja N, Shakur AH, Christley S, Cowell LG, Brugarolas J, Jamieson AR, Kapur P. npj Digit Med 2025;8:301. doi:10.1038/s41746-025-01686-z; PMID 40410408. Received 14 Feb 2025, accepted 28 Apr 2025. PDF page = article page.*

- **Design:** Same study as #2: iterative refinement on 152 reports (6 cycles), internal validation and TCGA portability (p. 3; Methods pp. 10–11).
- **Language and documents:** Kidney-tumour pathology reports (free-text sections) and OCR'd TCGA reports. The language is not stated (English excerpts).
- **Dataset size:**
  - Development: 152 reports, 1,413 entities.
  - Internal: 3,520 reports, of which 2,297 had structured EMR data and "an additional 1223 reports" did not (p. 8).
  - TCGA: BRCA 53/757, PRAD 253/333 (p. 9).
- **Annotators:** Data scientist, statistician, and a GU pathologist for ambiguous cases (p. 11). **No IAA reported** (p. 10).
- **Output schema:**
  - JSON with a `"reasoning"` field plus one key per specimen for a given feature (e.g. `A_histology`, `B_histology`), per the Fig. 1b picture text (p. 2).
  - Converted to a long table (item, specimen, label).
  - Controlled vocabularies with "Other" options.
- **Prompting:**
  - Fig. 1b (p. 2) shows **seven templates in three sets**:
    - Feature/Report: segmentation, standardization.
    - Feature/Specimen: segmentation, standardization.
    - IHC/FISH: segmentation I, segmentation II, standardization.
  - The feature templates are parameterized by a single `{{feature}}` and its `{{labels}}` ("Segment text relevant to {{feature}}"), so each run targets one feature. The IHC/FISH set handles all tests of a report together.
  - The paper does not report the total number of calls per report.
  - Reasoning is generated first and passed forward (chain-of-thought) (p. 10).
- **Models:**
  - GPT-4o 2024-05-13 through Azure (temperature 0) for development; the same backbone in all iterations (Fig. 2, p. 3).
  - GPT-4o 2024-08-06 for validation and TCGA.
  - Llama 3.3 70B and Qwen2.5 72B "run on local compute infrastructure" at temperature 0 (p. 11).
- **Grounding:** No automated span verification. Segmented text and reasoning are passed forward; there is a human discrepancy review and a histology–IHC consistency check (Table 7, p. 9).
- **Error ontology:** Discrepancies are classified by source (LLM / annotation / schema issue), severity (major / minor) and 14 context labels, such as "Inter-Entity Attribution", "Terminology Drift", "Specification Issues" and "Formatting Only" (Fig. 4b, p. 7; p. 11).
- **Key results (identical to #2):**
  - Final-iteration major LLM error 0.99% (14/1,413) (p. 3).
  - Backbone exact-match accuracy 84.1% (GPT-4o), 78.1% (Qwen), 70.1% (Llama); fuzzy 90.0/86.1/82.0 (p. 6).
  - Internal macro-F1 0.99 (subtypes) and F1 0.97 (metastasis) (Table 6, p. 8), with 27 corrections to the existing structured data.
  - TCGA: BRCA 89%, PRAD 98% (p. 9).
- **Code:** https://github.com/DavidHein96/prompts_to_table (p. 11).
- **Author-stated limitations** (p. 10):
  - one-off rules;
  - time-intensive review;
  - semi-structured output;
  - no IAA;
  - no exhaustive held-out benchmark;
  - context-dependent severity grading.

**Citable claims**
- "The full output from segmentation steps, both reasoning and the segmented text, is passed to subsequent steps. The resulting data is in tabular format for immediate downstream utility." (p. 2, Fig. 1 caption)
- "We also observed that major errors in IHC/FISH extraction, primarily missing results, were more prevalent in reports containing a high volume of tests (>10), and ambiguity arose in defining the severity of missing results when tests were mentioned by name but potentially not performed (Supplementary Table 2)." (p. 4, §Report complexities)
- "Despite adding more illustrative examples of correctly mapped output to the prompts, these challenges persisted; Fig. 4a, b." (p. 4, §Report complexities)
- "A structured error ontology was developed to both provide a framework for classifying the source and severity of discrepancies between the LLM outputs and the gold-standard, and to highlight generalizable contexts in which discrepancies arose." (p. 11, §Creating an error ontology)
- "It became evident that the model’s success depended heavily on the clarity and depth of instructions." (p. 9, §Discussion)
- "We found that well-meaning instructions like “focus on the current specimen…, not past medical history” led to instances of ‘malicious compliance’ where the LLM followed instructions too literally, discarding important contextual information." (p. 10, §Discussion)

#### Relationship between #2 (promptstotable2025) and #7 (iterativerefine2025)

These are the same study. The authors, team, data, models, GitHub repository and every headline number are identical: 152 development reports, 6 cycles, 1,413 entities, 0.99% major error, 3,520/2,297 internal reports, F1 0.99/0.97, 27 corrections, TCGA 89%/98%, and backbone accuracies 84.1/78.1/70.1. The abstracts are essentially identical.

What changed in the journal version:
- **Title and framing:** "Prompts to Table: Specification…" became "Iterative refinement and goal articulation…".
- **Structure:** the Methods moved to the end, and the tables were renumbered (1.1–2.2 became 1–7; STable 1.x–8 became Supplementary Tables 1–19).
- **Additions:**
  - a caption sentence on tabular output (Fig. 1) and the same-backbone statement (Fig. 2);
  - the explicit count of 1,223 reports without structured data;
  - temperature 0 for the local models;
  - author contributions and received/accepted dates.
- **Corrections and softening:**
  - the preprint's inconsistent GPT-4o version label is fixed;
  - some wording is softened ("mostly transferable" became "transferable");
  - the Qwen reference is updated.

The npj article was received on 14 Feb 2025, one day after medRxiv v1 was posted. Neither medRxiv (whose API reports `published: NA`) nor Crossref registers a formal preprint→article link. **Cite #7 as the study.** Cite #2 only if you need preprint-specific wording. Do not count them as two independent studies.

---

### clinicalentityretrieval2024 — CLEAR: Clinical entity augmented retrieval

*Lopez I, Swaminathan A, Vedula K, Narayanan S, Nateghi Haredasht F, Ma SP, Liang AS, Tate S, Maddali M, Gallo RJ, Shah NH, Chen JH. npj Digit Med **2025**;8:45. doi:10.1038/s41746-024-01377-1; PMID 39828800. PDF page = article page.*

- **Design:** A new method with retrospective evaluation on two Stanford EHR-derived datasets.
  - CLEAR (entity-based RAG) is compared with embedding-chunk RAG and full-note input, using 6 models.
  - Also included: an NER ablation, a weak-supervision comparison and BERT distillation (p. 2; §Methods).
- **Language and documents:** Stanford MOUD cohort clinical notes (note types not specified) and CheXpert radiology reports (p. 5). The language is not stated explicitly; English models are used.
- **Dataset size:**
  - MOUD: train 767 patients / 16,031 notes; test 505 patients / 12,319 notes. Note length is 218–10,981 tokens (median 1,778) (p. 5).
  - 420 annotated test notes give 13 per-variable test sets (p. 6).
  - The retrieval comparison used the 50% longest notes (p. 8).
  - The CheXpert split counts are internally inconsistent (p. 5), and the abstract's "20,000 clinical notes" cannot be reconciled with them.
- **Annotators:** Five board-certified physicians and one medical student. **IAA: unweighted Cohen's κ 0.86 (95% CI 0.79–0.93) for MOUD and 0.93 (0.88–0.98) for CheXpert** (p. 2, §Inter-rater reliability).
- **Output schema:** One ternary label per variable: 0 = absent/negated, 1 = present, 2 = uncertain. 18 variables in total (13 MOUD, 5 CheXpert) (p. 7).
- **Prompting:** **Per target variable.**
  - Retrieval runs for an "input target entity" through five steps: Flan-T5-XXL zero-shot NER, then embedding filter (cosine ≥0.85), then a GPT-4 relevance filter, then UMLS/GPT-4 synonym augmentation, then MedSpaCy matching.
  - It returns ±150-word windows. **Each retrieved chunk is sent in a separate model call** ("all models were called once per retrieved chunk", p. 4), and chunk labels are aggregated per note.
  - Prompts are 5-shot, with synthetic examples generated by GPT-4 (p. 7).
- **Models:**
  - Run locally (PHI-compliant VM, 4×A100 80GB): Med42-70B, Mixtral-8x7B-Instruct, Llama-3-70B, Flan-T5-XXL, Flan-UL2.
  - GPT-4 through a PHI-compliant Azure instance (p. 7).
- **Grounding:** At the retrieval level only: the model sees entity-anchored windows. No output-to-span verification.
- **Key results:**
  - CLEAR vs embedding RAG vs full note (Abstract, p. 1): F1 0.90 / 0.86 / 0.79; seconds per note 4.95 / 17.41 / 20.08; queries per note 1.68 / 4.94 / 4.18; about 1.1k / 3.8k / 6.1k input tokens per note.
  - MOUD mean F1 0.90 (Med42 0.78 to GPT-4 0.97) (Table 1, p. 3).
  - Removing NER lowers F1 from 0.97 to 0.86 (p. 2).
- **Code:** https://github.com/iv-lop/clear (p. 8). MOUD data not shareable.
- **Author-stated limitations** (p. 5):
  - only variable extraction evaluated;
  - the embedding baseline's chunk size may matter;
  - multiple chunks per prompt not explored;
  - CLEAR-step prompts not fully tuned;
  - COVID-era temporal split;
  - quantization not tested.

**Citable claims**
- "We show that CLEAR, when used for extraction of 13 variables from clinical notes, outperformed chunk embedding and full-note approaches, achieving 3% higher F1 on average with 71% fewer input tokens, 72% faster inference time, and 66% fewer model queries." (p. 4, §Discussion)
- "In addition, LLM performance has been shown to degrade on reasoning tasks as input length increases, even on models with large context windows, suggesting that inputting long EHR excerpts containing extraneous information can reduce performance." (p. 2, Introduction; citation superscript removed)
- "In our own analysis, models like Mixtral, Llama, and GPT-4, despite having context windows large enough to accommodate multiple notes, did not perform as well as CLEAR when processing the full note." (p. 4, §Discussion)
- "Note that we processed each chunk in separate model calls rather than within a single large context." (p. 4, §Discussion)
- "Several CLEAR note chunks from different notes can be combined into a single prompt for LLM inference, however, this was not explored in our paper." (p. 5, §Discussion)
- "Dividing a note into smaller chunks with adjoining strides can address context window limits but still requires multiple LLM queries per patient, which can be computationally expensive." (p. 2, Introduction)

---

### spaanderman2025structured — Open-weight LLMs for structured extraction across use cases and languages

*Spaanderman DJ, Prathaban K, Zelina P, … Starmans MPA, Klein S (23 authors). arXiv:2511.10658v1 [cs.CL], 3 Nov 2025 (preprint). The PDF has 81 pages including the supplement; cite "PDF p."*

- **Design:** A retrospective multicentre benchmark with no fine-tuning: 15 open-weight LLMs × 6 prompting strategies × 7 datasets = 630 experiments. Linear mixed-effects variance analysis (PDF pp. 4–9).
- **Language and documents:** Dutch, English and Czech. Five pathology use cases and one radiology use case (brain MRI, neurodegenerative disease) (PDF p. 5).
- **Dataset size (reports):**
  - Colorectal liver metastases: 864.
  - Liver tumours: 289.
  - Neurodegenerative: 948.
  - Soft-tissue tumours: 300 English + 327 Dutch.
  - Melanoma: 1,252.
  - Sarcoma: 80 (Czech).
- **Annotators:** Vary by use case: one rater, students, clinicians, or 3 clinicians per report for sarcoma (Suppl. A).
  - **Inter-rater agreement** is measured with the task metrics, not κ, as a macro-average: neurodegenerative 0.88, soft-tissue English 0.73, soft-tissue Dutch 0.68, melanoma 0.76, sarcoma 0.78. None for the two liver datasets (PDF p. 10, §3.3).
- **Output schema:** One flat JSON per report, with typed fields, option lists and defaults.
  - Fields per prompt template: colorectal liver metastases 4, liver tumours 13, neurodegenerative 22, soft tissue 9, melanoma 15, sarcoma 7 (Tables A3–A14).
  - Table A1 gives 4/12/25/9/16/7.
  - Metrics by type: balanced accuracy (categorical), accuracy (numeric), cosine similarity (free text and lists) (PDF p. 7).
- **Prompting (PDF p. 7, §2.3):** zero-shot, one-shot, few-shot (3 examples), chain-of-thought, self-consistency, and **prompt graph**.
  - The prompt graph is a manually defined DAG of smaller sequential subtasks with conditional branches and shared conversational memory.
  - Every strategy except the prompt graph asks for **the whole schema in one JSON call**.
  - Whether a graph node is one variable or a group is not stated in the text; the DAG figures are images.
- **Models:** All open-weight and locally hosted (vLLM / SGLang on H100 / B200). The 15 models range from 1.5B to 685B:
  - DeepSeek-R1, Llama-4 Maverick/Scout, Qwen3-235B, Qwen2.5-72B, Nemotron-49B;
  - Gemma 3 27B/4B, Mistral Small 3.1 24B;
  - small distilled models;
  - three medical models: Med42, OpenBioLLM, MedGemma (Table 1, PDF p. 8).
- **Grounding:** None evaluated. The reasoning prompts ask the model to justify each field, but the justifications are not assessed.
- **Key results:**
  - Best macro-average per use case: 0.89 / 0.95 / 0.85 / 0.76 (English) / 0.70 (Dutch) / 0.81 / 0.76 (Table 1, PDF pp. 12–14).
  - Mean by size group (each model at its best strategy): large 0.78, medium 0.77, small 0.77, tiny 0.57, medical 0.73.
  - The prompt graph was top-ranked in 37 of 105 model–use-case pairs.
  - Mean gain over zero-shot: prompt graph +12.7%, few-shot +5.1% (§3.2).
  - Variance explained: LLM 18–37%, prompting strategy 0.2–35% (Table C2).
  - Time per report: few-shot 4.5 s, prompt graph 37.6 s (§3.5).
- **Code:** https://zenodo.org/records/17131185 (MedicalRecordLLM v0.1). No data-availability statement.
- **Author-stated limitations** (PDF p. 16):
  - no quantization or compression studied;
  - quantitative evaluation only;
  - 5 of 6 use cases are pathology;
  - incomplete, small-sample inter-rater agreement.
- **Caveats (internal inconsistencies):**
  - variable counts in Table A1 vs the prompts;
  - model size range "1.5B–650B" vs 685B;
  - the abstract's claim about few-shot gains vs §3.2.

**Citable claims**
- "Finally, graph prompting decomposes the task into a directed graph of smaller, interdependent subtasks, with conditional paths allowing subsequent prompts to depend on earlier answers [23]. The graph is defined manually, and while outputs are not directly passed between prompts, conversational memory is retained to maintain contextual consistency during sequential execution." (PDF p. 7, §2.3)
- "On average, using the best-performing prompting strategy for each model–use-case combination yielded a substantial improvement compared with the corresponding zero-shot baseline: +6.5% [0.8–12.3] for one-shot, +5.1% [2.4–7.8] for few-shot, +8.2% [2.2–14.2] for chain-of-thought, +6.1% [2.4–9.9] for self-consistency, and +12.7% [8.6–16.8] for prompt graph." (PDF p. 9, §3.2)
- "In contrast, more complex prompting strategies, such as selfconsistency and prompt graph, required considerably more GPU resources, requiring 15.9 s and 37.6 s per report, respectively." (PDF p. 14, §3.5; "selfconsistency" as in the converted text)
- "Mixed-effects modelling showed that the choice of LLM explained 18–37% of the performance variance, prompting strategy contributed 0.2–35%, and residual variability accounted for 45–80%, depending on the use case (Table C2)." (PDF p. 9, §3.2)
- "In contrast, fields requiring contextual interpretation or synthesis of dispersed information showed lower model performance." (PDF p. 10, §3.3)
- "Small-to-medium general-purpose models with optimised prompting achieve performance comparable to expert annotators, providing a practical approach for scalable clinical data curation." (PDF p. 2, Abstract)

*[Relevance]* This is the closest analogue to a grouped multi-call harness: a decomposed, sequential prompt graph run on open-weight models, compared with single-call baselines. Its largest single-call schema is 22 fields, far below 199.

---

### gallifant2025tripodllm — The TRIPOD-LLM reporting guideline

*Gallifant J, Afshar M, Ameen S, … Collins GS, Moons KGM, Celi LA, Bitterman DS (25 authors). Nat Med 2025;31(1):60–69. doi:10.1038/s41591-024-03425-5; PMID 39779929; PMC12104976. PDF pp. 1–10 = journal pp. 60–69. PDF pp. 11–12 are the online Methods and have no journal page number.*

- **Design:** A reporting guideline, an extension of TRIPOD+AI, developed by an **expedited Delphi** process plus expert consensus, and framed as a **living** guideline.
  - Candidate items came from TRIPOD-2015, TRIPOD+AI and the LLM reporting literature, giving 64 unique items.
  - The Methods describe one survey round (1 Mar–23 Apr 2024, 4-level rating scale).
  - An online consensus meeting followed.
  - Registered with EQUATOR on 2 May 2024. MIT COUHES exemption E-5705 (PDF pp. 11–12).
- **Scope:** Studies "developing, tuning, prompt engineering or evaluating an LLM" (p. 61).
  - The checklist is **modular** by research design: D (de novo development), M (LLM methods), E (LLM evaluation), H (evaluation in healthcare settings).
  - It is also modular by LLM task (Table 1, p. 62). Information extraction is not its own task category; in the Methods, text processing (entity recognition, relation extraction) is the closest (PDF p. 12).
- **Participants:** 26 of 56 invited completed the survey, from 9 countries; 20 of 26 worked mainly in AI/ML, clinical informatics or NLP (PDF p. 11). The steering group had 5 members and the expert panel 13. The number of consensus-meeting attendees is not reported.
- **Consensus rule (replaces IAA):** Items with less than 50% "essential" support were highlighted and deliberated. Consensus was reached in all cases by discussion "until no panel member had additional comments or disagreements" (PDF p. 12).
- **Output:** 19 main items and 50 subitems. 14 main items and 32 subitems apply to all designs and tasks (p. 61). There is also a 12-item abstract checklist, 2a–2l (Table 3, p. 67). See the checklist below and the count caveat under it.
- **Items relevant to an LLM-IE harness study:**

| Topic | Items |
|---|---|
| Model name, version, last training date | 6a |
| Generation details: prompt engineering, output consistency, seed, temperature, max tokens | 6c (M/D/E) |
| Prompt design and prompt-development data | 9a–9b |
| Raw vs post-processed output | 6d |
| Metrics and error types | 7a (coded for QA/IR/DG/SS/MT, not classification) |
| Date of inference for closed-source LLMs | 7c |
| Assessor qualifications and agreement | 7d |
| Annotation guidelines, annotator count, multiply-annotated share, IAA, annotator background | 8a–8c |
| Compute | 12 |
| Data and code availability | 14e–14f |
| Human oversight / autonomy | 19d |
| User interaction | 19f |

- **Grounding:** No dedicated item. Hallucination and omission are discussed in general terms (p. 61).
- **Availability:** Interactive checklist at https://tripod-llm.vercel.app/. Supplementary Tables 1–3 (example completed checklist, fillable checklist, explanation and elaboration) were not downloaded. The expert panel reviews the guideline every 3 months.
- **Author-stated limitations:**
  - the expedited Delphi "may introduce limitations in consensus and breadth of input" (p. 67);
  - designed for text-only LLMs;
  - the design and task categories are imperfect and overlapping (PDF p. 12);
  - the checklist will need updating.

**Citable claims**
- "The recommendations contained within TRIPOD-LLM are for completely and transparently reporting on how LLM-based research was conducted; TRIPOD-LLM does not prescribe how to develop or evaluate LLMs specifically. The checklist is not a quality appraisal tool." (p. 61 (PDF p. 2), §The TRIPOD-LLM statement)
- "Where relevant, reports must include comprehensive descriptions of data sources used for developing prompts, LLM model names and versions, any preprocessing steps undertaken and methods used in prompt engineering. This ensures that prompts are effectively designed to elicit stable and reproducible performance from LLMs." (p. 65 (PDF p. 6), §Discussion)
- "In addition, studies should document the model version date and whether the model was frozen or remained dynamic during the data collection phase." (p. 65 (PDF p. 6), §Discussion)
- "Furthermore, there is a focus on the quality control processes used in dataset development and evaluation, such as qualifications of human assessors, requirements for dual annotation and specific details on instructions provided to assessors to ensure that nuances of text evaluation are captured, thus facilitating reliable assessments of safety and performance." (p. 65 (PDF p. 6), §Discussion)
- "We carried out an expedited Delphi process to arrive at the initial version of the checklist included here but acknowledge that this may introduce limitations in consensus and breadth of input." (p. 67 (PDF p. 8), §Discussion)

#### TRIPOD-LLM main checklist (Table 2, pp. 63–64 = PDF pp. 4–5)

Item descriptions are copied verbatim from Table 2. Section grouping was checked against the rendered PDF page. Applicability codes: Research design — M, LLM methods; D, de novo LLM development; E, LLM evaluation; H, LLM evaluation in healthcare settings. LLM task — C, classification; OF, outcome forecasting; QA, long-form question answering; IR, information retrieval; DG, document generation; SS, summarization and simplification; MT, machine translation. The table footnote reads: "For studies using existing LLMs, users should include reference(s) to reportable information if provided by the original developers or state that this information is not available."

| Section | Item | Description (verbatim) | Research design | LLM task |
|---|---|---|---|---|
| Title | 1 | Identify the study as developing, fine-tuning and/or evaluating the performance of an LLM, specifying the task, the target population and the outcome to be predicted. | All | All |
| Abstract | 2 | See TRIPOD-LLM for abstracts. | All | All |
| Introduction: Background | 3a | Explain the healthcare context/use case (for example, administrative, diagnostic, therapeutic and clinical workflow) and rationale for developing or evaluating the LLM, including references to existing approaches and models. | All | All |
| Introduction: Background | 3b | Describe the target population and the intended use of the LLM in the context of the care pathway, including its intended users in current gold standard practices (for example, healthcare professionals, patients, public or administrators). | E, H | All |
| Objectives | 4 | Specify the study objectives, including whether the study describes the initial development, fine-tuning or validation of an LLM (or multiple stages). | All | All |
| Methods: Data | 5a | Describe the sources of data separately for the training, tuning and/or evaluation datasets and the rationale for using these data (for example, web corpora, clinical research/trial data, EHR data or unknown). | All | All |
| Methods: Data | 5b | Describe the relevant data points and provide a quantitative and qualitative description of their distribution and other relevant descriptors of the dataset (for example, source, languages and countries of origin). | All | All |
| Methods: Data | 5c | Specifically state the date of the oldest and newest item of text used in the development process (training, fine-tuning and reward modeling) and the evaluation datasets. | All | All |
| Methods: Data | 5d | Describe any data preprocessing and quality checking, including whether this was similar across text corpora, institutions and relevant sociodemographic groups. | All | All |
| Methods: Data | 5e | Describe how missing and imbalanced data were handled and provide reasons for omitting any data. | All | All |
| Analytical methods | 6a | Report the LLM name, version and last date of training. | All | All |
| Analytical methods | 6b | Report details of the LLM development process, such as LLM architecture, training, fine-tuning procedures and alignment strategy (for example, reinforcement learning and direct preference optimization) and alignment goals (for example, helpfulness, honesty and harmlessness). | M, D | All |
| Analytical methods | 6c | Report details of how the text was generated using the LLM, including any prompt engineering (including consistency of outputs), and inference settings (for example, seed, temperature, max token length and penalties), as relevant. | M, D, E | All |
| Analytical methods | 6d | Specify the initial and postprocessed output of the LLM (for example, probabilities, classification and unstructured text). | All | All |
| Analytical methods | 6e | Provide details and rationale for any classification and, if applicable, how the probabilities were determined and thresholds identified. | All | C, OF |
| LLM output | 7a | Include metrics that capture the quality of generative outputs, such as consistency, relevance, accuracy and presence/type of errors compared to gold standards. | All | QA, IR, DG, SS, MT |
| LLM output | 7b | Report the outcome metrics' relevance to the downstream task at deployment time and, where applicable, the correlation of metric to human evaluation of the text for the intended use. | E, H | All |
| LLM output | 7c | Clearly define the outcome, how the LLM predictions were calculated (for example, formula, code, object and API), the date of inference for closed-source LLMs and evaluation metrics. | E, H | All |
| LLM output | 7d | If outcome assessment requires subjective interpretation, describe the qualifications of the assessors, any instructions provided, relevant information on demographics of the assessors and interassessor agreement. | All | All |
| LLM output | 7e | Specify how performance was compared to other LLMs, humans and other benchmarks or standards. | All | All |
| Annotation | 8a | If annotation was done, report how the text was labeled, including providing specific annotation guidelines with examples. | All | All |
| Annotation | 8b | If annotation was done, report how many annotators labeled the dataset(s), including the proportion of data in each dataset that was annotated by more than one annotator, and the interannotator agreement. | All | All |
| Annotation | 8c | If annotation was done, provide information on the background and experience of the annotators or the characteristics of any models involved in labeling. | All | All |
| Prompting | 9a | If research involved prompting LLMs, provide details on the processes used during prompt design, curation and selection. | All | All |
| Prompting | 9b | If research involved prompting LLMs, report what data were used to develop the prompts. | All | All |
| Summarization | 10 | Describe any preprocessing of the data before summarization. | All | SS |
| Instruction tuning/alignment | 11 | If instruction tuning/alignment strategies were used, what were the instructions, data and interface used for evaluation, and what were the characteristics of the populations doing the evaluation? | M, D | All |
| Compute | 12 | Report compute, or proxies thereof (for example, time on what and how many machines, cost on what and how many machines, inference time, floating-point operations per second), required to carry out methods. | M, D, E | All |
| Ethical approval | 13 | Name the institutional research board or ethics committee that approved the study and describe the participant-informed consent or the ethics committee waiver of informed consent. | All | All |
| Open science | 14a | Give the source of funding and the role of the funders for the present study. | All | All |
| Open science | 14b | Declare any conflicts of interest and financial disclosures for all authors. | All | All |
| Open science | 14c | Indicate where the study protocol can be accessed or state that a protocol was not prepared. | H | All |
| Open science | 14d | Provide registration information for the study, including register name and registration number, or state that the study was not registered. | H | All |
| Open science | 14e | Provide details of the availability of the study data. | All | All |
| Open science | 14f | Provide details of the availability of the code to reproduce the study results. | All | All |
| Public involvement | 15 | Provide details of any patient and public involvement during the design, conduct, reporting, interpretation or dissemination of the study or state no involvement. | H | All |
| Results: Participants | 16a | When using patient/EHR data, describe the flow of text/EHR/patient data through the study, including the number of documents/questions/participants with and without the outcome/label and follow-up time as applicable. | E, H | All |
| Results: Participants | 16b | When using patient/EHR data, report the characteristics overall and for each data source or setting and development/evaluation splits, including the key dates, key characteristics and sample size. | E, H | All |
| Results: Participants | 16c | For LLM evaluation that includes clinical outcomes, show a comparison of the distribution of important clinical variables that may be associated with the outcome between development and evaluation data, if available. | E, H | All |
| Results: Participants | 16d | When using patient/EHR data, specify the number of participants and outcome events in each analysis (for example, for LLM development, hyperparameter tuning and LLM evaluation). | E, H | All |
| Performance | 17 | Report LLM performance according to prespecified metrics (see item 7a) and/or human evaluation (see item 7d). | All | All |
| LLM updating | 18 | If applicable, report the results from any LLM updating, including the updated LLM and subsequent performance. | All | All |
| Discussion: Interpretation | 19a | Give an overall interpretation of the main results, including issues of fairness in the context of the objectives and previous studies. | All | All |
| Limitations | 19b | Discuss any limitations of the study and their effects on any biases, statistical uncertainty and generalizability. | All | All |
| Usability of the LLM in context | 19c | Describe any known challenges in using data for the specified task and domain context with reference to representation, missingness, harmonization and bias. | E, H | All |
| Usability of the LLM in context | 19d | Define the intended use for the implementation under evaluation, including the intended input, end-user and level of autonomy/human oversight. | E, H | All |
| Usability of the LLM in context | 19e | If applicable, describe how poor quality or unavailable input data should be assessed and handled when implementing the LLM; that is, what is the usability of the LLM in the context of current clinical care. | E, H | All |
| Usability of the LLM in context | 19f | If applicable, specify whether users will be required to interact in the handling of the input data or use of the LLM, and what level of expertise is required of users. | E, H | All |
| Usability of the LLM in context | 19g | Discuss any next steps for future research, with a specific view of the applicability and generalizability of the LLM. | All | All |

Count: 49 numbered entries (items 1–19 with sub-items) in Table 2.

The text (p. 61, PDF p. 2, §The TRIPOD-LLM statement) says: "The TRIPOD-LLM checklist comprises 19 main items [...] These main items are further divided into 50 subitems. Of these, 14 main items and 32 subitems are applicable to all research designs and LLM tasks." Fig. 1 (PDF p. 11, in the Methods, which carry no journal page number) refers to "59 reporting items". Table 2 as printed has 49 numbered rows: 10 items with no sub-items and 39 lettered sub-items. The difference from "50 subitems" cannot be explained from the text. The table above reproduces what is printed; note this when reporting compliance counts.

#### TRIPOD-LLM for abstracts (Table 3, p. 67 = PDF p. 8)

Checklist items copied verbatim. Section grouping was checked against the rendered page.

| Section | Item | Checklist item (verbatim) | Research design | LLM task |
|---|---|---|---|---|
| Title | 2a | Identify the study as developing, fine-tuning and/or evaluating the performance of an LLM, specifying the task, the target population and the outcome to be predicted. | All | All |
| Background | 2b | Provide a brief explanation of the healthcare context, use case and rationale for developing or evaluating the performance of an LLM. | E, H | All |
| Objectives | 2c | Specify the study objectives, including whether the study describes LLMs development, tuning and/or evaluation | All | All |
| Methods | 2d | Describe the key elements of the study setting. | All | All |
| Methods | 2e | Detail all data used in the study, specify data splits and any selective use of data. | M, D, E | All |
| Methods | 2f | Specify the name and version of LLM(s) used. | All | All |
| Methods | 2g | Briefly summarize the LLM-building steps, including any fine-tuning, reward modeling and RLHF. | M, D | All |
| Methods | 2h | Describe the specific tasks performed by the LLMs (for example, medical QA, summarization and extraction), highlighting key inputs and outputs used in the final LLM. | All | All |
| Methods | 2i | Specify the evaluation datasets/populations used, including the endpoint evaluated, and detail whether this information was held out during training/tuning where relevant and what measure(s) were used to evaluate LLM performance. | All | All |
| Results | 2j | Give an overall report and interpretation of the main results. | All | All |
| Discussion | 2k | Explicitly state any broader implications or concerns that have arisen in light of these results. | All | All |
| Other | 2l | Give the registration number and name of the registry or repository (if relevant). | H | All |

Supplementary material mentioned in the text but NOT downloaded here: Supplementary Table 1 (example completed checklist), Supplementary Table 2 (fillable checklist), Supplementary Table 3 (explanation and elaboration). Interactive checklist: https://tripod-llm.vercel.app/

---

### collins2024tripodai — TRIPOD+AI statement

*Collins GS, Moons KGM, Dhiman P, … Wynants L, Logullo P (34 authors). BMJ 2024;385:e078378. doi:10.1136/bmj-2023-078378; PMID 38626948. Text from the BMJ PDF (UCL Discovery copy); cite by PDF page.*

- **Design:** A reporting guideline that updates and supersedes TRIPOD 2015. It was developed through:
  - literature reviews;
  - a 2-round modified Delphi (Welphi, 4-level scale);
  - a patient and public involvement and engagement meeting;
  - an online consensus meeting (PDF pp. 3–6).
  
  EQUATOR registration 2019. Protocol on OSF (2021). Consensus methods reported following ACCORD.
- **Scope:** Studies that develop and/or evaluate diagnostic or prognostic prediction models using regression or machine learning. Items are labelled D (development) and/or E (evaluation). It is "primarily aimed at non-generative models" (PDF p. 9).
- **Participants:**
  - Delphi Round 1: 170 of 292 invited completed; 22 countries.
  - Delphi Round 2: 200 of 395 invited completed; 27 countries (PDF p. 5).
  - Patient and public involvement meeting: 9 members.
  - Consensus meeting: 28 attendees, 1 non-voting.
- **Consensus rule (replaces IAA):** At least 70% rating an item "desirable" or "essential" to carry it forward (PDF p. 5). At the meeting, polls were held on the remaining items; the vote threshold is not stated.
- **Output:** 27 main items and 52 subitems (PDF p. 7), plus a 13-item TRIPOD+AI for Abstracts checklist (Table 3).
  - Box 2 summarizes the changes: fairness throughout, an open-science section (18a–f), patient and public involvement (19), and subgroup performance (23a).
  - No count of new vs modified items is given.
- **Items relevant to an LLM-IE harness study** (Table 2):
  - 8b–8c: qualifications of outcome assessors; blinding.
  - 12c: model-building steps and tuning.
  - 12g: how predictions are calculated (code / API).
  - 18e–18f: data and code availability.
  - 23a: performance with confidence intervals and subgroups.
  - 27a–27b: poor-quality input data; user interaction and expertise.
  - There is no explicit item on prompting, annotator agreement or model version.
- **Grounding:** Not applicable.
- **Availability:** https://www.tripod-statement.org; OSF https://osf.io/zyacb/; supplementary expanded checklist.
- **Limitations:** No dedicated section. The authors say LLMs and foundation models were not considered (PDF p. 9), and a full explanation and elaboration document was still to follow (PDF p. 8).
- **Why cite it here:** TRIPOD-LLM is built on it. Cite it for general prediction-model reporting items, and use TRIPOD-LLM for the LLM-specific ones.

**Citable claims**
- "At the time of guideline development, foundation and large language models (such as ChatGPT) that are rapidly gaining momentum were not considered—the TRIPOD+AI guidance is primarily aimed at non-generative models. However, many of the principles are applicable for driving transparency in generative AI studies in health." (PDF p. 9, §Discussion)
- "If a particular checklist item cannot be discussed in the report because the information is unknown or irrelevant, then this should be acknowledged and clearly stated." (PDF p. 8, §How to use TRIPOD+AI)
- "The recommendations contained within TRIPOD+AI are the minimum reporting recommendations, and authors may provide additional information." (PDF p. 8, §How to use TRIPOD+AI)
- "Poor reporting of a model might also mask flaws in the design, data collection, or conduct of a study that, if the model was implemented in the clinical pathway, could cause harm." (PDF p. 2, Introduction)
- "Authors have an ethical and scientific obligation to honestly report their research in a complete and transparent manner." (PDF p. 2, Introduction)

---

### liu2020consortai — CONSORT-AI extension

*Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK; SPIRIT-AI and CONSORT-AI Working Group. BMJ 2020;370:m3164. doi:10.1136/bmj.m3164; PMID 32909959. Text from Europe PMC XML; cite by section or item. Also published in Nat Med 2020;26(9):1364–1374 and Lancet Digit Health 2020;2(10):e537–e548 (verified via Crossref; the BMJ text itself does not mention co-publication).*

- **Design:** An extension of CONSORT 2010, developed jointly with SPIRIT-AI:
  - a ClinicalTrials.gov scan on 13 May 2019 (316 AI trials registered);
  - 29 candidate items;
  - a 2-round e-Delphi on a 9-point scale;
  - a 2-day consensus meeting in January 2020;
  - a pilot of the checklist (§Methods).
- **Scope:** Reports of **randomized trials** of interventions with an AI component. For model development or validation studies the authors point to TRIPOD-ML and STARD-AI (§Discussion). It does not apply directly to a retrospective extraction benchmark.
- **Participants:** 169 invited to the Delphi; 103 (Round 1) and 91 (Round 2) responded. Consensus meeting: 31 stakeholders, 41 items discussed. Pilot: 34 participants.
- **Consensus rule (replaces IAA):** 80% pre-specified for inclusion, voted anonymously.
- **Output:** 14 new items (11 extensions and 3 elaborations) added to CONSORT 2010 (Table 1).
- **Items relevant here:**
  - 5(i): AI version.
  - 4a(ii), 5(ii), 5(iii): input data inclusion, acquisition and handling of poor-quality input.
  - 5(iv): human–AI interaction and expertise.
  - 5(v), 5(vi): output and how it contributes to decisions.
  - 19: analysis of performance errors.
  - 25: access to the AI intervention and code.
  - Prompting and annotation are not addressed (the guideline predates LLMs).
- **Grounding:** Not applicable.
- **Availability:** No website or tool; supplementary appendix only.
- **Author-stated limitations (§Discussion):**
  - few published AI trials existed;
  - search terms excluded decision-support and expert systems;
  - candidate items came from a small group;
  - bias toward detection and diagnosis applications;
  - continuously learning AI excluded.

**Citable claims**
- "CONSORT-AI recommends that investigators provide clear descriptions of the AI intervention, including instructions and skills required for use, the setting in which the AI intervention is integrated, the handling of inputs and outputs of the AI intervention, the human-AI interaction and providing analysis of error cases." (Abstract)
- "Reporting performance errors and failure case analysis is especially important for AI interventions." (§Results, CONSORT-AI 19 Extension, Explanation)
- "It is therefore important to specify which version of the AI system was used in the clinical trial, whether this is the same as the version evaluated in previous studies that have been used to justify the study rationale, and whether the version changed during the conduct of the trial." (CONSORT-AI 5 (i) Extension, Explanation)
- "Completeness and transparency of this description is integral to the replicability of the intervention beyond the clinical trial in real-world settings." (CONSORT-AI 5 (ii) Extension, Explanation)
- "Beyond this, investigators should also be encouraged to explore differences in performance and error rates across population subgroups." (§Discussion)

---

### rivera2020spiritai — SPIRIT-AI extension

*Cruz Rivera S, Liu X, Chan A-W, Denniston AK, Calvert MJ; SPIRIT-AI and CONSORT-AI Working Group. BMJ 2020;370:m3210. doi:10.1136/bmj.m3210; PMID 32907797. Text from Europe PMC XML; cite by section or item. Also published in Nat Med 2020;26(9):1351–1363 and Lancet Digit Health 2020;2(10):e549–e560 (verified via Crossref; not mentioned in the BMJ text).*

- **Design:** An extension of SPIRIT 2013, developed with CONSORT-AI in the same staged process: literature review, 2-round e-Delphi, consensus meeting in January 2020, pilot (§Methods).
- **Scope:** **Trial protocols** for interventions with an AI component. It does not apply directly to a retrospective extraction study, but its pre-specification logic suits a study protocol. Examples: 6a(ii) for prior evidence, 22 for the planned error analysis.
- **Participants:** Shared with CONSORT-AI (169 invited; 103 and 91 Delphi responses; 31 at the consensus meeting; 34 in the pilot). This paper says 38 items were discussed at the meeting, whereas CONSORT-AI says 41.
- **Consensus rule:** 80% pre-specified.
- **Output:** 15 new items (12 extensions and 3 elaborations) added to SPIRIT 2013 (Table 1).
- **Items relevant here:**
  - 11a(i): AI version.
  - 10(ii), 11a(ii), 11a(iii): input data handling.
  - 11a(iv): human–AI interaction.
  - 11a(v), 11a(vi): output and how it contributes to decisions.
  - 22: plans to analyse performance errors.
  - 29: access to the AI and code.
  - 6a(ii): pre-existing evidence.
- **Grounding:** Not applicable.
- **Availability:** No website; supplementary appendix only.
- **Author-stated limitations (§Discussion):**
  - "only seven published trials and no published trial protocols" were available;
  - the same search and small-group limitations as CONSORT-AI;
  - focus on detection and diagnosis.

**Citable claims**
- "The guidance does not aim to be prescriptive regarding the methodological approach to AI trials; rather it aims to promote transparency in reporting the design and methods of a clinical trial to facilitate understanding, interpretation, and peer review." (§Discussion)
- "The protocol should specify whether there are any plans to analyse performance errors. If there are no plans for this, a justification should be included in the protocol." (SPIRIT-AI 22 Extension, Explanation)
- "The procedure for how input data will be handled—including data acquisition, selection, and pre-processing before analysis by the AI system—should be provided." (SPIRIT-AI 11a (ii) Extension, Explanation)
- "The protocol should state which version of the AI system will be used in the clinical trial, and whether this is the same version that had been used in previous studies to justify the study rationale." (SPIRIT-AI 11a (i) Extension, Explanation)
- "Authors should describe in the protocol any pre-existing published (with supporting references) or unpublished evidence relating to validation of the AI intervention, or lack thereof." (SPIRIT-AI 6a (ii) Extension, Explanation)

---

### psych2stage2026 — Two-stage extraction of psychiatric clinical course (JMIR Form Res)

*Chen CH, Tseng PC, Dai HJ, Su CH, Wang SH, Chien YL, Huang WL, Wu CS, Chen HH. JMIR Form Res 2026;10:e94454. doi:10.2196/94454; PMID 42560822; PMC13446380. Published 6 Aug 2026. Text from Europe PMC XML; cite by section.*

- **Design:** A single-centre retrospective study with 10-fold cross-validation. A fine-tuned 2-stage pipeline is compared with "direct" chart-level prediction and with single-stage "joint" extraction (§Model Development; Table 4).
- **Language and documents:** Psychiatric discharge summaries (history of present illness only) from NTUH-iMD, Taiwan. Mostly English, with some Chinese or code-mixed content.
- **Dataset size:** 500 summaries with 12,947 sentences, giving 7,177 event and 4,842 temporal annotations.
- **Annotators and agreement:** A psychiatrist and an NLP researcher, with consensus adjudication. Cohen κ is 0.78 overall: calendar dates 0.90, hospitalization 0.87, vague time 0.47.
- **Output schema:**
  - Stage 1, per sentence: an event label (symptom/episode, hospitalization, remission/response, none) plus the time.
  - Stage 2, per chart: onset time, episode count, hospitalization count, most recent hospitalization.
- **Intermediate representation:** An ordered list of "[SENTENCE] | [EVENT] | [TIME]" rows. It is the only input to stage 2.
- **Prompting:** One call per sentence, then one chart-level call. The output is plain text. Structured-output, no-few-shot and CoT variants were tested in a prompt-sensitivity analysis.
- **Models:** Llama-3.1-8B-Instruct, MentaLLaMA, OpenBioLLM and Ministral-8B, each LoRA-fine-tuned for each stage and run locally on one A6000. Bio_ClinicalBERT is a sentence-level baseline only.
- **Grounding:** Not addressed. Stage-2 input keeps the source sentence.
- **Compared with direct/single-step extraction:**
  - Onset accuracy: 2-stage 0.734–0.772 vs direct 0.558–0.648 and joint 0.484–0.644 (all P≤.002).
  - Last hospitalization: better than direct for all models; vs joint, mostly not significant (Table 5).
- **Where it helps / where it does not:**
  - The largest gain is on temporal synthesis (onset).
  - Hospitalization count: the best result was LLaMA with direct prompting (0.692), and 2-stage vs direct was not significant (P=.56, .99).
- **Error propagation:**
  - Oracle (gold) stage-1 input improved onset for only 2 of 4 models. It *lowered* last-hospitalization accuracy for all models.
  - The authors place many errors in stage-2 aggregation, and note that stage 2 was trained on predicted, not gold, inputs.
- **Error analysis:** ambiguous time 30.7%, missing information 14.8%, episode–hospitalization conflation 11.4%.
- **Cost:** Fine-tuning takes 2–3 h per fold; inference about 20 min per fold per model. No cost comparison between arms.
- **Code and data:** Data not public. Code not reported.
- **Author-stated limitations:**
  - single hospital;
  - mostly English;
  - onsets of comorbid diagnoses not separated;
  - only 4 chart features;
  - research prototype that needs prospective validation.

**Citable claims**
- "Stage 2—chart-level aggregation and prediction: all sentence-level predictions are assembled into a structured list maintaining original document order, with the format: [SENTENCE]: <text >| [EVENT]: <label >| [TIME]: <temporal info or “none”>." (§Methods › Model Development)
- "For all 4 models, the 2-stage framework significantly outperformed both the direct and joint approaches for onset prediction (all bootstrap P≤.002)." (§Results › Clinical Course Information Extraction Results)
- "Although the joint approach explicitly incorporates sentence-level extraction, it still requires event extraction and chart-level prediction to be performed within a single prompt-response process. In contrast, the proposed framework decomposes the task into 2 sequential steps." (§Discussion › Principal Results)
- "This suggests that many chart-level errors arose from the second-stage aggregation and reasoning process, such as selecting the correct onset time, distinguishing episodes from hospitalizations, and integrating multiple temporally distributed events across a discharge summary." (§Discussion › Principal Results)
- "For hospitalization count prediction, improvements over the direct approach were limited, with no significant differences observed for either LLaMA (P=.56) or Mistral (P=.99)." (§Results › Clinical Course Information Extraction Results)
- "For the most recent hospitalization, oracle performance was consistently lower than that of the complete pipeline (eg, Mistral: 0.796 vs 0.858; LLaMA: 0.846 vs 0.866)." (§Results › Oracle Analysis Results)

*[Relevance]* This is the closest clinical analogue to arm C's first call. Building a structured event–time layer before chart-level reasoning beat direct and joint prompting for a temporally synthesized variable (onset), but not for simple counts. The oracle result warns that the downstream call must be tuned to the representation it actually receives.

---

### clinicirca2026 — CliniCIRCA: calendar-anchored patient-journey timelines from discharge summaries

*Zhang AI, Ishfaq N, Chandra M, Alvarez Lesmes S, Coscia A, Chelidze Moon K, Ding X, De Choudhury M. arXiv:2609.19585v1 [cs.CL], 17 Sep 2026 (preprint, no venue). The PDF has 34 pages including appendices; cite "PDF p."*

- **Design:** A three-stage sequential LLM pipeline (§3, PDF p. 3). Stage 1 extracts open-vocabulary atomic events from the raw note (no chunking); Stage 2 tags each event with an ISO date/range and one of [EXACT], [APPROX], [PRE ADM], [INDETERMINATE], resolved against admission, discharge and birth dates; Stage 3 writes a date-grouped summary. 11 LLMs compared on Stages 1–2; the winner is frozen for all stages. 1,000 silver timelines then train 5 open-weight models (§6).
- **Language and documents:** English MIMIC-III v1.4 discharge summaries of admissions with any ICD-9 290–319 code (14,882 summaries), one summary per reconstruction.
- **Dataset size:** Benchmark of 52 summaries (mean 1,774 words), 15,891 Stage-2 events; silver split 750/100/150.
- **Annotators and agreement:** Two psychiatric clinicians plus two annotators reviewed all 15,891 events and corrected 629 errors (608 temporal). LLM judge vs gold: κ 0.655, AC1 0.972 (App. G). Human–human IAA not reported.
- **Intermediate representation:** Output A, a list of (date + certainty tag, atomic event) pairs; Stage 2 also receives the full note "as global context" (App. D.2). Output B may use only facts from Output A (App. H).
- **Models:** Gemini 2.5 Pro selected (Stage-2 Likert 5.00/5.00/4.83; MEDCON F1 0.710, Table 1); greedy decoding, t = 0 (App. B).
- **Grounding:** Events must restate the source without inference; 7 hallucinations found by humans only.
- **Compared with direct/single-step extraction:** Not tested (Limitations).
- **Where it helps / where it does not:** Extraction is near-faithful; residual errors are temporal: 175 over-specified tags on pre-admission medications (151) and demographics (24), 169 of them missed by the judge (App. G.1).
- **Error propagation:** Each stage consumes the previous output; Stage 3 was run on the clinician-corrected timeline, so end-to-end propagation is not measured.
- **Key results:** Stage 3 compresses 1.52×; instruction tuning on silver data beats prompting on event extraction (best RM-F1 0.847, Table 3).
- **Cost:** 61.84M tokens for 1,000 admissions (61,836 per admission); Stage 1 alone used 25.7M (Table A3, App. A.3).
- **Code and data:** Anonymized repository https://anonymous.4open.science/r/CliniCIRCA-E5FF/.
- **Author-stated limitations:** date-centred schema forces timing on atemporal facts; salience defined and judged by the same clinicians; single-document scope; no single-pass baseline.

**Citable claims**
- "Decomposing the task in this way allows each stage to be prompted, evaluated, and improved independently, and confines each temporal decision to the stage best positioned to make it." (PDF p. 3, §3)
- "We select based on Stage 2 because the summary stage depends on the accuracy of its event-level temporal input." (PDF p. 3, §4.2)
- "We therefore compare 11 candidate models under the same framework (Section 4), but do not include a single-pass end-to-end baseline." (PDF p. 9, Limitations)
- "The pattern therefore represents a systematic false-negative class in which the judge accepts admission-anchored [EXACT] or [APPROX] labels for standing or pre-admission facts that should receive [PRE ADM]." (PDF p. 21, App. G.1)
- "In short, on everything except temporal tagging the model is essentially faithful; its only residual weakness is a tendency to resolve ambiguity in the source rather than preserve it." (PDF p. 24, App. G.2)
- "All other generation settings were held constant across models, and for openweight models this produces byte-identical outputs across runs." (PDF p. 16, App. B; "openweight" as converted; the claim is asserted, not measured)

*[Relevance]* This is the closest analogue to arm C: a note-wide, anchored event timeline is built once and reused downstream. It gives no head-to-head evidence, since there is no single-pass baseline. Its main residual error, pre-admission versus in-stay classification, maps onto arm C's antecedent/acute split. That error is also the one an LLM judge misses.

---

### promptplanextract2026 — Prompt, Plan, Extract: zero-shot agentic workflow for lung pathology

*Pathak A, Peng C, Lyu M, Chen Z, Solan R, Talankar S, Khan Y, Mehta H, Chen A, Guo Y, Wu Y. arXiv:2606.19852v2 [cs.CL], 25 Jun 2026 (preprint; v1 18 Jun 2026). Cite "PDF p."*

- **Design:** A single-centre exploratory study.
  - A zero-shot LangGraph workflow (5 open-weight LLMs) is compared with a supervised GatorTron NER→RE pipeline (PDF pp. 3–5).
  - There is **no single-call LLM baseline and no ablation** of the workflow nodes.
- **Language and documents:** English lung-resection pathology reports, UF Health, 2018–2022.
- **Dataset size:** 286 reports labelled after calibration, split 7:1:2. The test set was 58 reports, reduced to 53 after removing 5 with empty gold standards (PDF p. 3).
- **Annotators and agreement:** 3 annotators plus a domain expert. Final calibration round (22 reports): entity F1 0.843 (κ 0.810), relation F1 0.802.
- **Output schema:** CAP-aligned JSON with 13 fields (histology, grade, site, laterality, focality, size, VPI, LVI, margin status/distance, LN counts, stage) plus an "add_attrs" catch-all.
- **Intermediate representation:**
  - The Mapper splits the report into sections (SPECIMEN, TUMOR, MARGINS, LYMPH NODES, PATHOLOGIC STAGE).
  - The Planner extracts metadata for each section (focality, count hints, margin cues, pTNM vs ypTNM context).
  - This metadata goes into every Executor prompt as "structured context hints" (PDF pp. 4–5).
- **Prompting:** Role prompts per node; Planner and Executor tasks run concurrently; a Compiler merges the JSON fragments. Zero-shot, temperature 0, up to 2 retries.
- **Models:** gpt-oss-20b, gpt-oss-120b, Gemma-3-27B-it, Llama-3.3-70B-Instruct and Granite-3.3-8B-Instruct, all with identical prompts.
- **Grounding:** None. Outputs are not linked to spans.
- **Key results (Table 1, PDF p. 6):**
  - Micro-F1: NER-RE 0.960; LLMs 0.831–0.893. The best LLM is gpt-oss-20b (P 0.843, R 0.949).
  - Every LLM has recall >0.92, with precision 0.748–0.843.
- **Where it helps / where it does not (Table 2):**
  - Pathologic stage, which needs T/N/M synthesis, reaches 0.915–0.994; Granite beats the baseline.
  - Histology is competitive with the baseline.
  - Weak on tumor size (≤0.849), LN involved count (≤0.772) and VPI (0.308–0.348).
- **Compared with direct/single-step extraction:** Not tested.
- **Error propagation:** Argued for the NER→RE cascade; not measured for the workflow.
- **Cost:** Workflow: a mean of 27.5–63.5 s per report (medians 24.65–35.71 s). Baseline: about 22 h of GPU training plus 286 annotated reports.
- **Evaluation caveats:** Concept-level deduplication, normalization, an "Implicit Null" forgiveness rule, and all margins collapsed into one category.
- **Code and data:** Not reported.
- **Author-stated limitations:**
  - single centre with a small test set;
  - sensitivity to prompt wording not evaluated;
  - LLMs not yet on par with the supervised model.

**Citable claims**
- "Critically, the Planner's outputs were passed to the Executor as structured context hints, reducing ambiguity in complex cases such as multi-focal tumors or post-neoadjuvant reports." (PDF p. 5, §Prompt Design & Experimental Setup)
- "For each task, a prompt is constructed that includes (i) the relevant section text (from Mapper), (ii) the extracted metadata (from Planner), and (iii) a concise instruction to return a structured JSON response." (PDF p. 4, §Zero-Shot Agentic Workflow)
- "Similar to the planner, tasks are run concurrently, which reduces wall-clock latency while preserving isolation between tasks." (PDF p. 4, §Zero-Shot Agentic Workflow)
- "However, the generative LLMs lagged slightly on strictly numeric fields such as Tumor Size, where the baseline (0.931 F1) outperformed the best LLM (GPT-OSS20B: 0.849 F1)." (PDF p. 7, §Results; "GPT-OSS20B" as in the converted text)
- "In this study, we did not formally evaluate the system's sensitivity to semantic variations in prompt phrasing." (PDF p. 5, §Prompt Design & Experimental Setup)
- "The fully supervised model is based on multi-stage architecture (NER followed by RE), creating a pipeline cascade where error propagation at the span level renders subsequent extraction impossible." (PDF p. 7, §Discussion)

*[Relevance]* Architecturally, this is the nearest analogue to arm C: a first pass builds shared metadata, the metadata is injected into parallel per-section extraction calls, and a compiler merges the results. It gives no evidence on whether the shared context helps, because no single-call or no-Planner comparison was run.

---

### cancerregistrymas2026 — Multi-agent open-source LLM for cancer registry extraction (BioNLP 2026)

*Aal Abdulsalam A, Al Zaabi A, Jeeballah R, El Keraby H. This is the ACL Anthology/Crossref order; the PDF byline puts Jeeballah R first and Aal Abdulsalam A last. BioNLP 2026, pp. 531–551. doi:10.18653/v1/2026.bionlp-1.43. Page refs: proceedings p. (PDF p.).*

- **Design:** A single-institution study.
  - A sequential LangGraph multi-agent pipeline is compared with direct prompting of the same model.
  - For the baseline, the best of 5 prompting strategies was chosen for each task (§3.8, p. 533).
  - No ablation.
- **Language and documents:** Pathology and medical reports ("concatenated clinical notes" in the baseline prompts) from Sultan Qaboos University Hospital, Oman. The language is not stated.
- **Dataset size:** 818 annotated cases; the evaluation uses breast (n=454) and colorectal (n=174). No split is reported, and the data on which prompts were "iteratively refined" is not stated (§3.3).
- **Annotators and agreement:** Pathologists, with a senior pathologist adjudicating. Overall κ 0.917; colorectal T κ 0.576 (App. B, p. 543).
- **Output schema:**
  - Grade, morphology, T, N, M and laterality, each from a closed label set.
  - Each agent returns the stated value, an estimated value, a certainty score (0–1) and an evidence quote (App. D).
- **Intermediate representation:** A shared LangGraph state (reports, retrieved evidence, intermediate outputs, predictions, confidence), persisted in SQLite. Chunks carry a field-focus label.
- **Prompting:**
  - Pipeline: chunking agent → field-conditioned retriever → one extraction agent per field → reviewer (schema validation and repair) → evaluator → aggregator.
  - Baseline: one prompt per field over the whole text (prefix, cloze, anticipatory, CoT or heuristic).
- **Models:** LLaMA 3.3 70B, run locally through Ollama on 2× RTX 6000 Ada.
- **Grounding:** Evidence quotes are requested but not checked against the source.
- **Compared with direct/single-step extraction:** Weighted F1 averaged over tasks (Table 5, p. 537):
  - breast: baseline 0.74 vs multi-agent 0.71;
  - colorectal: 0.63 vs 0.61.
- **Where it helps / where it does not:**
  - Helps on context-dependent fields: grade F1w 0.71→0.78 (breast) and 0.56→0.67 (colorectal); colorectal laterality 0.45→0.50.
  - Hurts on short, standardized fields: T (breast 0.75→0.66), M (0.60→0.48 and 0.66→0.48, through lost recall), colorectal morphology (0.87→0.80).
- **Error propagation:** The authors trace the losses mainly to retrieval and normalization, not to extraction itself.
- **Cost:** Extra overhead acknowledged, not measured.
- **Evaluation caveats:**
  - Predictions are mapped to the gold label set by an LLM normalizer (App. D.10).
  - The evaluator agent reads reference labels when they are available.
- **Code:** https://github.com/RihamJeeballah/multi-agent-cancer-registry-extraction.
- **Author-stated limitations:** No dedicated section. The text notes:
  - no ablation (p. 537);
  - lost recall for M stage;
  - multi-institution evaluation still needed (p. 538).

**Citable claims**
- "Pipeline-level inspection suggests that performance degradation primarily originates from retrieval and normalization stages rather than extraction itself. For structured fields, chunking and retrieval may occasionally remove useful context or introduce unnecessary normalization steps." (p. 537 (PDF p. 7), §4.5)
- "The baseline performs better in highly structured tasks such as TNM staging and morphology extraction, where clinically relevant information often appears in concise and standardized forms." (p. 537 (PDF p. 7), §4.5)
- "These improvements suggest that decomposition and field-specific evidence retrieval are beneficial when grade-related information is context-dependent or distributed across multiple report sections." (p. 535 (PDF p. 5), §4.1)
- "Figures 6 and 7 show that the multi-agent framework redistributes performance across tasks rather than uniformly improving all of them." (p. 536 (PDF p. 6), §4.5)
- "Compared to direct prompting, the proposed multi-agent framework introduces additional computational overhead due to sequential agent execution, retrieval stages, and intermediate validation steps." (p. 534 (PDF p. 4), §3.8)
- "The M sub-figure in Figure 4 highlights a clear precision– recall trade-off: although the multi-agent framework achieved higher precision in some settings, it suffered from substantially lower recall, suggesting conservative predictions that missed metastasisrelated cases." (p. 536 (PDF p. 6), §4.3.3; "precision– recall" and "metastasisrelated" as in the converted text)

*[Relevance]* This is direct evidence of a trade-off arm C must measure for each variable group. Decomposition with retrieval helped context-dependent variables but lost accuracy on explicit, standardized ones, mainly because chunking and retrieval removed context. Arm C adds context instead of removing it, and that design difference is worth stating.

---

### twophaseexam2025 — Two-phase LLM framework for medical feature extraction (JMIR Med Inform)

*Abumelha M, AL-Ghamdi AAM, Fayoumi A, Ragab M. JMIR Med Inform 2025;13:e78432. doi:10.2196/78432; PMID 41171081; PMC12712565. Published 3 Dec 2025. Text from Europe PMC XML; cite by section.*

- **Design:** A method paper on a public benchmark.
  - "Two-phase" means two **training** phases (instruction fine-tuning, then confidence-regularization fine-tuning), not a two-step inference pipeline.
  - Compared with published INCITE and DeBERTa systems and with vanilla Mistral Nemo few-shot ICL.
- **Language and documents:** English USMLE Step-2 Clinical Skills patient notes (NBME/Kaggle) covering 10 clinical cases. These are exam notes, not EHR.
- **Dataset size (Table 1):**
  - Training: 700 notes (100 in the few-shot setting).
  - Validation: 100.
  - Public test: 200 notes (2,860 features).
  - Private test: 1,839 notes (20,360 features).
- **Annotators and agreement:** 10 expert annotators working in pairs, from the corpus paper. F1 agreement 84%; binary detection 97%.
- **Output schema:** For each case-specific target feature, a text segment or Ø. Scored as present/absent.
- **Prompting:** One note per prompt, with the case's feature list, instructions and 4–6 exemplars.
- **Models:** Mistral-NeMo-Instruct-2407 (open-weight), fine-tuned on H100s. No other backbone tested.
- **Grounding:** An inference-time "matching gate" (regex/Levenshtein, TF-IDF, windowed overlap):
  - keeps only features found in the note and logs their character offsets;
  - then requires cosine similarity ≥0.5 to the target feature;
  - is applied to every model, including the vanilla baseline.
- **Intermediate representation:** None.
- **Compared with direct/single-step extraction:** Not applicable; every arm uses one call per note.
- **Key results:**
  - Full data, public split: F1 0.983 (semantic) / 0.968 (binary overlap).
  - 100 notes: 0.973 / 0.952 (Table 2).
  - Private split vs the vanilla model: hallucinated features 3,081→311; missing features 6,376→708.
- **Where it helps / where it does not:**
  - Omissions outnumber hallucinations (per-feature rates up to 23% vs 7%).
  - Compound "…-OR-…" features and non-standardized features are hardest.
  - Other errors come from gaps in the annotations and in domain knowledge.
- **Error propagation:** Not applicable.
- **Cost:** 200 notes in 30 min on one high-performance GPU. Training time not reported.
- **Calibration:** ECE worsened from 0.060 to 0.147 while the Brier score improved from 0.087 to 0.036.
- **Code and data:** https://github.com/manalS101/medical_feture_extraction. Data through Kaggle or an NBME agreement.
- **Author-stated limitations:**
  - inconsistent annotations;
  - gaps in medical logic;
  - exam notes only, no EHR;
  - calibration trade-off;
  - lenient semantic matching;
  - needs a predefined feature list;
  - untested parameter sensitivity;
  - one backbone.

**Citable claims**
- "Extracted features undergo a three-step validation process, referred to as the matching gate: (1) exact matching with regular expressions and Levenshtein distance for misspellings, (2) nonconsecutive and sentence-level matching using term frequency-inverse document frequency similarity and segment alignment, and (3) overlap and windowed matching for distributed features. This ensures that only text-supported features are validated, preventing hallucinations [42]." (§Methods › Evaluation Framework › Performance Evaluation)
- "To ensure fair comparison, this matching gate validation pipeline was applied consistently across all models during inference, including the vanilla baseline (Mistral Nemo with few-shot ICL), the instructing fine-tuned models, and the confidence-regularization fine-tuned models." (§Methods › Evaluation Framework › Performance Evaluation)
- "Our analysis shows that hallucination errors occur less frequently than missing feature errors, with the highest hallucination rates at 7%, while missing features showed an even higher occurrence, up to 23%." (§Results › Qualitative Error Analysis)
- "Predicting complex features proved consistently challenging for the model." (§Results › Qualitative Error Analysis › Missing Feature Error Patterns)
- "The semantic approach is inherently more lenient than token-based methods, which may introduce a positive bias." (§Discussion › Limitations)
- "Without predefined target features, the cosine similarity component cannot function, invalidating our current evaluation methodology." (§Discussion › Limitations)

*[Relevance]* This paper says little about arm C's architecture: there is no intermediate case model and no multi-call comparison. It is a precedent for arm C's evidence validation: a deterministic gate that requires each extracted value to be found in the source, applied equally to all arms. It also reports hallucinations and omissions separately.

---

### skeletonofthought2024 — Skeleton-of-Thought: plan first, then expand points in parallel

*Ning X, Lin Z, Zhou Z, Wang Z, Yang H, Wang Y. ICLR 2024 (poster; OpenReview mqVgBbNCm9); arXiv:2307.15337v3 (2 Mar 2024). No DOI. Text from arXiv v3 (header "Published as a conference paper at ICLR 2024"); cite "PDF p."; PDF pp. 17–51 are appendices.*

- **Design:** A prompting method for lower end-to-end latency, tested on 12 LLMs (§2.1, PDF p. 3).
  - **Skeleton stage:** one call returns 3–10 points of 3–5 words.
  - **Point-expanding stage:** one call per point, run as parallel API calls or one batched decode; the outputs are concatenated.
  - **SoT-R:** a router (a GPT-4 prompt, or a trained 120M RoBERTa) sends only suitable questions to SoT (§4).
- **Tasks and data:** Open-ended assistant questions, not IE: Vicuna-80 (80 questions, 9 categories); WizardLM (218) in the appendices (§3).
- **Intermediate representation:** The skeleton, a short numbered list in natural language. Each expansion call gets the question, the whole skeleton and its own point index (Prompt 2). Expansions never see each other's text.
- **Models:** 9 open LLaMA-based models (7B–33B) on one A100; Claude, ChatGPT-3.5, GPT-4 (App. A).
- **Compared with direct/single-step:** Yes, against the same model's normal sequential answer, judged pairwise by GPT-4 (FastChat and LLMZoo prompts).
- **Key results:**
  - Speed-up: >2× on 8 of 12 models, up to 2.39× (§3.1.1). Open-model latency is estimated from profiling tables; measured batch tests are in App. G.1.4.
  - Answer quality, SoT win/tie/lose: 29.5/29.3/41.2% (FastChat) and 45.8/19.6/34.5% (LLMZoo) (Fig. 3).
- **Where it helps / where it does not:**
  - Helps: generic, common-sense, knowledge, roleplay and counterfactual questions, whose points can be expanded independently.
  - Hurts: writing, fermi, math and coding (§3.2.3).
  - Diversity and relevance go up; coherence and immersion go down (§3.2.4).
  - SoT-R mostly recovers quality on the unsuitable categories (§4.3.2).
- **Error propagation:**
  - Points are expanded blind to each other. In math and fermi answers, later points contradict numbers or assumptions made in earlier points (App. I.1.2).
  - Weak models break the skeleton format (App. I.1.1).
- **Cost:**
  - Prefill tokens rise 60–89× over the normal answer for API models, and about 29–39× for open models (Tables 6–7, App. H).
  - Router overhead: 0.03–0.80 s on average (App. G.2).
- **Code:** https://github.com/imagination-research/sot (PDF p. 1).
- **Author-stated limitations** (§6):
  - GPT-4 judge only, no human evaluation;
  - dependencies between points ignored;
  - unpredictable speed-up;
  - token overhead under load.

**Citable claims**
- "The current SoT is suitable for questions that require a long answer whose structure can be planned ahead, while not suitable for questions that require step-by-step reasoning or only need a short answer." (PDF p. 2, §1)
- "On the other hand, it is fundamentally challenging to apply SoT on questions that require step-by-step thinking, in which the latter steps require the details from the earlier steps, such as math questions." (PDF p. 6, §3.2.3)
- "On average, we can see that SoT improves the diversity and relevance while hurting the immersion and coherence." (PDF p. 7, §3.2.4)
- "For instance, SoT currently ignores the dependencies between points. A conceptually better way is to organize the points as Graph-of-Thoughts, where the edges represent the dependencies, and each point is decoded conditioned on the contents of its ancestor points." (PDF p. 9, §6; italics markup removed)
- "In step 4, ChatGPT-3.5 does not know that it has already assumed 3.5 billion years in step 3 and uses the wrong number 4.54 billion in the calculation." (PDF p. 34, App. I.1.2, fermi example)
- "We can see that SoT significantly increases the number of prefilling tokens. This is because that SoT issues an independent point-expanding request for each point, with the average number of points being 6.8 on Vicuna-80 dataset across all evaluated models." (PDF p. 31, App. H; "because that" [sic])

*[Relevance]* This is the closest published analogue of arm C's structure: one call writes a shared plan, then parallel calls each receive the plan and fill in one part.
- **Upside:** the plan buys parallel speed and broader coverage when the parts are independent.
- **Failure mode:** when parts depend on each other (shared numbers or assumptions), the parallel calls contradict one another. Arm C is designed to prevent this by putting shared facts, such as the timeline, ICU stays and outcome, in the case model.

The skeleton is never checked against evidence.

---

### erman1980hearsay — The Hearsay-II speech-understanding system (origin of the blackboard)

*Erman LD, Hayes-Roth F, Lesser VR, Reddy DR. ACM Comput Surv 1980;12(2):213–253 (June 1980). doi:10.1145/356810.356816. The text is ACM's own OCR layer of the scanned PDF (free ACM backfile, retrieved through an Internet Archive capture); OCR errors are kept. Page refs: journal p. (PDF p.); journal p. = PDF p. + 212.*

- **Design:** A survey-style system paper on CMU's Hearsay-II (DARPA program, ended 1976), with comparisons to HWIM, SRI and HARPY (§§1–3).
- **Problem and domain:** Spoken queries for retrieving AI abstracts; 1,011-word vocabulary, context-free "semantic grammar" (p. 222 (PDF p. 10)).
- **Architecture:**
  - **Knowledge sources (KSs):** independent condition-action modules. The September 1976 configuration has 13 (Figs. 2–3, p. 219 (PDF p. 7)); about 40 were written over the project (p. 249 (PDF p. 37)).
  - **Blackboard:** a global database of hypotheses on levels (parameter, segment, syllable, word, word sequence, phrase, database interface). Each hypothesis has a time span, a credibility rating and links to the hypotheses that support it (pp. 218–220 (PDF pp. 6–8)).
  - **Control:** KSs are triggered by blackboard changes; a heuristic scheduler ranks pending actions from "stimulus" and "response" frames plus global state ("selective attention", focus of control) (p. 221 (PDF p. 9)).
- **Intermediate representation:** The multi-level hypothesis network itself. Partial results are shared, and changes propagate to every higher-level hypothesis that contains them (p. 245 (PDF p. 33)).
- **Error propagation:** Low-level credibility ratings were too unreliable for opportunistic search. MOW captured only about 75% of the words spoken, and the correct word ranked about 4.5th among about 20 competitors, so the low levels are processed in lock-step (§3.2, p. 240 (PDF p. 28)). Cheap approximate KSs (WORD-SEQ) make errors that fuller KSs (PARSE) correct later (§3.3, p. 241 (PDF p. 29)).
- **Key results:**
  - End of 1976: 9% semantic error and 19% sentence error on 23 new utterances, at 60 MIPSS on a PDP-10 (Table 2, p. 239 (PDF p. 27)).
  - Word error with opportunistic vs unordered scheduling: 29% vs 48%. Island-driving vs left-to-right search: 33% vs 53% (p. 240). The experiments are not directly comparable (fn. 13).
  - HARPY, a compiled network, beat Hearsay-II in both accuracy and speed on the same test data (p. 242 (PDF p. 30)).
- **Cost:** Deliberative scheduling is expensive, and routing a KS's internal steps through the blackboard failed or degraded performance (§4.3, p. 246 (PDF p. 34)).
- **Author-stated limitations** (§4.3): generality gets in the way of specialization; interpreted knowledge is slower than a compiled algorithm once one exists.

**Citable claims**
- "Because each KS is an _independent_ condition-action module, KSs communicate through a global database called the _blackboard._ The blackboard records the hypotheses generated by KSs." (p. 218 (PDF p. 6), §Hearsay-II Problem-Solving Model; OCR text)
- "The blackboard is subdivided into a set of information levels corresponding to the intermediate representation levels of the decoding processes (phrase, word, syllable, etc.)." (p. 218 (PDF p. 6), same section; OCR text)
- "In short, control of KS activation is determined by the blackboard actions of other KSs, rather than explicit calls from other KSs or some central sequencing mechanism." (p. 220 (PDF p. 8), same section; OCR text)
- "We found, however, that opportunistic processing at the lower levels was ineffective and harmful because the credibility ratings of hypotheses were insufficiently accurate to form hypothesis islands capable of focusing the search effectively." (p. 240 (PDF p. 28), §3.2 Opportunistic Scheduling; OCR text)
- "The blackboard and hypothesis structures allow the knowledge sources to represent and share partial results." (p. 244 (PDF p. 32), §4.2 Shared Partial Solutions; OCR text)
- "Attempts to coerce these specialized activities into the general blackboard-mediated style of Hearsay-II either failed completely or caused intolerable performance degradation [LEss77b]." (p. 246 (PDF p. 34), §4.3; OCR text, citation key as in the OCR)

*[Relevance]* Arm C's shared case model descends from this blackboard. It is one explicit, evidence-linked intermediate structure that independent specialists, the 18 variable-group calls, all read. The analogy breaks on control and write access. Arm C writes the model once; the readers cannot revise it; there is no scheduler, no credibility-driven focus and no incremental build-up. Hearsay-II's own finding that unreliable low-level hypotheses mislead the search is the classic warning for arm C: an error in the case model reaches all 18 calls.

---

### nii1986blackboard — The blackboard model of problem solving (Part One)

*Nii HP. The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures. AI Magazine 1986;7(2):38–53 (Summer 1986), printed under the label "PART ONE". doi:10.1609/aimag.v7i2.537. The text is OCR (Apple Vision) of the scanned AAAI OJS PDF, with printed line breaks and hyphenation kept. Page refs: journal p. (PDF p.); journal p. = PDF p. + 37.*

- **Design:** A conceptual and historical review. It defines the blackboard model, extends it into a "blackboard framework" (design guidelines for serial computers), and traces its history from Newell (1962) to HEARSAY and HASP. Part 2 covers specific systems (Abstract, p. 38 (PDF p. 1)).
- **Problem and domain:** Domain-independent. It is illustrated with a jigsaw-puzzle analogy and a koala-spotting example (pp. 40–42 (PDF pp. 3–5)); the historical cases are speech (HEARSAY) and passive-sonar interpretation (HASP).
- **Architecture:**
  - **Knowledge sources:** separate, independent and self-selecting, each with a precondition and a body. They are the only components that modify the blackboard (p. 43 (PDF p. 6)).
  - **Blackboard:** a global database of solution-space objects (input data, partial solutions, alternatives, final solutions) on levels. Each level has its own vocabulary, with attribute–value properties and named links such as "part-of" or "in-support-of"; the blackboard may have several panels (p. 43).
  - **Control:** the model itself specifies none (fn. 6, p. 39 (PDF p. 2)). The framework adds control modules that choose a focus of attention (a KS, a blackboard object, or both) one step at a time, plus a stopping criterion (p. 44 (PDF p. 7)).
- **Intermediate representation:**
  - The koala example frames the solution as bits of information backed by evidence and lines of reasoning (p. 42 (PDF p. 5)).
  - HASP kept one global "Current Best Hypothesis" (CBH), updated every time frame, whose network of evidential support also served as the explanation (pp. 50–52 (PDF pp. 13–15)).
- **Error propagation:** Lessons from HEARSAY-I:
  - without feedback in a part-of hierarchy, low-level errors grew multiplicatively on the way up (p. 47 (PDF p. 10));
  - a blackboard holding only the word level forced each KS to recompute non-word information (p. 48 (PDF p. 11)).
- **Key claims:**
  - Divide the problem into "loosely coupled subtasks" that match areas of specialization. How the problem is partitioned affects clarity, speed, resources and even whether it can be solved (Summary, pp. 45–46 (PDF pp. 8–9)).
  - The model is conceptual, not a computational specification (p. 39).
- **Limitations:** No empirical evaluation, and no agreed-upon architecture (pp. 52–53).

**Citable claims**
- "The blackboard model of problem solving is a highly structured special case of opportunistic problem solving." (p. 39 (PDF p. 2), §Blackboard Model of Problem Solving; OCR text)
- "Communication and interaction among the knowledge sources take place solely through the blackboard." (p. 39 (PDF p. 2), §The Blackboard Model; OCR text, hyphenated "knowl-edge" in the scan)
- "The important characteristics of the solution are that the solution consists of bits and pieces of information, and it is a reasoned solution with supporting evidence and supporting lines of reasoning." (p. 42 (PDF p. 5), koala example; OCR text)
- "The knowledge sources modify only the blackboard or control data structures (that also might be on the blackboard), and only the knowledge sources modify the blackboard. All modifications to the solution state are explicit and visible." (p. 43 (PDF p. 6), §The Blackboard Framework; OCR text)
- "that because of the lack of feedback in a simple part-of hierarchical structure, the magnitude of errors on the lower level propagated multiplicatively up the hierarchy; that is; minor errors in the signal level, for example, became major errors on a sentence level." (p. 47 (PDF p. 10), §The HEARSAY Project, summarizing Reddy et al. 1973; OCR text; "that is;" [sic, OCR: the scan prints "that is,"])
- "CBH was thought of as a cognitive "flywheel" that maintained the continuous activities in a region of ocean between time frames." (p. 50 (PDF p. 13), §The HASP Project; OCR text)

*[Relevance]* Nii gives the vocabulary for arm C. The case model is a blackboard-like solution state organized in levels with evidence links, and the 18 variable-group calls act as knowledge sources that interact only through it. Arm C departs from the model where Nii locates its power. There is no opportunistic, incremental control loop, the group calls cannot write back, and one call produces the "blackboard" in one pass. That is closer to HASP's CBH, rewritten once per time frame, than to HEARSAY-II. Nii's warning about partitioning applies directly to how the 199 variables are grouped.

---

### blackboardllm2025 — LLM multi-agent blackboard for data discovery

*Salemi A, Parmar M, Goyal P, Song Y, Yoon J, Zamani H, Pfister T, Palangi H. arXiv:2510.01285v2 [cs.MA] (v1 30 Sep 2025; v2 31 Jan 2026; PDF dated 2026-2-3). Preprint only: OpenReview lists it as a rejected ICLR 2026 submission, and no peer-reviewed version was found. The PDF has 44 pages including appendices; cite "PDF p."*

- **Design:** A multi-agent architecture for data-science questions whose files must first be found in a data lake (§3–4).
- **Tasks and data** (Table 3, App. A):
  - KramaBench: 104 tasks in 6 domains, with 5–1,556 files per domain.
  - DSBench (253 tasks, 48 files) and DA-Code (91 tasks, 145 files), repurposed and manually filtered.
- **Method** (§3; footnote 2):
  - **Clustering:** Gemini-2.5-Pro groups the files by filename; each cluster gets a file agent. A web search agent is added.
  - **Main agent:** runs a ReAct loop of at most 10 actions (plan, reason, run code, request help, answer). A help request is posted to the blackboard without naming any agent, and each helper decides for itself whether to answer.
  - **Responses:** go to a separate response board that only the main agent reads.
- **Intermediate representation:** The blackboard holds the main agent's requests, not a shared solution state. Helpers' responses are hidden from the other helpers.
- **Models:** Gemini 2.5 Pro and Flash and Claude 4 Opus (Vertex AI); Qwen3-Coder-30B-A3B (vLLM, 2×A100).
  - Temperature 0.1 "for more deterministic inference" (§4.1).
  - Single runs; no run-to-run variance reported.
- **Compared with direct/single-step:** Yes:
  - DS-GRU (all files in one prompt);
  - RAG over the top-5 files;
  - master–slave, where the main agent calls sub-agents by name;
  - Data Interpreter and AutoGen, on KramaBench only.
- **Key results:**
  - **End-to-end success, macro average vs best baseline** (Table 1): Gemini Pro 28.53% vs 24.01%; Claude 31.43% vs 27.63%; Qwen 7.90% vs 5.03%. The authors report "13%–57%" relative improvement.
  - **File-discovery F1** (Gemini Pro): 0.561 vs 0.513 for master–slave (Table 2).
  - The relative gain grows with data-lake size (App. F, Fig. 20).
- **Where it helps / where it does not:**
  - Largest gains on the largest data lakes: Astronomy +211%, DA-Code +70%.
  - Not uniformly best. Master–slave has higher discovery F1 on KramaBench Legal and Wildfire. RAG beats it on DA-Code with Gemini Flash (2.75% vs 0.55%) (Tables 1–2).
- **Cost** (50 KramaBench questions, §4.2): Runtime is similar across methods (132.0–145.2 s) because sub-agents run in parallel. Cost per question is about 2.3× that of RAG and 1.8× that of master–slave.
- **Code:** Not reported.
- **Author-stated limitations:** No limitations section.

**Citable claims**
- "Conversely, in the blackboard architecture, there is no task assignment; instead, requests are broadcast on a blackboard, and each agent retains full autonomy whether to participate in the task or not." (PDF p. 3, §1; italics markup removed)
- "Responses aren’t written to board β to prevent cross-influence of sub-agents; instead, they are written to a board βr, enabling independent operation and exclusive access by the main agent." (PDF p. 4, §3, footnote 2; β and βr are math symbols in the PDF, subscript r flattened)
- "Unlike RAG and Master–Slave, which execute their component calls sequentially following the ReAct framework, the Blackboard architecture parallelizes sub-agent interactions: once the main agent posts a request to the shared blackboard, the corresponding sub-agents process it independently." (PDF p. 10, §4.2, Runtime and Cost Analysis)
- "In terms of monetary cost, Blackboard is more expensive per question (approximately 2.3× the cost of RAG and 1.8× that of Master–Slave), due to increased token usage." (PDF p. 10, §4.2; the converted text splits "2.3" as "2 _._ 3")
- "We use nucleus sampling (Holtzman et al., 2020) with a temperature of 0.1 for more deterministic inference and default value for other hyperparameters." (PDF p. 7, §4.1; same conversion artifact in "0.1")

*[Relevance]* This is a shared blackboard read by independent agents, but in one respect it is the opposite of arm C.
- **Here:** the blackboard carries requests, and responses are kept apart on purpose "to prevent cross-influence".
- **Arm C:** broadcasts a validated case model to all 18 calls.

It supports parallel data-owning specialists (flat latency, about 2× the tokens), but gives no evidence on injecting a shared, pre-validated case model.

---

### blackboardmas2025 — LbMAS: blackboard-based LLM multi-agent system

*Han B, Zhang S. arXiv:2507.01701v1 [cs.MA], 2 Jul 2025 (preprint; no venue found as of 2026-09-24). The PDF has 15 pages including appendices; cite "PDF p."*

- **Design:** A general framework (bMAS) and one implementation (LbMAS), tested on six QA and reasoning benchmarks (§3–4).
- **Tasks and data:** MMLU (1,140 sampled questions), ARC-Challenge, GPQA-Diamond, BBH date-understanding, MATH-500 and GSM8K (Table 6). There is no information-extraction task.
- **Method** (§3.2):
  - **Agents:** an agent-generation step creates 1–3 expert roles specific to the question. Five agents are fixed: planner, critic, conflict-resolver, cleaner and decider.
  - **Each round:** an LLM control unit reads the blackboard and chooses which agents act. The chosen agents read the whole public blackboard and append messages.
  - **Debate:** agents in conflict debate in a private space.
  - **Stopping:** the decider answers, or after 4 rounds the most mutually similar answer is chosen.
- **Intermediate representation:** The blackboard is the only shared memory (agents have no own memory). It accumulates plans, partial solutions and critiques; the cleaner deletes redundant messages.
- **Models:** Llama-3.1-70B-Instruct and Qwen2.5-72B-Instruct, one drawn at random for each new agent. Accessed via API at temperature 0.7 (§4.1). Single runs; no seeds or variance reported.
- **Compared with direct/single-step:** Yes:
  - vanilla and CoT single calls;
  - majority vote;
  - static multi-agent systems: MultiPersona, Exchange-of-Thought, ChatEval;
  - autonomous multi-agent systems (GPTSwarm, AFlow, MaAS), on MATH only.
- **Key results:**
  - Average accuracy: LbMAS 81.68 vs CoT-Qwen 80.09 and ChatEval 80.56 (Table 1).
  - CoT-Qwen beats LbMAS on MATH (76.4 vs 72.8). With Llama as the only base model, LbMAS falls below CoT on both MATH and GSM8K (Table 2).
  - Full agreement among agents: 89.8% of questions in MMLU, 52.5% in GPQA, 29.4% in MATH (§4.2).
- **Error propagation / validation:** The critic flags wrong messages, and the conflict-resolver triggers a debate. Their effect is not ablated. Having the cleaner only mark redundant messages, instead of removing them, lowers accuracy on all three datasets tested (Table 5).
- **Cost:**
  - Total tokens on MATH: 4.72M, vs 2.17M for MultiPersona and 5.45M for ChatEval (Table 3).
  - Without the control unit (agents self-select), accuracy is similar but tokens rise about 3–4.5× (Table 5).
- **Code:** "Code will be released soon"; no URL is given (PDF p. 1).
- **Author-stated limitations** (PDF p. 9): few agent types; limited benchmarks; simple agent generation; blackboard not compared with per-agent memory.

**Citable claims**
- "Unlike MetaGPT (Hong et al., 2024) that uses a shared memory pool as an assistant for knowledge storage, in LbMAS agents communicate solely through the blackboard without any direct contact; in other words the blackboard is responsible for all agent communication and agents decide on their own what to write on the blackboard." (PDF p. 4, §3.2, Blackboard)
- "The critic agent points out errors in messages on the blackboard, which may come from hallucinations of LLMs, and forces relevant agents to rethink their output." (PDF p. 4, §3.2, Agent group)
- "The cleaning is necessary as effective management of content of the blackboard can facilitate meaningful communication among agents and at the same time reduce token consumption." (PDF p. 4, §3.2, Agent group)
- "The results in Table 5 show that the control unit can significantly reduce the token cost of LbMAS with a slight turbulence in performance." (PDF p. 7, §5, Ablation study)
- "Thirdly, exploration of the blackboard is not adequate. Comparative experiments should be conducted to explore the differences between shared memory pool and agent memory module, as memory of LLM agent is the key component to support agent-environment interactions (Zhang et al., 2024b)." (PDF p. 9, Limitations)

*[Relevance]* This paper reads the blackboard as shared memory: every agent reads the whole shared state before acting. That makes it closer to arm C's injected case model than blackboardllm2025. Its limits for arm C:
- Its evidence is on token efficiency and QA/math accuracy, not extraction.
- The shared state is never checked against source evidence.
- Single runs at temperature 0.7, with the base model assigned at random, leave run-to-run variability unmeasured.

---

### hisccg2026 — Hi-SCCG: hierarchical path-aware context for chunked document-level IE

*Tian P, Xie P, Li Q, Gu J. Sci Rep 2026, Article in Press (unedited manuscript), published online 22 Sep 2026; doi:10.1038/s41598-026-58930-z; no volume or article number yet. Received 1 Feb 2026, accepted 17 Jun 2026. Cite "PDF p." of the unedited PDF (29 pp.); equations and some captions are garbled in the conversion (L = 600 for Tables 7 and 13 was checked on the rendered PDF).*

- **Design:** A method paper plus a benchmark (Fig. 2, PDF p. 6), in three phases:
  - MinerU layout parsing and LLM heading-level correction build a semantic tree with chunks as leaves.
  - Entity-preserving section summaries are generated once, bottom-up, and cached.
  - Path-aware injection at extraction time.
  
  All methods share the same parser, chunk limit (L ∈ {600, 1200}), KGGen extractor and prompt.
- **Language and documents:** Chinese medical guidelines (30) and technical standards (30), mean 37–45K tokens; supplementary Legal-OOD-60 (10 legal documents).
- **Dataset size:** LDE-500 has 500 chunks (250 high- and 250 low-dependency) and 2,864 gold triples, of which 1,222 (42.7%) need subject restoration.
- **Annotators and agreement:** LDE-500 gold labels are LLM pseudo-labels generated with the full hierarchical path. A 50-chunk manual audit gives F1 0.94; no IAA. Legal-OOD-60 is fully manual; annotator count not reported.
- **Output schema:** (head, relation, tail) triples.
- **Intermediate representation:** Injected into **every** chunk's extraction call. The root summary plus the most recent ancestors (K_max = 3, ≤150 Chinese characters each) are prepended as Global Context / Section Context / Current Text (PDF pp. 5, 9, 15).
- **Models:** Qwen3 (size not reported); temperature 1.0 for context generation and extraction.
- **Key results (L = 600, Table 7):**
  - F1 0.82 vs SLIDE 0.75, Doc-Global Summary 0.71, fixed-size 0.50.
  - SRR 82.1% vs 72.7/68.1/45.2%.
  - High-dependency SRR 79.0% (+11.0 pp over SLIDE).
  - Three runs: F1 SD 0.002.
  - Legal: F1 0.77 vs 0.70.
- **Where it helps / where it does not:** The gain is largest on high-dependency chunks, and F1 is still the highest on low-dependency ones. One static document summary prepended to every chunk scores below local sliding context (0.71 vs 0.75).
- **Error propagation (ablation, high-dependency subset, Table 13):** F1/SRR are 0.80/79.0% for the full method.
  - Without heading correction: 0.45/41.2%. The wrong tree turns context into "misleading evidence".
  - Titles instead of summaries: 0.60/58.7%.
  - Parent summary only: 0.71/71.5%.
- **Cost (45K-token document, Table 12):** 144K tokens in total (54K one-time build) vs SLIDE 585K and Doc-Global 162K.
- **Code and data:** Data on request; code not reported.
- **Author-stated limitations:** relies on explicit hierarchy; lossy fixed-length summaries; LLM pseudo-labels; Qwen3 both answers and judges in QA; small legal set; savings depend on reuse.

**Citable claims**
- "Its central operation is _path-aware injection_ : for each chunk to be extracted, the method deterministically retrieves the chunk’s ancestral summaries from the reconstructed document tree and prepends them to the local text." (PDF p. 5, §Augmenting context and document structure; "injection_ :" spacing as converted)
- "Doc-Global Summary adds document-level information, but its static summary is not tailored to each local predicate and can introduce irrelevant context." (PDF p. 19, §Fine-grained extraction performance)
- "Compared with the strongest context-enhanced baseline, SLIDE, Hi-SCCG improves SRR by 9.4 percentage points and Subset P by 0.09." (PDF p. 19, same section)
- "Relying on raw layout parsing can introduce structural noise, leading to chunks being attached to incorrect branches and turning the injected context into misleading evidence." (PDF p. 24, §Ablation study)
- "While our heading correction module mitigates noise, errors in initial layout parsing or semantic tree construction can still propagate downstream, leading to context misalignment." (PDF p. 25, Limitations)
- "Additionally, to maintain low token overhead, our recursive summarization functions as lossy compression, which may occasionally filter out subtle qualifiers required for complex reasoning." (PDF p. 26, Limitations)

*[Relevance]* This is the most direct evidence for arm C's mechanism. Shared, precomputed context injected into every parallel extraction call beats both no context and a static global summary, at modest token cost. The ablation, however, shows that a wrong shared structure is worse than none, which argues for validating the case model. Caveat: Chinese guidelines, triples rather than clinical variables, LLM pseudo-gold.

---

### trialgpt2024 — TrialGPT: matching patients to clinical trials with LLMs

*Jin Q, Wang Z, Floudas CS, Chen F, Gong C, Bracken-Clarke D, Xue E, Yang Y, Sun J, Lu Z. Nat Commun 2024;15:9074. doi:10.1038/s41467-024-53081-z; PMID 39557832; PMC11574183. Received 18 Jan 2024, accepted 1 Oct 2024. PDF page = article page.*

- **Design:** Three modules (p. 2):
  - **Retrieval:** LLM keywords feed a BM25 + MedCPT hybrid retriever with reciprocal rank fusion.
  - **Matching:** criterion-level explanation, evidence and label.
  - **Ranking:** linear or LLM aggregation of criterion labels into trial scores.
  
  Compared with NLI-trained encoder baselines, plus a pilot user study.
- **Language and documents:** English synthetic patient summaries (SIGIR 2016, TREC CT 2021/2022), mean 89–156 words; ClinicalTrials.gov criteria.
- **Dataset size:** 183 patients, >75,000 trial annotations. Manual evaluation: 1,015 patient–criterion pairs from 105 patient–trial pairs.
- **Annotators and agreement:** Three physicians, with majority consensus (sentence evidence = union). No κ; individual experts score 0.887–0.900 against the consensus (p. 4).
- **Intermediate representation:** The note is split into numbered sentences. Per criterion, the output is JSON with a free-text explanation, **relevant sentence IDs** and a 4-way label ({Included, Not included, Not enough information, Not applicable} or the exclusion analogue) (pp. 3, 10).
- **Prompting:** Two calls per patient–trial pair: all inclusion criteria, then all exclusion criteria. The explanation is generated first, then the IDs and the label. An optional further LLM call aggregates into relevance (0–100) and eligibility (−100 to 100) (p. 10).
- **Models:** GPT-4 and GPT-3.5 (0613, Azure), temperature 0.
- **Grounding (evaluated):**
  - Sentence locations: P 90.1%, R 87.9%, F1 88.6% on 405 criteria, vs 86.9–91.5% for the experts.
  - Explanations: 87.8% correct, 2.56% incorrect (pp. 3–4).
- **Key results:**
  - Criterion accuracy 0.873 (inclusion 0.899, exclusion 0.859).
  - Ranking: NDCG@10 0.7275, exclusion AUROC 0.7979; mean 0.7314 vs 0.5085 for the best baseline (+43.8%).
  - 90% retrieval recall using 5.5% of trials.
  - Screening time −42.6% (36 pairs).
- **Where it helps / where it does not:** Errors cluster in "not included"/"not excluded" cases needing implicit inference, and in confusion between "no info" and "not applicable". Of the 26 errors: reasoning 30.7%, label ambiguity 26.9%, medical knowledge 15.4%.
- **Compared with direct/single-step extraction:** No direct trial-level LLM baseline; LLM aggregation beat linear aggregation (Table 2).
- **Error propagation:** Not analysed.
- **Cost:** Not reported.
- **Code and data:** https://github.com/ncbi-nlp/TrialGPT; criterion annotations at https://huggingface.co/datasets/ncbi/TrialGPT-Criterion-Annotations.
- **Author-stated limitations:**
  - closed GPT backbone;
  - other prompting strategies unexplored;
  - small user study;
  - short free-text summaries only.

**Citable claims**
- "For each criterion, TrialGPT-Matching generates three elements: (1) the explanation of the patient-criterion relevance; (2) the locations of relevant sentences in the patient notes to the criterion; (3) the eligibility classification for the patientcriterion pair." (p. 2, §TrialGPT architecture; "patientcriterion" as converted)
- "As shown in Fig. 3b, the TrialGPT-predicted sentence locations are 90.1% correct (precision) and cover 87.9% of the ground-truth relevant sentence IDs (recall), leading to an F1 score of 88.6%." (p. 4, §TrialGPT-Matching achieves a high criterion-level prediction accuracy)
- "Overall, TrialGPT-Matching achieves a prediction accuracy of 0.873, close to the expert performance (0.887–0.900)." (p. 4, same section)
- "We make two LLM inference calls for each patient-trial pair: one for all inclusion criteria, and another one for all exclusion criteria." (p. 10, Methods › TrialGPT-matching)
- "We set the inference temperature to 0 for deterministic outputs." (p. 9, Methods › TrialGPT; determinism is assumed, not tested)
- "Our work does not justify the position that clinical trial matching should be fully automatic and exclude human recruiters." (p. 9, Discussion)

*[Relevance]* This is a template for arm C's evidence discipline. Each decision cites sentence IDs, and those citations were checked against experts (F1 88.6%). Per-criterion decisions are aggregated into a patient-level judgement, much like variable-group calls feeding a case record. Caveats: the notes are short and synthetic, and the paper assumes temperature 0 is deterministic.

---

### thinkingmachines2025nondeterminism — Defeating Nondeterminism in LLM Inference (grey literature)

*He H, Thinking Machines Lab. Defeating Nondeterminism in LLM Inference. Thinking Machines Lab: Connectionism (research blog), 10 Sep 2025. doi:10.64434/tml.20250910 (Crossref, type "report"). **Grey literature: a technical blog post, not peer-reviewed.** Byline: "Horace He in collaboration with others at Thinking Machines". The page was last modified 2026-08-31; the text was captured from HTML on 2026-09-24. Cite by section heading.*

- **Design:** An explanatory technical essay with code snippets and three small demonstrations. No statistical analysis.
- **Setting:**
  - Implementation: vLLM with its FlexAttention backend; batch-invariant PyTorch operators are swapped in through torch.Library (§Implementation).
  - Demo 1: Qwen3-235B-A22B-Instruct-2507, 1,000 completions at temperature 0 of 1,000 tokens each, for one prompt.
  - Demo 2: throughput with Qwen-3-8B on one GPU (model of GPU not stated), 1,000 sequences of 90–110 output tokens.
  - Demo 3: RLVR on Bigmath from Qwen 2.5-VL instruct 8B (§Experiments).
- **Nondeterminism findings:** Default vLLM produced 80 distinct completions out of 1,000 (the most common appeared 78 times). All were identical for the first 102 tokens. With batch-invariant kernels all 1,000 were identical.
- **Root cause:**
  - Floating-point non-associativity is the "original sin", but the LLM forward pass has no atomic adds and is run-to-run deterministic.
  - What a user sees as nondeterminism comes from kernels that are not **batch-invariant**: the reduction strategy changes with batch size (split reductions, split-K matmul, choice of tensor-core instruction, Split-KV/FlashDecoding). Server load, and therefore batch size, varies between requests.
  - Chunked prefill and prefix caching also change how a request is sliced.
  - The same applies to CPU and TPU endpoints (§Batch invariance and "determinism").
- **Mitigation:** Fix each element's reduction order regardless of batch size:
  - data-parallel RMSNorm;
  - one matmul kernel configuration for all shapes;
  - updating the KV cache and page table before attention;
  - a "fixed split-size" Split-KV.
- **Code:** https://github.com/thinking-machines-lab/batch_invariant_ops. A sidenote says some FlexAttention changes are not in the release.
- **Cost:**
  - The batch-invariant matmul loses about 20% against cuBLAS (figure caption, §Batch-invariant matrix multiplication).
  - End to end: 26 s for default vLLM, 55 s for unoptimized deterministic vLLM, 42 s with an improved attention kernel (§Performance).
- **Error propagation:** One divergent token (the 103rd: "Queens, New York" vs "New York City") changes everything that follows.
- **Limitations:**
  - one prompt;
  - no repeated-measures statistics;
  - hardware not specified;
  - kernels not tuned for performance;
  - not peer-reviewed.

**Citable claims**
- "Even when running inference on your own hardware with an OSS inference library like vLLM or SGLang, sampling still isn’t deterministic" (Introduction; the sentence continues with links to the vLLM and SGLang FAQs)
- "In other words, **the primary reason nearly all LLM inference endpoints are nondeterministic is that the load (and thus batch-size) nondeterministically varies!**" (§Batch invariance and "determinism")
- "Thus, to achieve determinism in LLM inference our numerics must be invariant to both how many requests are processed at once **and** how each request gets sliced up in the inference engine." (§Batch-invariant attention)
- "Surprisingly, we generate _80_ unique completions, with the most common of these occuring 78 times." (§Experiments › How nondeterministic are completions?; "occuring" [sic])
- "On the other hand, when we enable our batch-invariant kernels, all of our 1000 completions are identical." (§Experiments › How nondeterministic are completions?)
- "Much of the slowdown comes from the fact that the FlexAttention integration in vLLM has not been heavily optimized yet. Nevertheless, we see that performance is not _disastrous_." (§Experiments › Performance)

*[Relevance]* This is the mechanism to cite for running the three arms on vLLM. Under continuous batching, an epicrisis' output depends on what else is in the batch, so temperature 0 does not make runs reproducible. Arms B and C send 18–19 concurrent requests per case, so their batches differ from arm A's single call, and run-to-run variance may differ by arm. It has to be measured with repeated runs, or removed with batch-invariant kernels (42 s vs 26 s in their demo). Arm C adds a sequential dependency: a divergent case model changes all 18 downstream calls.

---

### atil2024nondeterminism — Non-determinism of "deterministic" hosted LLM settings

*Atıl B, Aykent S, Chittams A, Fu L, Passonneau RJ, Radcliffe E, Rajagopal GR, Sloan A, Tudrej T, Ture F, Wu Z, Xu L, Baldwin B. Non-Determinism of "Deterministic" LLM System Settings in Hosted Environments. Proceedings of the 5th Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP 2025), Mumbai, Dec 2025, pp. 135–148. doi:10.18653/v1/2025.eval4nlp-1.12. Preprint: arXiv:2408.04667 (v4–v5 titled 'Non-Determinism of "Deterministic" LLM Settings'; v1–v3 titled "LLM Stability: A detailed analysis with some surprises"). Page refs: proceedings p. (PDF p.); proceedings p. = PDF p. + 134.*

- **Design:** An empirical study of run-to-run variability in hosted LLM APIs under settings expected to be deterministic (§§3–6).
- **Setting (§4.2, §5, p. 137–138 (PDF pp. 3–4)):**
  - Five models: GPT-3.5 Turbo and GPT-4o (OpenAI API); Llama-3-70B-Instruct, Llama-3-8B-Instruct and Mixtral-8x7B-Instruct (Together API).
  - Temperature 0, top-p 1, fixed seed. Zero-shot and few-shot (3-shot BBH, 5-shot MMLU), without chain-of-thought.
  - Eight multiple-choice tasks, 4 from BBH and 4 from MMLU, with 100–282 items each.
  - 80 conditions × 10 runs, run in February 2025, plus a 20-run check on college math.
- **Metrics (§4.3, pp. 137–138):**
  - TARr@N: the share of items whose raw outputs are identical across N runs.
  - TARa@N: the same for the parsed answers.
  - BestAcc, WorstAcc, the max–min accuracy difference, and median accuracy.
  - No means or SDs are reported, because the run distributions are non-normal (Kolmogorov–Smirnov p < 10⁻⁹).
- **Nondeterminism findings:**
  - Max–min accuracy differences reach 5–15% on some tasks.
  - The gap between best and worst possible accuracy reaches 72 points (Mixtral on college math, 75 vs 3) (Table 2, p. 139 (PDF p. 5); §7, p. 141 (PDF p. 7)).
  - TARr@10 is often near zero (e.g. GPT-4o scores 0.0 on geometric shapes, ruin names and college math); TARa@10 is higher but well below 100 (Table 2).
  - Instability rises with output length. In the few-shot setting it falls as accuracy rises (§6.2, p. 139).
- **Root cause:** Not established. The authors speculate about serving optimizations: continuous batching, chunked prefill, prefix caching, and "input buffer packing across multiple jobs". Llama-3-8B run locally on an A6000 with Hugging Face/PyTorch "without any optimization" was deterministic (§5; §7.1, p. 141).
- **Mitigation:**
  - cap the maximum number of generated tokens;
  - report max–min accuracy across runs;
  - a fine-tuned GPT-3.5 was less unstable, but no numbers are given (pp. 139–141).
- **Error propagation:** Changes in format break downstream parsers (§7.1).
- **Code:** https://github.com/breckbaldwin/llm-stability (Abstract).
- **Limitations:** Only 8 multiple-choice datasets and 5 systems (Limitations, p. 142 (PDF p. 8)); the answer parser is hard-coded (§7, p. 141).

**Citable claims**
- "We apply five API-based LLMs configured to be deterministic to eight diverse tasks across 10 runs. Experiments reveal accuracy variations of up to 15% across runs, with a gap of up to 70% between best possible performance and worst possible performance." (p. 135 (PDF p. 1), Abstract; the converted text reads "APIbased", a line-break artefact)
- "These correlations mean that as an LLM’s output length increases, the instability of the output increases, resulting in more diverse natural language responses as well as in the actual multiple choice answer prediction." (p. 139 (PDF p. 5), §6.2)
- "String variation does not affect a human reader much because we can extract the same answer even if the output format is different, but a downstream system that needs to parse the LLM response can be affected significantly when the format or pattern is different." (p. 140 (PDF p. 6), §7)
- "This instability lowers confidence in the reliability of reporting only a single number in LLM benchmarks. We encourage reporting maximum-minimum scores across runs to have a more robust comparison of LLM systems." (p. 141 (PDF p. 7), §7)
- "However, engineering optimizations to run LLMs faster, such as continuous batching, chunk prefilling, or prefix caching, might lead to non-deterministic behavior." (p. 141 (PDF p. 7), §7.1)
- "In order to support this line of reasoning, we ran Llama3-8b on our local GPUs without any optimizations, yielding deterministic results. This indicates that the models and GPUs themselves are not the source of non-determinism." (p. 141 (PDF p. 7), §7.1)

*[Relevance]* This is peer-reviewed evidence that temperature 0 is not reproducible on shared serving infrastructure, and that longer outputs are less stable. Arm A's monolithic 199-variable JSON is the longest output of the three arms. For a vLLM deployment it supports reporting variability over repeated runs (max–min accuracy, per-variable agreement) instead of a single run. Its deterministic local baseline ran without batching optimizations, unlike a vLLM server; the Thinking Machines post supplies the mechanism.

---

## Metadata corrections

Each entry compares the original request list with the verified record. Sources: Crossref (C), PubMed/E-utilities (P), PMC ID Converter (I), arXiv API (A), medRxiv API (M), ACL Anthology BibTeX (L).

| # | Key | Request list said | Verified | Status |
|---|---|---|---|---|
| 1 | agrawal2022fewshot | arXiv:2205.12689; also EMNLP 2022 | EMNLP 2022 main conference, pp. 1998–2022, doi:10.18653/v1/2022.emnlp-main.130, Anthology ID 2022.emnlp-main.130 (C, L). arXiv v2 (30 Nov 2022) comment: "Accepted as a long paper to … EMNLP" (A). Anthology title is sentence case; PDF title is title case. | Correct. Cite the EMNLP version; arXiv as eprint. |
| 2 | promptstotable2025 | "JMIR 2025?", PMID 39990557 | **Not JMIR.** PMID 39990557 is the **medRxiv preprint** doi:10.1101/2025.02.11.25322107 (PMC11844613; v1 13 Feb 2025, v2 1 Apr 2025) (P, I, M). Authors: Hein D, Christie A, Holcomb M, Xie B, Jain AJ, Vento J, Rakheja N, Hamza Shakur A, Christley S, Cowell LG, Brugarolas J, Jamieson AR, Kapur P. A Crossref title search returns only the medRxiv record. | **Wrong venue.** It is also the **preprint of #7** (same authors, data and results; see "Relationship" under #7). medRxiv lists `published: NA` and Crossref has no relation link, so the match rests on content. |
| 3 | privacy2024structured | npj Digit Med 2024, doi 10.1038/s41746-024-01233-2 | 7(1):257, published 20 Sep 2024; PMID 39304709; PMC11415382. First author Wiest IC; 12 authors (C, P). | Correct. Added volume, article number, PMID and authors. |
| 4 | scoping2024radiology | npj Digit Med 2024, doi 10.1038/s41746-024-01219-0 | 7(1):222, published 24 Aug 2024; PMID 39182008; PMC11344824. Authors Reichenpfader D, Müller H, Denecke K (C, P). | Correct. |
| 5 | fornasiere2024medical | ICNLSP 2024, aclanthology 2024.icnlsp-1.47 | Proceedings of the 7th ICNLSP, Trento, Oct 2024, pp. 456–466; editors Abbas M and Freihat AA; ACL (L). **No DOI.** Last author: "Mark Carman" in the Anthology, "Mark James Carman" in the PDF byline. | Correct. Minor author-name variant. |
| 6 | llmie2025 | JAMIA Open 2025;8(2):ooaf012 | doi:10.1093/jamiaopen/ooaf012; PMID 40078164; PMC11901043. Authors Hsu E, Roberts K. Online 12 Mar 2025; issue date Apr 2025 per PubMed (C, P). Official title has lowercase "python": "LLM-IE: a python package for…". | Correct. Title capitalization differs trivially. |
| 7 | iterativerefine2025 | npj Digit Med 2025, doi 10.1038/s41746-025-01686-z | 8(1):301, published 23 May 2025 (received 14 Feb 2025); PMID 40410408; PMC12102345; 13 authors (C, P). | Correct. The journal version of #2. |
| 8 | clinicalentityretrieval2024 | npj Digit Med **2024**, doi 10.1038/s41746-024-01377-1 | npj Digit Med **2025**;8(1):45, published online 19 Jan 2025 (received 1 Jul 2024, accepted 8 Dec 2024); PMID 39828800; PMC11743751. First author Lopez I; 12 authors (C, P). | **Year wrong: 2025**, not 2024; the DOI suffix contains "2024". The key is kept for compatibility; the .bib says `year = {2025}`. |
| 9 | spaanderman2025structured | arXiv:2511.10658 | v1 submitted 3 Nov 2025, cs.CL, 23 authors (A). No later arXiv version, and no journal version found by Crossref title search as of 2026-09-23. arXiv DOI 10.48550/arXiv.2511.10658 resolves. | Correct. It is a preprint (not peer-reviewed). |
| 10 | gallifant2025tripodllm | Nature Medicine 2025, PMID 39779929 | Nat Med 31(1):60–69; online 8 Jan 2025; doi:10.1038/s41591-024-03425-5; PMC12104976; 25 authors (C, P). | Correct. |
| 11 | collins2024tripodai | BMJ 2024;385:e078378 | doi:10.1136/bmj-2023-078378; PMID 38626948; PMC11019967; published 16 Apr 2024; 34 authors (C, P). | Correct. |
| 12 | liu2020consortai | BMJ 2020;370:m3164 (also Nat Med) | doi:10.1136/bmj.m3164; PMID 32909959; PMC7490784; published 9 Sep 2020. PubMed lists the group author "SPIRIT-AI and CONSORT-AI Working Group". Co-publications (C): Nat Med 2020;26(9):1364–1374, doi:10.1038/s41591-020-1034-x; Lancet Digit Health 2020;2(10):e537–e548, doi:10.1016/S2589-7500(20)30218-1. | Correct. TRIPOD-LLM (#10) cites the Nat Med version (its ref. 12). |
| 13 | rivera2020spiritai | BMJ 2020;370:m3210 | doi:10.1136/bmj.m3210; PMID 32907797; PMC7490785; published 9 Sep 2020. **First author's surname is "Cruz Rivera"** (Samantha Cruz Rivera); group author as in #12. Co-publications (C): Nat Med 2020;26(9):1351–1363, doi:10.1038/s41591-020-1037-7; Lancet Digit Health 2020;2(10):e549–e560, doi:10.1016/S2589-7500(20)30219-3. | Correct. The key "rivera" truncates the surname; the .bib uses `Cruz Rivera, Samantha`, so it renders as "Cruz Rivera S". |

### Other issues found inside the papers (not errors in the list)

Worth knowing before quoting numbers:
- **TRIPOD-LLM:**
  - The text says "19 main items … 50 subitems", but Table 2 has 49 numbered rows, and Fig. 1 says "59 reporting items".
  - The Methods list 8 task categories, but Table 1 has 9.
- **Spaanderman:**
  - Variable counts in Table A1 (4/12/25/9/16/7) differ from the prompt templates (4/13/22/9/15/7).
  - Model size range "1.5B–650B" vs DeepSeek R1 at 685B.
  - The abstract's statement about few-shot gains is inconsistent with §3.2.
- **Reichenpfader:**
  - "15 out of 35 papers" although 34 studies were included.
  - "up to 64" concepts vs 75 in Table 4.
  - External-validation counts differ (7, 6, 7).
- **CLEAR (Lopez):**
  - CheXpert train/test counts appear swapped (p. 5).
  - "2000 CheXpert notes" (p. 7) matches neither count.
  - The abstract's "20,000 clinical notes" cannot be reconciled with the dataset counts.
- **Wiest:** The abstract gives SOB specificity as 97%; the text and Table 1 give 0.96.
- **Hein (both versions):** The TFEB regex F1 is 0.35 in the text but 0.36 in the table. The preprint's GPT-4o version label is inconsistent; the npj version fixes it.
- **Fornasiere:** §6.1 interprets precision and recall the opposite way from the standard definitions.

## Provenance and verification

- **PDFs** (`pdf/`):
  - 10 papers: ACL Anthology (2), arXiv (1), nature.com (5), medRxiv v1 (1), and UCL Discovery (1; the BMJ publisher PDF of TRIPOD+AI).
  - No PDF for llmie2025, liu2020consortai or rivera2020spiritai. Every source (academic.oup.com, bmj.com, PMC and the Europe PMC render endpoints) returned a Cloudflare challenge page. Their text comes from the Europe PMC REST full-text JATS XML.
- **Conversion:**
  - PDFs were converted with pymupdf4llm 1.28.2 (venv in `.venv/`, Python 3.14). That version keeps table cells; the older 0.0.27 dropped them.
  - JATS XML was converted with a small custom script. Figures are captioned only, as "[figure image not converted]".
- **Quote check:** Each "Citable claims" quote was verified against `md/<key>.md` by an automated substring check (the script is not included in this folder). All 71 quotes and all 61 TRIPOD-LLM checklist rows (49 main, 12 abstract) were found in the text.
  - The check normalizes Unicode quotes and dashes, markdown emphasis and whitespace.
  - When the PDF conversion dropped spaces between words, the check falls back to comparing letters and digits only. Such quotes are marked LOOSE in the script output, and each was inspected.
- **Not verifiable from the texts:** any number that sits only in supplementary files that were not downloaded. Examples: TRIPOD-LLM Supplementary Tables 1–3; CLEAR Supplementary Table 12; Hein Supplementary Tables.

## Metadata corrections (batch 2)

Batch 2 (#14–#27) was added on 2026-09-24. Each entry compares the request list with the verified record. Sources: Crossref (C), PubMed/E-utilities (P), PMC ID Converter (I), arXiv API and abs pages (A), ACL Anthology BibTeX (L), OpenReview API (O), OpenAlex (X), doi.org resolution (D), publisher or landing page (W).

| # | Key | Request list said | Verified | Status |
|---|---|---|---|---|
| 14 | psych2stage2026 | JMIR Formative Research, doi 10.2196/94454, PMC13446380 | JMIR Form Res 2026;10:e94454, published 6 Aug 2026; PMID 42560822; PMC13446380; 9 authors, first author Chen CH, last Chen HH (C, P, I). Crossref gives article number "v10i6e94454", PubMed PII "v10i1e94454". | Correct. Added volume, article number, PMID and authors. |
| 15 | clinicirca2026 | Title as listed; arXiv 2609.19585 | Title identical. v1 only, 17 Sep 2026, cs.CL; 8 authors (A). No journal_ref or comment; no venue in OpenAlex or Semantic Scholar (X). | Correct. A preprint, posted one week before this check. |
| 16 | promptplanextract2026 | Title as listed; arXiv 2606.19852 | cs.CL; v1 18 Jun 2026, v2 25 Jun 2026, same title; the text is v2; 11 authors (A). No venue found (X). | Correct. A preprint. |
| 17 | cancerregistrymas2026 | BioNLP 2026, aclanthology 2026.bionlp-1.43 | Proceedings of the 25th Workshop on Biomedical Language Processing (BioNLP 2026), San Diego, July 2026, pp. 531–551, doi:10.18653/v1/2026.bionlp-1.43; editors Demner-Fushman, Ananiadou, Roberts, Tsujii (L, C). **Author order:** the Anthology and Crossref give Aal Abdulsalam A, Al Zaabi A, Jeeballah R, El Keraby H. The PDF byline gives Jeeballah R, Al Zaabi A, El Keraby H, "AAl Abdulsalam" A (corresponding author, listed last). | Venue correct. **The author order differs between the registered metadata and the printed byline.** The .bib follows the DOI metadata. Decide whether to cite "Aal Abdulsalam et al." (DOI) or "Jeeballah et al." (PDF). "AAl" is a typo in the PDF. |
| 18 | twophaseexam2025 | Title + PMC12712565 ("verify journal/year/DOI") | **JMIR Med Inform 2025;13:e78432**, doi:10.2196/78432, published 3 Dec 2025; PMID 41171081; PMC12712565 (C, P, I). 4 authors: Abumelha M, AL-Ghamdi AAM, Fayoumi A, Ragab M. Crossref links a JMIR preprint, doi:10.2196/preprints.78432. | Completed; journal, year and DOI were missing. "Two-phase" means two training phases, not a two-step inference pipeline. |
| 19 | skeletonofthought2024 | Ning et al., ICLR 2024, arXiv 2307.15337 | ICLR 2024 poster, OpenReview forum mqVgBbNCm9, same 6 authors (O). arXiv v1 28 Jul 2023, v2 8 Oct 2023, v3 2 Mar 2024; comment "In ICLR'24"; cs.CL (A). ICLR proceedings have no pages or DOI. | Correct. Cite ICLR 2024 with the arXiv ID as eprint. The text is arXiv v3, which carries the ICLR header. |
| 20 | erman1980hearsay | ACM Computing Surveys 1980;12(2) | 12(2):213–253, June 1980, doi:10.1145/356810.356816; authors Erman LD, Hayes-Roth F, Lesser VR, Reddy DR (C). OpenAlex lists the ACM PDF as free to read (bronze OA) (X). A 1981 reprint exists in *Readings in Artificial Intelligence*, pp. 349–389, doi:10.1016/b978-0-934613-03-3.50029-5 (C); it is not the version cited. | Correct. Added pages, month and DOI. Full text obtained from ACM's free PDF through an Internet Archive capture. |
| 21 | nii1986blackboard | "Blackboard Systems, Part One: The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures", AI Magazine 1986;7(2), doi 10.1609/aimag.v7i2.537 | **Printed title:** "The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures", under a "PART ONE" label; the OJS metadata has the same title (W). Summer 1986, pp. 38–53 from the printed footers; single author H. Penny Nii.<br>**DOI:** resolves at doi.org (registration agency Crossref) (D), but the Crossref REST API and DOI content negotiation both return "Resource not found".<br>**OJS metadata:** gives the last page as 38, which is wrong. | **Title differs from the request:** "Blackboard Systems, Part One:" is not printed on the article; it is a common citation convention. The .bib uses the printed title with the note "Part one of a two-part article". Pages added. |
| 22 | blackboardllm2025 | Title as listed; arXiv 2510.01285 | 8 authors; v1 30 Sep 2025, v2 31 Jan 2026; primary category cs.MA, not cs.CL (A). The v1 abs page and the PDF write "LLM-based"; current arXiv metadata writes "LLM-Based". OpenReview lists an ICLR 2026 submission with venueid "Rejected_Submission" (O). No published version found (X). | Correct as a preprint. Not peer-reviewed. |
| 23 | blackboardmas2025 | Title as listed; arXiv 2507.01701 | 2 authors (Han B, Zhang S); v1 only, 2 Jul 2025; cs.MA (A). Semantic Scholar and OpenAlex list only arXiv (X). | Correct. A preprint. |
| 24 | hisccg2026 | Scientific Reports 2026, nature.com URL | Title identical. **Article in Press** (unedited manuscript), published online 22 Sep 2026 (received 1 Feb 2026, accepted 17 Jun 2026). No volume or article number yet (C, W). 4 authors: Tian P, Xie P, Li Q, Gu J. Licence CC BY-NC-ND 4.0. | Correct but necessarily incomplete. Add the volume and article number when assigned, and recheck the quotes against the final edited version. |
| 25 | trialgpt2024 | Jin Q et al., Nature Communications 2024, nature.com URL | Nat Commun 15(1):9074, online 18 Nov 2024 (received 18 Jan 2024, accepted 1 Oct 2024); PMID 39557832; PMC11574183; 10 authors (C, P, I). CC BY 4.0. | Correct. Added volume, article number, PMID, PMCID and authors. |
| 26 | thinkingmachines2025nondeterminism | He H (Thinking Machines Lab), 2025 blog; official URL to be found | **URL:** https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/.<br>**Byline:** "Horace He in collaboration with others at Thinking Machines", 10 Sep 2025. The page metadata says it was modified on 2026-08-31 (W).<br>**DOI:** 10.64434/tml.20250910, registered with Crossref as type "report" (C, D). Crossref lists "Thinking Machines Lab" twice as an author. | Correct; DOI added. **Grey literature.** The post changed after publication; the text in `md/` is the version captured on 2026-09-24. |
| 27 | atil2024nondeterminism | Atil B et al., "Non-Determinism of 'Deterministic' LLM Settings" (or the exact verified title), arXiv 2408.04667; venue? | **arXiv titles:** v1–v3 (6 Aug 2024 to 28 Mar 2025) were "LLM Stability: A detailed analysis with some surprises"; v4–v5 (1–2 Apr 2025) are 'Non-Determinism of "Deterministic" LLM Settings' (A).<br>**Published** as "Non-Determinism of “Deterministic” LLM System Settings in Hosted Environments", Proceedings of the 5th Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP 2025), Mumbai, Dec 2025, pp. 135–148, doi:10.18653/v1/2025.eval4nlp-1.12 (L, C, X).<br>**Authors:** the same 13 in all versions. The first author is "Atıl" in the Anthology and Crossref, "Atil" in the PDF. | **Published in a venue, under a longer title.** Cite the Eval4NLP version. The key keeps "2024"; the .bib has year = 2025 and the arXiv ID as eprint. |

### Other issues found inside the papers (batch 2)

Worth knowing before quoting numbers. These are the compiler's checks against the texts in `md/`.
- **psych2stage2026:**
  - The Discussion claims a "consistent advantage" of the 2-stage framework, but Tables 4–5 do not show one for hospitalization count (best: LLaMA with direct prompting, 0.692; P=.56), nor against joint extraction for last hospitalization (3 of 4 models not significant).
  - The "joint" comparator is described only in a table footnote and the Discussion.
  - The error-analysis percentages use different denominators.
- **twophaseexam2025:**
  - The private split is "1893 records" in the text but 1,839 notes in Table 1 and the Abstract; the error analysis mentions "26,297 features" against 20,360 in Table 1.
  - The Abstract's few-shot F1 range uses 0.960 (private) while the rest of the paper uses 0.952 (public).
  - Hallucination and miss rates are "defined as precision" and "as recall", but the formulas given are 1 − precision and 1 − recall.
- **promptplanextract2026:**
  - The Results twice name "Llama-3.1-70B"; Methods and the tables use Llama-3.3-70B-Instruct.
  - The latency SDs exceed the means for two models (outlier-dominated).
  - The corpus total is never stated: 286 reports were labelled, and 58 test reports became 53 after exclusions.
- **cancerregistrymas2026:**
  - The Abstract calls TNM and morphology "comparable" to direct prompting; §4.3 and the tables show the baseline ahead on T and M.
  - The evaluator agent reads the reference labels inside the pipeline, and an LLM normalizer maps predictions onto the gold label set before scoring (App. D.8–D.10).
  - §3.9 "Evaluation Metrics" is empty.
  - 818 cases were annotated, but only 628 were evaluated.
- **clinicirca2026:**
  - Mistral Small 3.2 is labelled "24B-A4B" in one place and a dense 24B elsewhere.
  - §5.3 says Stage 3 works "without re-reading the discharge note", but the Stage 3 prompt passes the note (restricted to clarifying wording).
  - No human–human agreement is reported, only judge-vs-gold agreement.
- **hisccg2026:**
  - The paper says decoding is fixed "to control randomness and improve reproducibility", yet extraction runs at temperature 1.0.
  - The LDE-500 gold labels are LLM pseudo-labels generated with the same hierarchical path that the method injects; a manual audit covers 50 chunks.
  - The model size is not given (only "Qwen3").
  - The unedited PDF interleaves equations and captions with the body text.
- **trialgpt2024:**
  - P@10 for the feature combination is 0.6699 in the text but 0.6688 in Table 2.
  - Two figure-panel references are mislabelled (Fig. 4d/e, Fig. 5b/d).
  - Matching is two calls per patient–trial pair (all inclusion criteria, then all exclusion criteria), not one call per criterion.
- **skeletonofthought2024:**
  - The open-model latencies in the main text are estimates from profiling. The measured batch tests (App. G.1.4) differ; for example, StableVicuna-13B gets 0.97×, which is no speed-up.
  - The two LLM judges disagree on the win rate (29.5% vs 45.8%).
- **blackboardllm2025:**
  - §4.2 says the system beats all baselines "on all three datasets", but RAG is ahead on DA-Code with Gemini 2.5 Flash (2.75% vs 0.55%).
  - The cost analysis uses a 50-question sample, while the gains quoted next to it come from the full Table 1.
  - There is no limitations section and no code link.
- **blackboardmas2025:**
  - The average rounds in the text (2.88, 3.05, 3.29) differ from Table 4 (2.88, 3.29, 3.04).
  - The 72.60 MATH figure in Tables 3–4 is the majority-vote result, not the decider result (72.8).
  - The Abstract's "less tokens" is second-lowest in Table 3.
- **erman1980hearsay:**
  - The text is ACM's own OCR, with many character errors.
  - The results in §§3.2–3.4 come from different configurations and are not comparable (fn. 13).
  - Nii dates HEARSAY-II to 1971–1976; Erman et al. date the start of the Hearsay-II effort to 1973 (1971 is the start of the DARPA program).
- **nii1986blackboard:**
  - The OCR renders "AI Magazine" as "Al Magazine" and one "that is," as "that is;"; figure text is mixed into the flow.
  - The article's own reference list gives Erman's initials as "D. L.".
- **thinkingmachines2025nondeterminism:**
  - The GPU used is not stated.
  - A sidenote says part of the FlexAttention changes are not in the code release.
  - The text says forward-pass kernels are run-to-run deterministic, while a sidenote hedges this for matmuls.
- **atil2024nondeterminism:**
  - The Abstract says accuracy varies by "up to 15%", but §7 reports a "72% (75% - 3%)" max–min difference, and 75 and 3 are that condition's BestAcc and WorstAcc.
  - §6.1 calls GPT-3.5's lower TARr "less instability", which is backwards.
  - Table 3 has TARa@10 < TARr@10 for GPT-3.5 on ruin names, which should be impossible.
  - The Anthology abstract gives the code URL as github.com/Anonymous; the PDF gives https://github.com/breckbaldwin/llm-stability.
  - **Differences from arXiv v5** (same models, tasks and runs, and identical few-shot Table 2):
    - The Eval4NLP version adds the API providers, the February 2025 run date, the details of the local A6000 run and a Limitations section.
    - It changes "not the only source" to "not the source" of non-determinism.
    - It drops v5's point that non-determinism compounds multiplicatively in pipelines (.95^4 = .814).

### Provenance and verification (batch 2)

- **PDFs** (`pdf/`), 11 in total:
  - arXiv (5): clinicirca2026, promptplanextract2026, skeletonofthought2024, blackboardllm2025, blackboardmas2025.
  - ACL Anthology (2): cancerregistrymas2026, atil2024nondeterminism.
  - nature.com (2): trialgpt2024, and hisccg2026 as the unedited "Article in Press" PDF.
  - AAAI OJS (1): nii1986blackboard, a scan with no text layer.
  - ACM (1): erman1980hearsay. It is free to read, but dl.acm.org returned a Cloudflare challenge, so the PDF came from the Internet Archive capture of 2025-01-05.
- **No PDF:**
  - psych2stage2026 and twophaseexam2025: the JMIR PDFs returned a bot challenge (HTTP 202, empty body) and the PMC PDF returned an HTML challenge page. Their text comes from the Europe PMC REST full-text JATS XML.
  - thinkingmachines2025nondeterminism: HTML only.
  - The arXiv v5 PDF of atil2024nondeterminism was downloaded for comparison but is not stored.
- **Conversion:**
  - PDFs were converted with pymupdf4llm 1.28.2, as in batch 1.
  - JATS XML and the blog HTML were converted with new small scripts. Tables were kept as markdown; figures are captions only. The blog's KaTeX is kept as TeX, sidenotes are inlined as "[Sidenote: …]" and interactive widgets were dropped.
  - Nii: OCR with the macOS Apple Vision framework (300 dpi, accurate mode) and a two-column reading-order heuristic. Line breaks and hyphenation are kept as printed.
  - Hearsay-II: ACM's own OCR text layer, errors kept.
- **Full text:** obtained for all 14 works. None is abstract-only.
- **Quote check:** all 82 new quotes were verified against `md/<key>.md` with the batch-1 normalization (Unicode quotes and dashes, markdown emphasis, whitespace), falling back to letters and digits only (LOOSE).
  - 72 matched EXACT and 10 LOOSE: 5 from OCR hyphenation (Nii), 1 lost line-break hyphen (Atil), 1 from italic markup (SoT) and 3 from math symbols or split decimals (blackboardllm2025). Each LOOSE match was inspected; none is MISSING.
  - Every number in the new fichas was also searched in its source text. The few not found verbatim are conversion artifacts (e.g. "0 _._ 847"), roundings of table values (e.g. 4,721,489 → 4.72M) or page numbers, and each was checked by hand.
- **Drafting:** fichas #14–#27 were written from the full texts and then checked centrally (quotes, numbers and metadata). *[Relevance]* lines are the compiler's reading for arm C (a shared case model injected into 18 parallel group calls) and for nondeterminism in vLLM runs.
