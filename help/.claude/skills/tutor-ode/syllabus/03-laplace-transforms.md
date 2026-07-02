# Tema 3 — Transformada de Laplace

**Referencias**: Boyce & DiPrima, *Elementary Differential Equations* (10th ed.), Ch. 6; Zill, *A First Course in Differential Equations* (10th ed.), Ch. 7.

---

## 3.1 Definición

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t)\, dt$$

Existe para $s > \sigma_0$ (abscisa de convergencia) si $f$ es de orden exponencial.

---

## 3.2 Tabla de Transformadas Fundamentales

| $f(t)$ | $\mathcal{L}\{f(t)\} = F(s)$ | Condición |
|---|---|---|
| $1$ | $\dfrac{1}{s}$ | $s > 0$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $s > 0$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ | $s > a$ |
| $\sin bt$ | $\dfrac{b}{s^2+b^2}$ | $s > 0$ |
| $\cos bt$ | $\dfrac{s}{s^2+b^2}$ | $s > 0$ |
| $e^{at}\sin bt$ | $\dfrac{b}{(s-a)^2+b^2}$ | $s > a$ |
| $e^{at}\cos bt$ | $\dfrac{s-a}{(s-a)^2+b^2}$ | $s > a$ |
| $t^n e^{at}$ | $\dfrac{n!}{(s-a)^{n+1}}$ | $s > a$ |
| $\delta(t-a)$ | $e^{-as}$ | $a \ge 0$ |
| $u_a(t) = u(t-a)$ | $\dfrac{e^{-as}}{s}$ | $s > 0$ |

---

## 3.3 Propiedades

**Linealidad**: $\mathcal{L}\{af + bg\} = a F(s) + b G(s)$.

**Derivada**:
$$\mathcal{L}\{f'(t)\} = s F(s) - f(0)$$
$$\mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0) - f'(0)$$
$$\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)$$

**Traslación en $s$** (multiplicación por exponencial):
$$\mathcal{L}\{e^{at}f(t)\} = F(s-a)$$

**Traslación en $t$** (función escalón de Heaviside $u(t-a)$):
$$\mathcal{L}\{u(t-a)\,f(t-a)\} = e^{-as}F(s)$$

Para $\mathcal{L}\{u(t-a)\,g(t)\}$: reescribir $g(t) = f(t-a)$ determinando $f$.

**Convolución**:
$$\mathcal{L}\{(f*g)(t)\} = F(s)\,G(s), \qquad (f*g)(t) = \int_0^t f(\tau)\,g(t-\tau)\, d\tau$$

---

## 3.4 Método para Resolver IVPs con Laplace

**Protocolo**:
1. Aplicar $\mathcal{L}$ a ambos lados de la EDO usando las condiciones iniciales.
2. Despejar $Y(s) = \mathcal{L}\{y(t)\}$ algebraicamente.
3. Descomponer $Y(s)$ en fracciones parciales si es necesario.
4. Aplicar $\mathcal{L}^{-1}$ usando la tabla.

**Ejemplo**: $y'' + 4y = \sin 2t$, $y(0) = 0$, $y'(0) = 0$.

$$s^2Y - 0 - 0 + 4Y = \frac{2}{s^2+4} \implies Y = \frac{2}{(s^2+4)^2}$$

Usar tabla o convolución: $\mathcal{L}^{-1}\left\{\frac{2}{(s^2+4)^2}\right\} = \frac{1}{4}(\sin 2t - 2t\cos 2t)$.

---

## 3.5 Función Escalón de Heaviside y Forzamiento Discontinuo

$$u(t-a) = \begin{cases} 0 & t < a \\ 1 & t \ge a \end{cases}$$

**Escritura de funciones por tramos**:
$$f(t) = \begin{cases} g_1(t) & 0 \le t < a \\ g_2(t) & t \ge a \end{cases} = g_1(t) + [g_2(t) - g_1(t)]\,u(t-a)$$

---

## 3.6 Delta de Dirac — Forzamiento Impulsivo

$$\delta(t-a): \quad \int_{-\infty}^\infty \delta(t-a)\,f(t)\, dt = f(a)$$

$$\mathcal{L}\{\delta(t-a)\} = e^{-as}, \qquad \mathcal{L}^{-1}\{e^{-as}\} = \delta(t-a)$$

**Uso**: modelar fuerzas de golpe instantáneo (impacto, descarga eléctrica).
