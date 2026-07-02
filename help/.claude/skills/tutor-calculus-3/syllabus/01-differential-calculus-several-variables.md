# Tema 1 — Cálculo Diferencial de Varias Variables

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 14; Spivak, *Calculus on Manifolds*, Ch. 2.

---

## 1.1 Topología Básica en Rⁿ

- **Bola abierta**: $B(\mathbf{a}, r) = \{\mathbf{x} \in \mathbb{R}^n : \|\mathbf{x}-\mathbf{a}\| < r\}$.
- **Conjunto abierto**: todo punto es interior (tiene una bola abierta contenida en el conjunto).
- **Conjunto cerrado**: contiene todos sus puntos de acumulación (complemento de abierto).
- **Conjunto acotado**: contenido en alguna bola de radio finito.
- **Conjunto compacto** (en $\mathbb{R}^n$): cerrado y acotado.

---

## 1.2 Límites y Continuidad

$$\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) = L \iff \forall\, \varepsilon > 0,\; \exists\, \delta > 0 : 0 < \|\mathbf{x}-\mathbf{a}\| < \delta \Rightarrow |f(\mathbf{x})-L| < \varepsilon$$

**Estrategia para demostrar que el límite no existe**: encontrar dos caminos hacia $\mathbf{a}$ con límites distintos.

**Límites en coordenadas polares**: para $f(x,y)$ con $\mathbf{a} = \mathbf{0}$, escribir $x = r\cos\theta$, $y = r\sin\theta$ y analizar $r \to 0$.

---

## 1.3 Derivadas Parciales vs. Diferenciabilidad

**Derivada parcial**:
$$\frac{\partial f}{\partial x}(a,b) = \lim_{h \to 0} \frac{f(a+h,b) - f(a,b)}{h}$$

> **Trampa crítica**: La existencia de $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ **no implica** diferenciabilidad. Solo implica que la función tiene "tangentes" en las direcciones axiales.

**Diferenciabilidad real**: $f$ es diferenciable en $\mathbf{a}$ si existe una transformación lineal $Df(\mathbf{a})$ tal que:
$$\lim_{\mathbf{h} \to \mathbf{0}} \frac{f(\mathbf{a}+\mathbf{h}) - f(\mathbf{a}) - Df(\mathbf{a})\mathbf{h}}{\|\mathbf{h}\|} = 0$$

**Condición suficiente**: si $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$ existen y son **continuas** en $\mathbf{a}$, entonces $f$ es diferenciable en $\mathbf{a}$.

---

## 1.4 Gradiente, Derivada Direccional y Plano Tangente

**Gradiente**: $\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle$.

**Derivada direccional** (en la dirección del vector unitario $\hat{\mathbf{u}}$):
$$D_{\hat{\mathbf{u}}} f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \hat{\mathbf{u}}$$

- $\nabla f$ apunta en la dirección de **máximo crecimiento** de $f$.
- $-\nabla f$ apunta en la dirección de **máximo decrecimiento**.
- $\|\nabla f\|$ es la tasa de cambio máxima.

**Plano tangente** a $z = f(x,y)$ en $(a,b)$:
$$z - f(a,b) = f_x(a,b)(x-a) + f_y(a,b)(y-b)$$

**Aproximación lineal**: $f(a+\Delta x, b+\Delta y) \approx f(a,b) + f_x \Delta x + f_y \Delta y$.

---

## 1.5 Regla de la Cadena Multivariable

Si $z = f(x,y)$, $x = x(t)$, $y = y(t)$:
$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

Si $z = f(x,y)$, $x = x(s,t)$, $y = y(s,t)$:
$$\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial s}$$

---

## 1.6 Optimización

**Puntos críticos**: donde $\nabla f = \mathbf{0}$ o las parciales no existen.

**Test de la segunda derivada (Hessiano)** para $f(x,y)$: sea $D = f_{xx}f_{yy} - f_{xy}^2$:
- $D > 0$ y $f_{xx} > 0$: **mínimo local**.
- $D > 0$ y $f_{xx} < 0$: **máximo local**.
- $D < 0$: **punto silla**.
- $D = 0$: test no concluyente.

**Extremos absolutos en región cerrada y acotada**:
1. Encontrar puntos críticos en el interior.
2. Parametrizar y analizar el borde.
3. Comparar todos los valores.

**Multiplicadores de Lagrange**: maximizar/minimizar $f(\mathbf{x})$ sujeto a $g(\mathbf{x}) = 0$:
$$\nabla f = \lambda \nabla g, \quad g(\mathbf{x}) = 0$$
Sistema de ecuaciones con incógnitas $(x, y, z, \lambda)$.
