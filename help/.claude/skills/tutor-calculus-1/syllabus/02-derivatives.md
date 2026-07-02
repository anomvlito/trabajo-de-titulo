# Tema 2 — Derivadas

**Referencias**: Spivak, *Calculus* (4th ed.), Ch. 9–10; Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 3.

---

## 2.1 Definición

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

- Si el límite existe, $f$ es **diferenciable** en $a$.
- Diferenciabilidad implica continuidad (el recíproco es falso: $|x|$ es continua en $0$ pero no diferenciable).

---

## 2.2 Reglas de Derivación

| Regla | Fórmula |
|---|---|
| Constante | $(c)' = 0$ |
| Potencia | $(x^n)' = nx^{n-1}$ |
| Suma | $(f \pm g)' = f' \pm g'$ |
| Producto | $(fg)' = f'g + fg'$ |
| Cociente | $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ |
| Cadena | $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$ |

**Derivadas de funciones elementales**:

| $f(x)$ | $f'(x)$ |
|---|---|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\ln x$ | $1/x$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\arcsin x$ | $1/\sqrt{1-x^2}$ |
| $\arccos x$ | $-1/\sqrt{1-x^2}$ |
| $\arctan x$ | $1/(1+x^2)$ |

---

## 2.3 Regla de la Cadena

$(f(g(x)))' = f'(g(x)) \cdot g'(x)$

**Ejemplo**: $\frac{d}{dx}\sin(x^2) = \cos(x^2) \cdot 2x$.

**Composición múltiple**: $(f \circ g \circ h)' = (f' \circ g \circ h) \cdot (g' \circ h) \cdot h'$.

---

## 2.4 Diferenciación Implícita

Cuando $y$ está definida implícitamente por $F(x,y) = 0$:
1. Derivar ambos lados respecto a $x$ (tratar $y$ como función de $x$, aplicar regla de la cadena).
2. Despejar $y' = dy/dx$.

**Ejemplo**: $x^2 + y^2 = 25$
$$2x + 2y\,y' = 0 \implies y' = -\frac{x}{y}$$

---

## 2.5 Teoremas Fundamentales

**Teorema de Rolle**: Si $f$ es continua en $[a,b]$, diferenciable en $(a,b)$, y $f(a) = f(b)$, entonces $\exists\, c \in (a,b)$ tal que $f'(c) = 0$.

**Teorema del Valor Medio (MVT)**: Si $f$ es continua en $[a,b]$ y diferenciable en $(a,b)$:
$$\exists\, c \in (a,b) : f'(c) = \frac{f(b)-f(a)}{b-a}$$

**Corolario**: Si $f'(x) = 0$ en un intervalo, entonces $f$ es constante en ese intervalo.

---

## 2.6 Derivadas de Orden Superior

- $f''(x) = (f')'(x)$: interpretación como aceleración (segunda derivada).
- $f^{(n)}(x)$: notación para la derivada de orden $n$.
- **Fórmula de Leibniz** (producto $n$-ésima derivada): $(fg)^{(n)} = \sum_{k=0}^n \binom{n}{k} f^{(k)} g^{(n-k)}$.
