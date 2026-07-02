# Tema 3 — Cálculo Vectorial

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 16; Spivak, *Calculus on Manifolds*, Ch. 4–5.

---

## 3.1 Campos Vectoriales

Un **campo vectorial** en $\mathbb{R}^2$: $\mathbf{F}(x,y) = P(x,y)\,\mathbf{i} + Q(x,y)\,\mathbf{j}$.

**Divergencia**: $\text{div}\,\mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$ (escalar).
Interpretación física: expansión/compresión de fluido.

**Rotacional**: $\text{curl}\,\mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ \partial_x & \partial_y & \partial_z \\ P & Q & R\end{vmatrix}$ (vector).
Interpretación física: rotación local del fluido.

**Campo conservativo**: $\mathbf{F} = \nabla f$ para algún potencial $f$. Condición necesaria: $\text{curl}\,\mathbf{F} = \mathbf{0}$.

> **Distinción crítica**: $\text{curl}\,\mathbf{F} = \mathbf{0}$ es suficiente para que $\mathbf{F}$ sea conservativo **solo si el dominio es simplemente conexo**.

---

## 3.2 Integrales de Línea

**Escalar** (masa de un alambre con densidad $f$):
$$\int_C f\, ds = \int_a^b f(\mathbf{r}(t))\,\|\mathbf{r}'(t)\|\, dt$$

**Vectorial / Trabajo**:
$$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\, dt$$

**Teorema Fundamental de las Integrales de Línea**: si $\mathbf{F} = \nabla f$:
$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$
(independiente de la trayectoria; en curva cerrada = 0).

---

## 3.3 Teorema de Green

Para región $D$ simplemente conexa con frontera $C = \partial D$ orientada positivamente (sentido antihorario):
$$\oint_C P\, dx + Q\, dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$$

**Área por Green**: $A = \frac{1}{2}\oint_C x\, dy - y\, dx$.

---

## 3.4 Integrales de Superficie

**Escalar** (área o masa de una superficie):
$$\iint_S f\, dS = \iint_D f(\mathbf{r}(u,v))\,\|\mathbf{r}_u \times \mathbf{r}_v\|\, dA$$

**Flujo vectorial**:
$$\iint_S \mathbf{F}\cdot d\mathbf{S} = \iint_D \mathbf{F}(\mathbf{r}(u,v))\cdot(\mathbf{r}_u \times \mathbf{r}_v)\, dA$$

**Orientación**: la normal $\mathbf{r}_u \times \mathbf{r}_v$ debe apuntar hacia el lado correcto según el problema.

---

## 3.5 Los Tres Grandes Teoremas

### Teorema de Stokes
Generaliza Green a superficies en $\mathbb{R}^3$. Sea $S$ superficie orientada con frontera $C = \partial S$ (orientación inducida por regla de la mano derecha):
$$\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F})\cdot d\mathbf{S}$$

### Teorema de Gauss (Divergencia)
Para región sólida $E$ con superficie cerrada $S = \partial E$ (normal apuntando hacia afuera):
$$\oiint_S \mathbf{F}\cdot d\mathbf{S} = \iiint_E (\nabla \cdot \mathbf{F})\, dV$$

### Tabla de Aplicabilidad

| Teorema | Convierte | Condición |
|---|---|---|
| Green | $\oint_C \to \iint_D$ | $C$ cerrada plana, $D$ simplemente conexo |
| Stokes | $\oint_C \to \iint_S$ | $C = \partial S$, orientación coherente |
| Gauss | $\oiint_S \to \iiint_E$ | $S = \partial E$ cerrada, normal exterior |

**Error frecuente — Orientación en Stokes**: la normal de $S$ y la dirección de $C$ deben satisfacer la regla de la mano derecha. Verificar siempre antes de calcular.
