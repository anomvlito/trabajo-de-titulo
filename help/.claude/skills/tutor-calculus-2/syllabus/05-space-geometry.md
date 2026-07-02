# Tema 5 — Geometría en el Espacio (R³)

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 12.

---

## 5.1 Vectores en R³

Un vector $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$. Norma: $\|\mathbf{v}\| = \sqrt{v_1^2+v_2^2+v_3^2}$.

**Operaciones**:
- Suma: $\mathbf{u} + \mathbf{v} = \langle u_1+v_1, u_2+v_2, u_3+v_3 \rangle$
- Escalar: $c\mathbf{v} = \langle cv_1, cv_2, cv_3 \rangle$
- Vector unitario: $\hat{\mathbf{v}} = \mathbf{v}/\|\mathbf{v}\|$

**Vectores canónicos**: $\mathbf{i} = \langle 1,0,0\rangle$, $\mathbf{j} = \langle 0,1,0\rangle$, $\mathbf{k} = \langle 0,0,1\rangle$.

---

## 5.2 Producto Punto (Escalar)

$$\mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3 = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$

**Aplicaciones**:
- Ángulo entre vectores: $\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$
- Ortogonalidad: $\mathbf{u} \perp \mathbf{v} \iff \mathbf{u}\cdot\mathbf{v} = 0$
- Proyección escalar: $\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|}$
- Proyección vectorial: $\text{proj}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{v}\|^2}\mathbf{v}$
- Trabajo: $W = \mathbf{F}\cdot\mathbf{d}$

---

## 5.3 Producto Cruz (Vectorial)

$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}$$

**Propiedades**:
- $\mathbf{u} \times \mathbf{v} \perp \mathbf{u}$ y $\mathbf{u} \times \mathbf{v} \perp \mathbf{v}$
- $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\|\mathbf{v}\|\sin\theta$ (área del paralelogramo)
- $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$ (anticonmutativo)
- $\mathbf{u} \parallel \mathbf{v} \iff \mathbf{u} \times \mathbf{v} = \mathbf{0}$

**Aplicaciones**:
- Normal a un plano: $\mathbf{n} = \mathbf{u} \times \mathbf{v}$
- Área del triángulo: $A = \frac{1}{2}\|\mathbf{u} \times \mathbf{v}\|$
- Volumen del paralelepípedo: $V = |(\mathbf{u} \times \mathbf{v}) \cdot \mathbf{w}|$ (producto triple)

---

## 5.4 Rectas en R³

**Forma vectorial**: $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{d}$, donde $\mathbf{r}_0$ es un punto y $\mathbf{d}$ es el vector director.

**Forma paramétrica**:
$$x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct$$

**Forma simétrica** (si $a,b,c \ne 0$):
$$\frac{x-x_0}{a} = \frac{y-y_0}{b} = \frac{z-z_0}{c}$$

---

## 5.5 Planos en R³

**Ecuación escalar**: $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$, es decir:
$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$

donde $\mathbf{n} = \langle a,b,c\rangle$ es el vector normal.

**Distancia de un punto $P_1$ al plano $ax+by+cz+d=0$**:
$$D = \frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$$

**Ángulo entre planos**: ángulo entre sus normales ($\cos\theta = |\hat{\mathbf{n}_1} \cdot \hat{\mathbf{n}_2}|$).

**Planos paralelos**: normales paralelas. **Perpendiculares**: normales ortogonales.
