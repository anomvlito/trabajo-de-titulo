# Tema 4 — Series Numéricas y de Potencias

**Referencias**: Spivak, *Calculus* (4th ed.), Ch. 23–24; Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 11.2–11.10.

---

## 4.1 Series Numéricas

Una **serie** $\sum_{n=1}^\infty a_n$ converge a $S$ si las sumas parciales $S_N = \sum_{n=1}^N a_n$ satisfacen $\lim_{N\to\infty} S_N = S$.

**Serie geométrica**: $\sum_{n=0}^\infty ar^n = \frac{a}{1-r}$ si $|r| < 1$; diverge si $|r| \ge 1$.

**Serie telescópica**: $\sum (a_n - a_{n+1}) = a_1 - \lim a_n$ (si el límite existe).

---

## 4.2 Tests de Convergencia

Aplicar **siempre** en este orden lógico:

### 1. Test de Divergencia (Condición Necesaria)
Si $\lim_{n\to\infty} a_n \ne 0$, la serie **diverge**. Si $\lim a_n = 0$, el test no concluye.

### 2. Test Integral
Si $f$ es positiva, continua, decreciente en $[1,\infty)$ y $a_n = f(n)$:
$$\sum_{n=1}^\infty a_n \text{ y } \int_1^\infty f(x)\, dx \text{ tienen el mismo comportamiento.}$$
**Validar los tres requisitos** antes de aplicar.

### 3. Test de Comparación Directa
Si $0 \le a_n \le b_n$: $\sum b_n$ conv. $\Rightarrow$ $\sum a_n$ conv.; $\sum a_n$ div. $\Rightarrow$ $\sum b_n$ div.

### 4. Test de Comparación al Límite
Si $a_n, b_n > 0$ y $\lim_{n\to\infty} \frac{a_n}{b_n} = L \in (0,\infty)$: ambas series tienen el mismo comportamiento.

### 5. Test del Cociente (Ratio)
$$L = \lim_{n\to\infty} \left|\frac{a_{n+1}}{a_n}\right|: \quad L < 1 \Rightarrow \text{conv. absoluta}; \quad L > 1 \Rightarrow \text{diverge}; \quad L=1 \Rightarrow \text{no concluye}$$

### 6. Test de la Raíz
$$L = \lim_{n\to\infty} \sqrt[n]{|a_n|}: \quad L < 1 \Rightarrow \text{conv. absoluta}; \quad L > 1 \Rightarrow \text{diverge}; \quad L=1 \Rightarrow \text{no concluye}$$

### 7. Test de la Serie Alternante (Leibniz)
$\sum (-1)^n b_n$ converge si: (i) $b_n > 0$, (ii) $b_n$ es decreciente, (iii) $\lim b_n = 0$.

---

## 4.3 Convergencia Absoluta vs. Condicional

- **Convergencia absoluta**: $\sum |a_n|$ converge $\Rightarrow$ $\sum a_n$ converge (y converge absolutamente).
- **Convergencia condicional**: $\sum a_n$ converge pero $\sum |a_n|$ diverge.
- Convergencia absoluta $\Rightarrow$ convergencia, pero no al revés.

---

## 4.4 Series de Potencias

$$\sum_{n=0}^\infty c_n (x-a)^n$$

**Radio de convergencia** $R$:
$$R = \frac{1}{\limsup_{n\to\infty} \sqrt[n]{|c_n|}} = \lim_{n\to\infty} \left|\frac{c_n}{c_{n+1}}\right|$$

La serie converge absolutamente en $(a-R, a+R)$ y diverge fuera de $[a-R, a+R]$. Los extremos deben verificarse individualmente.

**Diferenciación e integración término a término**: válidas en $(-R, R)$:
$$\left(\sum c_n x^n\right)' = \sum n c_n x^{n-1}, \qquad \int \sum c_n x^n\, dx = \sum \frac{c_n}{n+1} x^{n+1} + C$$

---

## 4.5 Series de Taylor y Maclaurin

$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n$$

**Series de Maclaurin estándar** (memorizar):

| $f(x)$ | Serie | Radio |
|---|---|---|
| $e^x$ | $\sum \frac{x^n}{n!}$ | $\infty$ |
| $\sin x$ | $\sum \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $\infty$ |
| $\cos x$ | $\sum \frac{(-1)^n x^{2n}}{(2n)!}$ | $\infty$ |
| $\ln(1+x)$ | $\sum \frac{(-1)^{n+1} x^n}{n}$ | $(-1,1]$ |
| $\frac{1}{1-x}$ | $\sum x^n$ | $(-1,1)$ |
| $(1+x)^k$ | $\sum \binom{k}{n} x^n$ | $(-1,1)$ |

**Error de Lagrange**: el residuo del polinomio de Taylor de grado $n$ satisface:
$$|R_n(x)| \le \frac{M}{(n+1)!}|x-a|^{n+1}, \quad M = \max_{t \in [a,x]} |f^{(n+1)}(t)|$$
