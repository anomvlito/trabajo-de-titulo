# Tema 1 — Ecuaciones de Primer Orden

**Referencias**: Boyce & DiPrima, *Elementary Differential Equations* (10th ed.), Ch. 1–2; Zill, *A First Course in Differential Equations* (10th ed.), Ch. 2.

---

## 1.1 Clasificación

Antes de resolver, **identificar** el tipo:

```
EDO de primer orden
├── Separable:    y' = g(x)·h(y)
├── Lineal:       y' + P(x)y = Q(x)
├── Exacta:       M dx + N dy = 0,  con My = Nx
├── Homogénea:    y' = F(y/x)
└── Bernoulli:    y' + P(x)y = Q(x)yⁿ
```

---

## 1.2 Ecuaciones Separables

**Forma**: $\frac{dy}{dx} = g(x)\,h(y)$.

**Método**:
$$\int \frac{dy}{h(y)} = \int g(x)\, dx$$

Despejar $y$ si es posible; dejar implícita si no.

**Cuidado**: verificar si $h(y_0) = 0$ da soluciones singulares (soluciones de equilibrio).

**Ejemplo**: $\frac{dy}{dx} = xy$
$$\int \frac{dy}{y} = \int x\, dx \implies \ln|y| = \frac{x^2}{2} + C_1 \implies y = Ce^{x^2/2}$$

---

## 1.3 Ecuaciones Lineales de Primer Orden

**Forma estándar**: $y' + P(x)y = Q(x)$.

**Factor integrante**: $\mu(x) = e^{\int P(x)\, dx}$.

**Método**:
1. Calcular $\mu(x)$.
2. Multiplicar ambos lados: $(\mu y)' = \mu Q$.
3. Integrar: $\mu y = \int \mu Q\, dx + C$.
4. Despejar $y$: $y = \frac{1}{\mu}\left(\int \mu Q\, dx + C\right)$.

**Verificación**: derivar $y$ y sustituir en la ecuación original.

---

## 1.4 Ecuaciones Exactas

**Forma**: $M(x,y)\, dx + N(x,y)\, dy = 0$.

**Condición de exactitud**: $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.

**Método**: encontrar $F(x,y)$ tal que $F_x = M$ y $F_y = N$:
1. $F(x,y) = \int M\, dx + g(y)$.
2. Derivar respecto a $y$ e igualar a $N$: $F_y = N$ determina $g'(y)$.
3. Integrar para obtener $g(y)$.
4. Solución implícita: $F(x,y) = C$.

**Si no es exacta**: buscar un factor integrante $\mu(x)$ o $\mu(y)$ para hacer la ecuación exacta.

---

## 1.5 Ecuaciones Homogéneas

**Forma**: $y' = F(y/x)$. Identificar: todos los términos tienen el mismo grado homogéneo.

**Sustitución**: $v = y/x \implies y = vx \implies y' = v + xv'$.

Sustituir y separar: $\frac{dv}{F(v)-v} = \frac{dx}{x}$.

---

## 1.6 Ecuaciones de Bernoulli

**Forma**: $y' + P(x)y = Q(x)y^n$, $n \ne 0,1$.

**Sustitución**: $v = y^{1-n}$, entonces $v' = (1-n)y^{-n}y'$.

Dividir la ecuación original por $y^n$:
$$y^{-n}y' + P(x)y^{1-n} = Q(x) \implies \frac{v'}{1-n} + P(x)v = Q(x)$$

Resulta una ecuación **lineal** en $v$.

---

## 1.7 Problemas de Valor Inicial (IVP)

La condición inicial $y(x_0) = y_0$ determina la constante $C$ de la solución general.

**Teorema de Existencia y Unicidad** (Picard): Si $f$ y $\frac{\partial f}{\partial y}$ son continuas en un rectángulo alrededor de $(x_0, y_0)$, entonces el IVP $y' = f(x,y)$, $y(x_0) = y_0$ tiene solución única en algún intervalo alrededor de $x_0$.
