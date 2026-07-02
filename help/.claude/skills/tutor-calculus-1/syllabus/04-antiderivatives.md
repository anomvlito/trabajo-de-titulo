# Tema 4 — Primitivas y Antiderivadas

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 4.9, 5.4–5.5.

---

## 4.1 Definición

$F$ es una **antiderivada** (primitiva) de $f$ en un intervalo si $F'(x) = f(x)$.

**Familia de primitivas**: Si $F$ es una primitiva, $F(x) + C$ (con $C \in \mathbb{R}$ constante) es la primitiva general. Nunca omitir $+C$ en una integral indefinida.

---

## 4.2 Tabla de Antiderivadas Elementales

| $f(x)$ | $\int f(x)\, dx$ |
|---|---|
| $x^n$ ($n \ne -1$) | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |
| $\frac{1}{1+x^2}$ | $\arctan x + C$ |

---

## 4.3 Sustitución Simple (Regla de la Cadena Inversa)

Si $\int f(g(x)) g'(x)\, dx$: sea $u = g(x)$, $du = g'(x)\, dx$:
$$\int f(g(x)) g'(x)\, dx = \int f(u)\, du$$

**Ejemplo**: $\int 2x \cos(x^2)\, dx$. Sea $u = x^2$, $du = 2x\, dx$:
$$= \int \cos u\, du = \sin u + C = \sin(x^2) + C$$

**Verificación**: derivar el resultado siempre.

---

## 4.4 Teorema Fundamental del Cálculo

**TFC 1**: Si $f$ es continua en $[a,b]$ y $g(x) = \int_a^x f(t)\, dt$, entonces $g'(x) = f(x)$.

**TFC 2**: Si $F$ es cualquier antiderivada de $f$ continua en $[a,b]$:
$$\int_a^b f(x)\, dx = F(b) - F(a)$$

**Derivada de integral con límite variable**: $\frac{d}{dx} \int_a^{g(x)} f(t)\, dt = f(g(x)) \cdot g'(x)$.

---

## 4.5 Errores Comunes

- Olvidar $+C$ en integrales indefinidas.
- Aplicar $\int x^n\, dx = \frac{x^{n+1}}{n+1}$ con $n=-1$ (caso especial: $\int \frac{1}{x}\, dx = \ln|x| + C$).
- Olvidar el valor absoluto en $\ln|x|$.
- No verificar la derivada del resultado para confirmar la integración.
