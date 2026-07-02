---
name: tutor-ode
description: Solucionador de certámenes de Ecuaciones Diferenciales Ordinarias. Use when user asks to "resolver EDO", "ecuaciones diferenciales ordinarias", "solución de Laplace", "valores de frontera", "Sturm-Liouville", or "desarrollar certamen de EDO".
---

# Ordinary Differential Equations Exam Solver

## When to use this skill
**ALWAYS** use this skill when the user requests help with:
- **Ordinary Differential Equations** curriculum.
- Solving First-Order ODEs (Separable, Linear, Exact, Homogeneous, Bernoulli).
- Second-Order Linear ODEs (Homogeneous/Non-homogeneous, Constant Coefficients, Cauchy-Euler).
- Laplace Transforms (for solving IVPs).
- Systems of Linear Differential Equations.
- Modeling with Differential Equations (Population, Mixing, Spring-Mass).

---

## Syllabus Reference — READ Before Answering

| Topic | File | Triggers |
|---|---|---|
| First-Order Equations | `syllabus/01-first-order-equations.md` | separable, lineal, exacta, homogénea, Bernoulli, factor integrante, IVP, existencia y unicidad |
| Second-Order Linear Equations | `syllabus/02-second-order-linear-equations.md` | ecuación característica, coeficientes indeterminados, variación de parámetros, Cauchy-Euler, Wronskiano, masa-resorte |
| Laplace Transforms | `syllabus/03-laplace-transforms.md` | transformada de Laplace, transformada inversa, función escalón, delta de Dirac, convolución, IVPs con Laplace |

Also read `shared/notation-standard.md` for notation conventions.

---

## Problem Solving Protocol

1. **Standardize**: rewrite in standard form if necessary for the calculation.
2. **Classify (Internal)**: Identify the specific type (Separable, Exact, Linear, etc.) to apply the correct algorithm, but do not write long explanations about it.
3. **Read Syllabus File** for the identified type if needed.
4. **Load Example Template (Few-Shot)**: ALWAYS read `ejercicios_resueltos/INDEX.md` and load the specific `.md` file for the identified problem type (e.g., `ejercicios_resueltos/01_primer_orden/02_lineal.md`) to mimic exactly the structural formatting and style.
5. **Execute directly**:
   - For **Geometric Modeling**:
     - Explicitly define the coordinates of the points of contact and intercepts (e.g. $A(0, y_A)$, $B(x_B, 0)$, $P(x, y)$).
     - State the geometric relations (e.g. distance $\overline{AP} = \overline{PB}$ or slope conditions).
     - Account for physical constraints (e.g. positive coordinates in the first quadrant, which affects signs of slopes/values).
   - For **Sturm / Boundary Value Problems**:
     - Apply case-by-case analysis based on parameters (e.g. $\lambda > 1$, $\lambda = 1$, $\lambda < 1$).
     - For theoretical proofs (like Sturm comparison), define the Wronskian $W(x)$, compute its derivative $W'(x)$, integrate over $[a, b]$, and carefully analyze signs at boundaries.
   - Show the mathematical development step-by-step cleanly (e.g. state characteristic equation, find roots, propose solution).
   - Do NOT explain theory or *why* a step is taken, just write the mathematical step.
   - Never forget $+C$.
   - For IVPs, find the constants directly and give the final particular solution.
6. **Final Answer**: Clearly state the final mathematical result.

---

## Exam Resolution Style & Semantic Flow
- **Estilo de Resolución:** Toda solución debe cumplir rigurosamente con las directrices de flujo semántico del lenguaje definidas en la skill rectora [[math-solver-style]](../math-solver-style/SKILL.md).
- **Conectores obligatorios:** Es imperativo usar exclusivamente conectores algebraicos breves en español (e.g., *"reemplazando en"*, *"integrando"*, *"volviendo a la variable original"*) para conectar los pasos del desarrollo.
- **Sin subtítulos:** Presentar el desarrollo en formato continuo, libre de títulos artificiales o explicaciones pedagógicas ajenas al certamen.
- **Vínculo al Orquestador:** Esta skill se ejecuta bajo la coordinación de [[exercise-solver]](../exercise-solver/SKILL.md).

## Common Errors Watchlist
- **Wronskian Basis Mismatch**: Be extremely careful with signs of roots in homogeneous solutions (e.g., if roots of auxiliary equation $r^2+r=0$ are $r=0,-1$, the basis is $\{1, e^{-t}\}$, NOT $\{1, e^t\}$; using the wrong basis invalidates variation of parameters).
- **Cauchy-Euler Derivative Conversions**: In independent variable changes ($x = e^t$), remember that $x y' = \dot{y}$ and $x^2 y'' = \ddot{y} - \dot{y}$, leading to a coefficient change in the linear equation.
- **Geometric Modeling Slopes**: Do not confuse normal slopes ($-1/y'$) with tangent slopes ($y'$), and verify if quadrant constraints restrict the sign of $y'$.
- Applying Laplace without expressing the IVP in standard form first.
- Forgetting $+C$ (or absorbing it incorrectly into a particular solution).
- Confusing $y_h$ and $y_p$: the particular solution must satisfy the **non-homogeneous** equation.
- In the Method of Undetermined Coefficients: forgetting to apply the **modification rule** when $y_p$ duplicates a term in $y_h$.
- In exact equations: not verifying $M_y = N_x$ before proceeding.
- In Cauchy-Euler: not converting to standard form before applying the characteristic equation.

