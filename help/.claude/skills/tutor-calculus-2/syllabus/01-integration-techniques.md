# Tema 1 — Técnicas de Integración

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 7; Spivak, *Calculus*, Ch. 18–19.

---

## 1.1 Sustitución (Cambio de Variable)

Sea $u = g(x)$, $du = g'(x)\, dx$:
$$\int f(g(x))\, g'(x)\, dx = \int f(u)\, du$$

Para integrales definidas, cambiar los límites: si $u = g(x)$, los nuevos límites son $g(a)$ y $g(b)$.

---

## 1.2 Integración por Partes

$$\int u\, dv = uv - \int v\, du$$

**Regla LIATE** para elegir $u$ (en orden de prioridad):
1. **L**ogarítmicas: $\ln x$, $\log_a x$
2. **I**nversas trigonométricas: $\arctan x$, $\arcsin x$
3. **A**lgebraicas: $x^n$, polinomios
4. **T**rigonométricas: $\sin x$, $\cos x$
5. **E**xponenciales: $e^x$, $a^x$

**Caso cíclico** (aparece la misma integral): sea $I = \int e^x \sin x\, dx$. Aplicar partes dos veces, aislar $I$:
$$I = -e^x \cos x + e^x \sin x - I \implies I = \frac{e^x(\sin x - \cos x)}{2} + C$$

---

## 1.3 Integrales Trigonométricas

### $\int \sin^m x \cos^n x\, dx$

- **$n$ impar**: guardar un $\cos x\, dx$, convertir el resto con $\cos^2 x = 1 - \sin^2 x$. Sustituir $u = \sin x$.
- **$m$ impar**: análogo con $u = \cos x$.
- **Ambos pares**: usar identidades de ángulo doble:
  $\sin^2 x = \frac{1-\cos 2x}{2}$, $\cos^2 x = \frac{1+\cos 2x}{2}$.

### $\int \tan^m x \sec^n x\, dx$

- **$n$ par**: guardar $\sec^2 x$, convertir resto con $\sec^2 x = 1 + \tan^2 x$. Sustituir $u = \tan x$.
- **$m$ impar**: guardar $\sec x \tan x$, convertir resto con $\tan^2 x = \sec^2 x - 1$. Sustituir $u = \sec x$.

**Integrales especiales**:
$$\int \sec x\, dx = \ln|\sec x + \tan x| + C, \qquad \int \sec^3 x\, dx = \frac{1}{2}(\sec x \tan x + \ln|\sec x + \tan x|) + C$$

---

## 1.4 Sustitución Trigonométrica

| Expresión | Sustitución | Identidad usada |
|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$, $\theta \in [-\pi/2, \pi/2]$ | $1-\sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$, $\theta \in (-\pi/2, \pi/2)$ | $1+\tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$, $\theta \in [0, \pi/2) \cup [\pi, 3\pi/2)$ | $\sec^2\theta - 1 = \tan^2\theta$ |

**Siempre dibujar el triángulo rectángulo** para volver a la variable original.

---

## 1.5 Fracciones Parciales

Para $\int \frac{P(x)}{Q(x)}\, dx$ con $\deg P < \deg Q$:

1. Factorizar $Q(x)$ completamente sobre $\mathbb{R}$.
2. Descomponer según los factores:

| Factor de $Q$ | Término en la descomposición |
|---|---|
| $(x-a)$ lineal | $\frac{A}{x-a}$ |
| $(x-a)^k$ repetido | $\frac{A_1}{x-a} + \cdots + \frac{A_k}{(x-a)^k}$ |
| $(x^2+bx+c)$ irreducible | $\frac{Ax+B}{x^2+bx+c}$ |
| $(x^2+bx+c)^k$ repetido | $\frac{A_1x+B_1}{x^2+bx+c} + \cdots + \frac{A_kx+B_k}{(x^2+bx+c)^k}$ |

3. Multiplicar por $Q(x)$ y resolver el sistema de coeficientes (sustituir valores convenientes de $x$ o igualar coeficientes).

**Si $\deg P \ge \deg Q$**: dividir primero (división polinomial).
