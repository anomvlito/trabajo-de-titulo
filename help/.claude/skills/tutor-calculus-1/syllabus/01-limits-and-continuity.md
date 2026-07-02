# Tema 1 — Límites y Continuidad

**Referencias**: Spivak, *Calculus* (4th ed.), Ch. 5–6; Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 2.

---

## 1.1 Definición Épsilon-Delta

$$\lim_{x \to a} f(x) = L \iff \forall\, \varepsilon > 0,\; \exists\, \delta > 0 : 0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

**Demostración típica**: Para $f(x) = 3x - 1$, $a = 2$, $L = 5$:
- $|f(x) - L| = |3x - 4 - 5 + 4| = |3(x-2)| = 3|x-2|$
- Elegir $\delta = \varepsilon/3$: si $|x-2| < \delta$, entonces $|f(x)-5| = 3|x-2| < 3\delta = \varepsilon$. $\square$

**Límites laterales**:
- Por la derecha: $\lim_{x \to a^+} f(x)$
- Por la izquierda: $\lim_{x \to a^-} f(x)$
- El límite $\lim_{x \to a} f(x)$ existe $\iff$ ambos límites laterales existen e son iguales.

---

## 1.2 Álgebra de Límites

Si $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$:

| Propiedad | Regla |
|---|---|
| Suma | $\lim (f+g) = L+M$ |
| Producto | $\lim (fg) = LM$ |
| Cociente | $\lim \frac{f}{g} = \frac{L}{M}$, $M \ne 0$ |
| Potencia | $\lim [f(x)]^n = L^n$ |
| Composición | $\lim_{x\to a} f(g(x)) = f(M)$ si $f$ es continua en $M$ |

**Regla del Sandwich (Teorema del Emparedado)**:
Si $g(x) \le f(x) \le h(x)$ en un entorno de $a$ y $\lim g(x) = \lim h(x) = L$, entonces $\lim f(x) = L$.

**Límites trigonométricos fundamentales**:
$$\lim_{x \to 0} \frac{\sin x}{x} = 1, \qquad \lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

---

## 1.3 Formas Indeterminadas y L'Hôpital

**Formas indeterminadas**: $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0\cdot\infty$, $\infty - \infty$, $0^0$, $1^\infty$, $\infty^0$.

**Regla de L'Hôpital**: Si $\lim f(x)/g(x)$ es $\frac{0}{0}$ o $\frac{\infty}{\infty}$:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
siempre que el límite del cociente de derivadas exista.

> **Validar siempre**: confirmar que es una forma indeterminada antes de aplicar L'Hôpital.

---

## 1.4 Continuidad

**Definición**: $f$ es continua en $a$ si:
1. $f(a)$ está definida.
2. $\lim_{x \to a} f(x)$ existe.
3. $\lim_{x \to a} f(x) = f(a)$.

**Tipos de discontinuidades**:
- **Removible**: el límite existe pero $f(a)$ no está definida o es distinta del límite.
- **De salto**: los límites laterales existen pero son distintos.
- **Esencial (infinita)**: algún límite lateral es $\pm\infty$.

**Teorema del Valor Intermedio (Bolzano)**: Si $f$ es continua en $[a,b]$ y $f(a) \ne f(b)$, entonces $f$ toma todo valor entre $f(a)$ y $f(b)$.

**Teorema de Weierstrass (Valor Extremo)**: Si $f$ es continua en $[a,b]$, entonces $f$ alcanza su máximo y mínimo absolutos en $[a,b]$.

---

## 1.5 Límites al Infinito y Asíntotas

**Asíntota horizontal**: $y = L$ si $\lim_{x \to \pm\infty} f(x) = L$.

**Asíntota vertical**: $x = a$ si $\lim_{x \to a^{\pm}} f(x) = \pm\infty$.

**Asíntota oblicua**: $y = mx + b$ si $m = \lim_{x\to\infty} \frac{f(x)}{x}$ y $b = \lim_{x\to\infty} [f(x) - mx]$.

**Jerarquía de infinitos** ($x \to \infty$): $\ln x \ll x^a \ll e^x \ll x^x$.
