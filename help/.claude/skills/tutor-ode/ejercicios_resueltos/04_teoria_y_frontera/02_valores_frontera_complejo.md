# Ejercicio: Problema de Valores en la Frontera (Sturm-Liouville)

**Problema:**
Encontrar los valores propios $\lambda$ y las funciones propias asociadas del siguiente problema de valores en la frontera:
$$ y''(x) + 2y'(x) + (1 + \lambda) y(x) = 0, \quad y(0) = 0, \quad y'(1) + y(1) = 0 $$

---
**Desarrollo:**

La ecuación característica asociada es:
$$ r^2 + 2r + (1 + \lambda) = 0 \implies r = -1 \pm \sqrt{-\lambda} $$

Analizando según el signo del parámetro $\lambda$:

* **Caso $\lambda < 0$ (Sean $\lambda = -k^2$ con $k > 0$):**
Las raíces son reales y distintas $r = -1 \pm k$. La solución general es:
$$ y(x) = e^{-x} (A \cosh(kx) + B \sinh(kx)) $$
Aplicando la condición $y(0) = 0$:
$$ y(0) = A = 0 \implies y(x) = B e^{-x} \sinh(kx) $$
Derivando $y(x)$:
$$ y'(x) = B e^{-x} (k \cosh(kx) - \sinh(kx)) $$
Sustituyendo en la condición de borde $y'(1) + y(1) = 0$:
$$ B e^{-1} (k \cosh(k) - \sinh(k)) + B e^{-1} \sinh(k) = 0 \implies B e^{-1} k \cosh(k) = 0 $$
Como $e^{-1} \neq 0$ y $k \cosh(k) > 0$, esto exige $B = 0$, resultando la solución trivial $y(x) = 0$.

* **Caso $\lambda = 0$:**
La raíz característica es doble $r = -1$. La solución general es:
$$ y(x) = e^{-x} (C_1 + C_2 x) $$
Aplicando la condición $y(0) = 0$:
$$ y(0) = C_1 = 0 \implies y(x) = C_2 x e^{-x} $$
Derivando $y(x)$:
$$ y'(x) = C_2 e^{-x} (1 - x) $$
Sustituyendo en la condición de borde $y'(1) + y(1) = 0$:
$$ C_2 e^{-1} (1 - 1) + C_2 e^{-1} = 0 \implies C_2 e^{-1} = 0 \implies C_2 = 0 $$
Obtenemos solo la solución trivial $y(x) = 0$.

* **Caso $\lambda > 0$ (Sean $\lambda = \beta^2$ con $\beta > 0$):**
Las raíces características son complejas conjugadas $r = -1 \pm i\beta$. La solución general es:
$$ y(x) = e^{-x} (C_1 \cos(\beta x) + C_2 \sin(\beta x)) $$
Aplicando la condición $y(0) = 0$:
$$ y(0) = C_1 = 0 \implies y(x) = C_2 e^{-x} \sin(\beta x) $$
Derivando $y(x)$:
$$ y'(x) = C_2 e^{-x} (\beta \cos(\beta x) - \sin(\beta x)) $$
Sustituyendo en la condición de borde $y'(1) + y(1) = 0$:
$$ C_2 e^{-1} (\beta \cos(\beta) - \sin(\beta)) + C_2 e^{-1} \sin(\beta) = 0 \implies C_2 e^{-1} \beta \cos(\beta) = 0 $$
Para obtener soluciones no triviales ($C_2 \neq 0$), al ser $e^{-1} \neq 0$ y $\beta > 0$:
$$ \cos(\beta) = 0 \implies \beta_n = (2n - 1) \frac{\pi}{2}, \quad n \in \mathbb{N} $$

Volviendo a la variable original $\lambda_n = \beta_n^2$:
$$ \lambda_n = \left( (2n - 1) \frac{\pi}{2} \right)^2, \quad n \in \mathbb{N} $$

Sustituyendo en la solución:
$$ y_n(x) = e^{-x} \sin\left( (2n - 1) \frac{\pi}{2} x \right) $$

**Solución:**
* Valores propios: $\lambda_n = \left( \frac{(2n - 1)\pi}{2} \right)^2$ para $n = 1, 2, 3, \dots$
* Funciones propias: $y_n(x) = e^{-x} \sin\left( \frac{(2n - 1)\pi}{2} x \right)$
