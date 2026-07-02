# Tema 2 — Integración Múltiple

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 15.

---

## 2.1 Integral Doble

$$\iint_R f(x,y)\, dA = \lim_{\|P\| \to 0} \sum_{i,j} f(x_{ij}^*, y_{ij}^*)\,\Delta A_{ij}$$

**Teorema de Fubini**: si $f$ es continua en el rectángulo $R = [a,b]\times[c,d]$:
$$\iint_R f\, dA = \int_a^b \int_c^d f(x,y)\, dy\, dx = \int_c^d \int_a^b f(x,y)\, dx\, dy$$

**Región tipo I** ($a \le x \le b$, $g_1(x) \le y \le g_2(x)$):
$$\iint_D f\, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y)\, dy\, dx$$

**Región tipo II** ($c \le y \le d$, $h_1(y) \le x \le h_2(y)$): análogo.

**Cambio de orden de integración**: dibujar la región, identificar si es tipo I o II, reescribir los límites.

---

## 2.2 Coordenadas Polares (2D)

$x = r\cos\theta$, $y = r\sin\theta$, $dA = r\, dr\, d\theta$.

$$\iint_D f(x,y)\, dA = \int_{\alpha}^{\beta} \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\, r\, dr\, d\theta$$

**Cuándo usar**: cuando $D$ tiene simetría circular o el integrando contiene $x^2+y^2$.

**No olvidar el $r$** del Jacobiano.

---

## 2.3 Integral Triple

$$\iiint_E f(x,y,z)\, dV$$

**Coordenadas cilíndricas**: $x = r\cos\theta$, $y = r\sin\theta$, $z = z$. $dV = r\, dr\, d\theta\, dz$.

**Coordenadas esféricas**: $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, $z = \rho\cos\phi$. $dV = \rho^2\sin\phi\, d\rho\, d\phi\, d\theta$.

| Sistema | Usar cuando |
|---|---|
| Rectangulares | Sólidos con caras planas |
| Cilíndricas | Simetría respecto al eje $z$, $x^2+y^2$ presente |
| Esféricas | $x^2+y^2+z^2$ presente, superficies esféricas |

**Rangos típicos en esféricas**: $\rho \ge 0$, $0 \le \theta \le 2\pi$, $0 \le \phi \le \pi$.

---

## 2.4 El Jacobiano — Cambio de Variables General

Para la transformación $(x,y) = T(u,v)$:
$$\iint_R f(x,y)\, dA = \iint_S f(T(u,v))\, \left|\frac{\partial(x,y)}{\partial(u,v)}\right|\, du\, dv$$

$$J = \frac{\partial(x,y)}{\partial(u,v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

**Los Jacobianos de coordenadas curvilíneas**:
- Polares: $|J| = r$
- Cilíndricas: $|J| = r$
- Esféricas: $|J| = \rho^2 \sin\phi$

---

## 2.5 Aplicaciones

**Volumen**: $V = \iiint_E dV$.

**Masa**: $m = \iiint_E \delta(x,y,z)\, dV$ donde $\delta$ es la densidad.

**Centro de masa**: $\bar{x} = \frac{1}{m}\iiint_E x\, \delta\, dV$ (análogo para $\bar{y}$, $\bar{z}$).

**Momentos de inercia**: $I_z = \iiint_E (x^2+y^2)\delta\, dV$.
