# Tema 3 — Sucesiones e Integrales Impropias

**Referencias**: Spivak, *Calculus* (4th ed.), Ch. 22; Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 11.1, 7.8.

---

## 3.1 Sucesiones

Una **sucesión** $\{a_n\}_{n=1}^\infty$ converge a $L$ si:
$$\lim_{n \to \infty} a_n = L$$

**Teorema de Convergencia Monótona**: Toda sucesión monótona y acotada converge.
- Creciente y acotada superiormente → converge.
- Decreciente y acotada inferiormente → converge.

**Límites útiles de sucesiones** ($r \in \mathbb{R}$, $p > 0$):
- $\lim n^{1/n} = 1$
- $\lim r^n = 0$ si $|r| < 1$; diverge si $|r| > 1$
- $\lim \frac{n^p}{e^n} = 0$
- $\lim \frac{\ln n}{n} = 0$
- $\lim \left(1 + \frac{1}{n}\right)^n = e$

---

## 3.2 Integrales Impropias

### Tipo I — Límites infinitos

$$\int_a^{\infty} f(x)\, dx = \lim_{t \to \infty} \int_a^t f(x)\, dx$$

**Nunca escribir** $\int_1^\infty$ sin el límite. La notación correcta siempre es $\lim_{t \to \infty} \int_1^t$.

$$\int_{-\infty}^{\infty} f(x)\, dx = \int_{-\infty}^c f(x)\, dx + \int_c^{\infty} f(x)\, dx$$
(ambas deben converger; elegir cualquier $c$ conveniente).

### Tipo II — Discontinuidades del integrando

Si $f$ tiene una singularidad en $b$:
$$\int_a^b f(x)\, dx = \lim_{t \to b^-} \int_a^t f(x)\, dx$$

**Trampa**: $\int_{-1}^{1} \frac{1}{x}\, dx$ no es $0$. La función tiene discontinuidad esencial en $0$ y la integral diverge.

### Integral $p$ de referencia

$$\int_1^\infty \frac{dx}{x^p} \begin{cases} \text{converge} & \text{si } p > 1 \\ \text{diverge} & \text{si } p \le 1 \end{cases}$$

$$\int_0^1 \frac{dx}{x^p} \begin{cases} \text{converge} & \text{si } p < 1 \\ \text{diverge} & \text{si } p \ge 1 \end{cases}$$

### Criterio de Comparación para Integrales

Si $0 \le f(x) \le g(x)$ para $x \ge a$:
- $\int_a^\infty g$ converge $\Rightarrow$ $\int_a^\infty f$ converge.
- $\int_a^\infty f$ diverge $\Rightarrow$ $\int_a^\infty g$ diverge.

**Criterio de comparación al límite**: si $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L \in (0, \infty)$, entonces $\int f$ y $\int g$ tienen el mismo comportamiento.
