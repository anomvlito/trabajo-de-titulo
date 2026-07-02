# Ejercicio: Ecuación Diferencial Separable

**Problema:**
Resolver la siguiente ecuación diferencial:
$$ \frac{dy}{dt} = \frac{t}{y} $$

---
**Desarrollo:**

1. Se separan las variables a lados opuestos de la igualdad:
$$ y \, dy = t \, dt $$

2. Se integra a ambos lados:
$$ \int y \, dy = \int t \, dt $$

3. Se resuelven las integrales (agregando la constante $C$ al lado de la variable independiente):
$$ \frac{y^2}{2} = \frac{t^2}{2} + C $$

4. (Opcional dependiendo del problema) Se despeja $y(t)$ para encontrar la solución explícita. Multiplicando por 2:
$$ y^2 = t^2 + 2C $$
Como $2C$ es una constante arbitraria, la podemos reescribir simplemente como $C_1$:
$$ y^2 = t^2 + C_1 $$
$$ y(t) = \pm \sqrt{t^2 + C_1} $$

**Solución General:**
$$ y^2 - t^2 = C_1 $$
*(Nota: Muchas veces en variables separables es aceptable dejar la solución en forma implícita).*
