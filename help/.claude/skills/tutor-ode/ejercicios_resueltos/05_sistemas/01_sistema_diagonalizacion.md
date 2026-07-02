# Ejercicio: Sistema de EDOs de Segundo Orden y Diagonalización

**Problema:**
Resolver el siguiente sistema de ecuaciones diferenciales en términos de la matriz $A$:
$$ \mathbf{x}''(t) = A^2 \mathbf{x}(t) $$
sujeto a las condiciones de contorno:
$$ \mathbf{x}(0) = \mathbf{x}_0, \quad \mathbf{x}(1) = \mathbf{x}_1 $$
donde $A$ es una matriz real cuadrada de orden $n$, simétrica y con valores propios reales $\lambda_j > 0$ distintos entre sí para todo $j = 1, \dots, n$.

---
**Desarrollo:**

Como $A$ es simétrica y tiene valores propios distintos, es diagonalizable. Existe una matriz invertible $P$ tal que:
$$ A = P D P^{-1}, \quad D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n) $$

Reemplazando en el sistema original:
$$ \mathbf{x}'' = P D^2 P^{-1} \mathbf{x} \implies P^{-1} \mathbf{x}'' - D^2 (P^{-1} \mathbf{x}) = 0 $$

Haciendo el cambio de variable $\mathbf{u}(t) = P^{-1} \mathbf{x}(t)$:
$$ \mathbf{u}''(t) - D^2 \mathbf{u}(t) = 0 $$

Esto nos da $n$ ecuaciones escalares independientes:
$$ u_i''(t) - \lambda_i^2 u_i(t) = 0, \quad i = 1, \dots, n $$

Como los valores propios son estrictamente positivos ($\lambda_i > 0$), proponemos la solución:
$$ u_i(t) = \alpha_i e^{-\lambda_i t} + \beta_i e^{\lambda_i t} $$

Expresando esto en forma vectorial:
$$ \mathbf{u}(t) = e^{-tD} \boldsymbol{\alpha} + e^{tD} \boldsymbol{\beta} $$

Volviendo a la variable original multiplicando por $P$:
$$ \mathbf{x}(t) = P \mathbf{u}(t) = P e^{-tD} \boldsymbol{\alpha} + P e^{tD} \boldsymbol{\beta} $$

Utilizando la relación de semejanza para exponenciales de matrices ($P e^{\pm tD} = e^{\pm tA} P$):
$$ \mathbf{x}(t) = e^{-tA} (P \boldsymbol{\alpha}) + e^{tA} (P \boldsymbol{\beta}) $$

Redefiniendo los vectores de constantes como $\boldsymbol{\bar{\alpha}} = P \boldsymbol{\alpha}$ y $\boldsymbol{\bar{\beta}} = P \boldsymbol{\beta}$:
$$ \mathbf{x}(t) = e^{-tA} \boldsymbol{\bar{\alpha}} + e^{tA} \boldsymbol{\bar{\beta}} $$

Aplicando la condición en $t = 0$:
$$ \mathbf{x}(0) = \boldsymbol{\bar{\alpha}} + \boldsymbol{\bar{\beta}} = \mathbf{x}_0 \implies \boldsymbol{\bar{\alpha}} = \mathbf{x}_0 - \boldsymbol{\bar{\beta}} $$

Aplicando la condición en $t = 1$:
$$ \mathbf{x}(1) = e^{-A} \boldsymbol{\bar{\alpha}} + e^A \boldsymbol{\bar{\beta}} = \mathbf{x}_1 $$

Sustituyendo $\boldsymbol{\bar{\alpha}}$ en la ecuación anterior:
$$ e^{-A}(\mathbf{x}_0 - \boldsymbol{\bar{\beta}}) + e^A \boldsymbol{\bar{\beta}} = \mathbf{x}_1 \implies (e^A - e^{-A})\boldsymbol{\bar{\beta}} = \mathbf{x}_1 - e^{-A}\mathbf{x}_0 $$

Multiplicando a la izquierda por $e^A$:
$$ (e^{2A} - I)\boldsymbol{\bar{\beta}} = e^A \mathbf{x}_1 - \mathbf{x}_0 \implies (I - e^{2A})\boldsymbol{\bar{\beta}} = \mathbf{x}_0 - e^A \mathbf{x}_1 $$

Como los valores propios de $A$ son positivos ($\lambda_j > 0$), los valores propios de $e^{2A}$ son distintos de $1$. Por lo tanto, $(I - e^{2A})$ es invertible y podemos despejar $\boldsymbol{\bar{\beta}}$:
$$ \boldsymbol{\bar{\beta}} = (I - e^{2A})^{-1} [ \mathbf{x}_0 - e^A \mathbf{x}_1 ] $$

Sustituyendo de vuelta para obtener $\boldsymbol{\bar{\alpha}}$:
$$ \boldsymbol{\bar{\alpha}} = \mathbf{x}_0 - (I - e^{2A})^{-1} [ \mathbf{x}_0 - e^A \mathbf{x}_1 ] = (I - e^{2A})^{-1} e^A [ \mathbf{x}_1 - e^A \mathbf{x}_0 ] $$

**Solución:**
$$ \mathbf{x}(t) = e^{-tA} \boldsymbol{\bar{\alpha}} + e^{tA} \boldsymbol{\bar{\beta}} $$
donde $\boldsymbol{\bar{\alpha}} = (I - e^{2A})^{-1} e^A [ \mathbf{x}_1 - e^A \mathbf{x}_0 ]$ y $\boldsymbol{\bar{\beta}} = (I - e^{2A})^{-1} [ \mathbf{x}_0 - e^A \mathbf{x}_1 ]$.
