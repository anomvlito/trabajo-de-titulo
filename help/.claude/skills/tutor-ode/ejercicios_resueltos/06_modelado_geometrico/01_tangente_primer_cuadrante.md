# Ejercicio: Modelado Geométrico de Normales y Trayectorias Ortogonales

**Problema:**
1. Determinar la familia de curvas del primer cuadrante tal que para cada recta normal a una de ellas, el segmento comprendido entre la curva y el eje $X$ sea bisectado por el eje $Y$.
2. Determinar la familia de curvas ortogonales.

---
**Desarrollo:**

Sea $P(x, y)$ un punto de la curva en el primer cuadrante. La ecuación de la recta normal en $P$ es:
$$ Y - y = -\frac{1}{y'}(X - x) $$

Haciendo $X = 0$, obtenemos el intercepto con el eje $Y$, $A(0, y_A)$:
$$ y_A = y + \frac{x}{y'} $$

Haciendo $Y = 0$, obtenemos el intercepto con el eje $X$, $B(x_B, 0)$:
$$ x_B = x + y y' $$

La condición de que el eje $Y$ bisecte el segmento normal entre la curva y el eje $X$ significa que $A$ es el punto medio del segmento $PB$. Planteando la igualdad de distancias cuadráticas $\overline{PA}^2 = \overline{AB}^2$:
$$ (x - 0)^2 + (y - y_A)^2 = (0 - x_B)^2 + (y_A - 0)^2 $$

Sustituyendo las expresiones de $y_A$ y $x_B$:
$$ x^2 + \left(-\frac{x}{y'}\right)^2 = (x + y y')^2 + \left(y + \frac{x}{y'}\right)^2 $$
$$ x^2 \left(1 + \frac{1}{y'^2}\right) = (y y' + x)^2 \left(1 + \frac{1}{y'^2}\right) $$

Dividiendo por el término común no nulo $\left(1 + \frac{1}{y'^2}\right)$:
$$ x^2 = (y y' + x)^2 \implies \pm x = y y' + x $$

Para la rama con signo positivo:
$$ x = y y' + x \implies y y' = 0 \implies y \frac{dy}{dx} = 0 $$
Integrando a ambos lados:
$$ y(x) = C_1 $$

Para la rama con signo negativo:
$$ -x = y y' + x \implies y y' = -2x \implies y \, dy = -2x \, dx $$
Integrando a ambos lados:
$$ \frac{y^2}{2} = -x^2 + C \implies y^2 + 2x^2 = C_2 $$

Para determinar la familia ortogonal, reemplazamos $y'$ por $-\frac{1}{y'}$ en la ecuación diferencial original $\pm x = y y' + x$:
$$ \pm x = -\frac{y}{y'} + x $$

Para la primera rama ($y y' = 0$):
$$ y \left(-\frac{1}{y'}\right) = 0 \implies y' = \infty \implies x(y) = K_1 $$

Para la segunda rama ($y y' = -2x$):
$$ y \left(-\frac{1}{y'}\right) = -2x \implies \frac{y}{y'} = 2x \implies \frac{y'}{y} = \frac{1}{2x} $$
Integrando a ambos lados:
$$ \ln|y| = \frac{1}{2} \ln|x| + \ln K \implies y(x) = K_2 \sqrt{|x|} $$

**Solución:**
* Curvas Originales: Rectas horizontales $y = C_1$ y elipses $y^2 + 2x^2 = C_2$.
* Curvas Ortogonales: Rectas verticales $x = K_1$ y parábolas $y = K_2\sqrt{|x|}$.
