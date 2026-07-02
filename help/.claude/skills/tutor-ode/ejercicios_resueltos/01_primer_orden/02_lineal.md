# Ejercicio: Ecuación Lineal de Primer Orden

**Problema:**
Resolver el siguiente Problema de Valor Inicial (PVI):
$$ y' + 2y = e^{-t}, \quad y(0) = 3 $$

---
**Desarrollo:**

1. La ecuación ya está en forma estándar $y' + P(t)y = Q(t)$, donde $P(t) = 2$ y $Q(t) = e^{-t}$.

2. Se calcula el factor integrante $\mu(t)$:
$$ \mu(t) = e^{\int P(t) dt} = e^{\int 2 dt} = e^{2t} $$

3. Se multiplica la EDO por el factor integrante:
$$ e^{2t} y' + 2e^{2t} y = e^{2t} e^{-t} $$
$$ (e^{2t} y)' = e^t $$

4. Se integra a ambos lados:
$$ \int (e^{2t} y)' dt = \int e^t dt $$
$$ e^{2t} y = e^t + C $$

5. Se despeja la solución general $y(t)$:
$$ y(t) = e^{-t} + C e^{-2t} $$

6. Se aplica la condición inicial $y(0) = 3$ para encontrar $C$:
$$ 3 = e^{0} + C e^{0} $$
$$ 3 = 1 + C \implies C = 2 $$

**Solución Particular:**
$$ y(t) = e^{-t} + 2e^{-2t} $$
