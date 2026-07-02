# Ejercicio: Ecuación Integrodiferencial Reducible a Cauchy-Euler

**Problema:**
Resolver la siguiente ecuación integrodiferencial suponiendo que $y'$ es continua en el intervalo $[1, b]$:
$$ \frac{1}{2} y'(x) = -\frac{1}{6x^3} - \int_1^x \frac{y'(\tau)}{\tau} \, d\tau $$

---
**Desarrollo:**

Multiplicando por 2 toda la ecuación:
$$ y'(x) = -\frac{1}{3x^3} - 2\int_1^x \frac{y'(\tau)}{\tau} \, d\tau $$

Derivando con respecto a $x$ a ambos lados aplicando el Teorema Fundamental del Cálculo:
$$ y''(x) = \frac{1}{x^4} - \frac{2 y'(x)}{x} \implies y''(x) + \frac{2}{x} y'(x) = \frac{1}{x^4} $$

Haciendo el cambio de variable $v(x) = y'(x)$ (por ende $v' = y''$):
$$ v' + \frac{2}{x} v = \frac{1}{x^4} $$

Calculando el factor integrante $\mu(x)$:
$$ \mu(x) = e^{\int \frac{2}{x} \, dx} = e^{2\ln|x|} = x^2 \quad (\text{ya que } x \ge 1) $$

Multiplicando la ecuación lineal por el factor integrante $\mu(x) = x^2$:
$$ x^2 v' + 2x v = \frac{1}{x^2} \implies (x^2 v)' = \frac{1}{x^2} $$

Integrando respecto a $x$ a ambos lados:
$$ x^2 v = \int x^{-2} \, dx \implies x^2 v = -\frac{1}{x} + C_2 \implies v(x) = -\frac{1}{x^3} + \frac{C_2}{x^2} $$

Volviendo a la variable original $v(x) = y'(x)$ e integrando nuevamente:
$$ y(x) = \int \left( -x^{-3} + C_2 x^{-2} \right) \, dx $$
$$ y(x) = \frac{1}{2x^2} - \frac{C_2}{x} + C_1 $$

Redefiniendo la constante arbitraria $-C_2$ como $C_2$:
$$ y(x) = C_1 + \frac{C_2}{x} + \frac{1}{2x^2} $$

**Solución General:**
$$ y(x) = C_1 + \frac{C_2}{x} + \frac{1}{2x^2} $$
