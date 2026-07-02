# Tema 2 — Ecuaciones Lineales de Segundo Orden

**Referencias**: Boyce & DiPrima, *Elementary Differential Equations* (10th ed.), Ch. 3–4; Zill, *A First Course in Differential Equations* (10th ed.), Ch. 3–4.

---

## 2.1 Forma General y Principio de Superposición

**Ecuación general**: $a(x)y'' + b(x)y' + c(x)y = g(x)$.

**Homogénea**: $g(x) = 0$. **No homogénea**: $g(x) \ne 0$.

**Solución general de la no homogénea**: $y = y_h + y_p$, donde:
- $y_h$: solución general de la ecuación homogénea asociada.
- $y_p$: una solución particular de la no homogénea.

**Principio de Superposición**: si $y_1$ e $y_2$ son soluciones de la homogénea, entonces $c_1 y_1 + c_2 y_2$ también lo es.

**Wronskiano**: $W(y_1, y_2)(x) = y_1 y_2' - y_1' y_2$.
- $W \ne 0$ en un punto $\iff$ $\{y_1, y_2\}$ son linealmente independientes (forman un conjunto fundamental de soluciones).

---

## 2.2 Ecuaciones con Coeficientes Constantes (Homogénea)

**Forma**: $ay'' + by' + cy = 0$.

**Ecuación característica**: $ar^2 + br + c = 0$.

| Discriminante $\Delta = b^2 - 4ac$ | Raíces | Solución general |
|---|---|---|
| $\Delta > 0$ | $r_1, r_2$ reales distintas | $y = c_1 e^{r_1 x} + c_2 e^{r_2 x}$ |
| $\Delta = 0$ | $r$ raíz doble $= -b/(2a)$ | $y = c_1 e^{rx} + c_2 x e^{rx}$ |
| $\Delta < 0$ | $r = \alpha \pm \beta i$ | $y = e^{\alpha x}(c_1 \cos\beta x + c_2 \sin\beta x)$ |

---

## 2.3 Método de Coeficientes Indeterminados

Aplica cuando $g(x)$ es una combinación de: polinomios, exponenciales $e^{\alpha x}$, $\cos\beta x$, $\sin\beta x$ (o productos de estas).

**Regla de la forma de $y_p$**:

| $g(x)$ | Proponer $y_p$ |
|---|---|
| $P_n(x)$ (polinomio grado $n$) | $A_n x^n + \cdots + A_0$ |
| $e^{\alpha x}$ | $Ae^{\alpha x}$ |
| $P_n(x)e^{\alpha x}$ | $(A_nx^n+\cdots+A_0)e^{\alpha x}$ |
| $\cos\beta x$ o $\sin\beta x$ | $A\cos\beta x + B\sin\beta x$ |
| $e^{\alpha x}\cos\beta x$ | $e^{\alpha x}(A\cos\beta x + B\sin\beta x)$ |

**Regla de modificación**: si $y_p$ propuesta es solución de la homogénea, multiplicar por $x$ (o $x^2$ si es raíz doble) hasta que deje de serlo.

**Procedimiento**:
1. Proponer $y_p$ con coeficientes indeterminados.
2. Calcular $y_p'$, $y_p''$.
3. Sustituir en la ecuación.
4. Igualar coeficientes de cada función base y resolver el sistema.

---

## 2.4 Variación de Parámetros

Método general (funciona para cualquier $g(x)$ continua).

Dado el conjunto fundamental $\{y_1, y_2\}$ de la homogénea:
$$y_p = -y_1 \int \frac{y_2\, g}{W}\, dx + y_2 \int \frac{y_1\, g}{W}\, dx$$

donde $W = W(y_1, y_2)$ y la ecuación está en **forma estándar** ($a = 1$).

---

## 2.5 Ecuación de Cauchy-Euler

**Forma**: $ax^2 y'' + bxy' + cy = g(x)$.

**Sustitución**: $x = e^t$ (o proponer $y = x^r$).

**Ecuación característica**: $ar(r-1) + br + c = 0$.

| Raíces | Solución homogénea |
|---|---|
| $r_1 \ne r_2$ reales | $c_1 x^{r_1} + c_2 x^{r_2}$ |
| $r$ doble | $c_1 x^r + c_2 x^r \ln x$ |
| $r = \alpha \pm \beta i$ | $x^\alpha(c_1 \cos(\beta\ln x) + c_2 \sin(\beta\ln x))$ |

---

## 2.6 Aplicaciones — Sistema Masa-Resorte

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

- Sin amortiguamiento ($c=0$): movimiento armónico simple, $\omega_0 = \sqrt{k/m}$.
- Subamortiguado ($c^2 < 4mk$): oscilación decreciente.
- Críticamente amortiguado ($c^2 = 4mk$): retorno más rápido sin oscilación.
- Sobreamortiguado ($c^2 > 4mk$): retorno exponencial sin oscilación.
- **Resonancia**: forzamiento a frecuencia $\omega_0$ sin amortiguamiento → amplitud crece sin límite.
