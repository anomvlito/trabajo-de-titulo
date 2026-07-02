# Tema 2 — Aplicaciones de la Integral

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 6, 8.

---

## 2.1 Área entre Curvas

**Entre $f$ y $g$ en $[a,b]$** (con $f(x) \ge g(x)$):
$$A = \int_a^b [f(x) - g(x)]\, dx$$

**Procedimiento cuando las curvas se cruzan**:
1. Encontrar puntos de intersección (resolver $f(x) = g(x)$).
2. Determinar cuál función es mayor en cada subintervalo.
3. Sumar las integrales de cada subintervalo con el valor absoluto de la diferencia.

**Integración respecto a $y$**: útil cuando las curvas se expresan mejor como $x = h(y)$:
$$A = \int_c^d [x_{\text{der}}(y) - x_{\text{izq}}(y)]\, dy$$

---

## 2.2 Volúmenes de Revolución

### Método de Discos/Arandelas (eje $x$)

Rotar $f(x)$ alrededor del eje $x$:
$$V = \pi \int_a^b [f(x)]^2\, dx$$

Arandela (hueco interior de radio $g(x) \le f(x)$):
$$V = \pi \int_a^b \left([f(x)]^2 - [g(x)]^2\right) dx$$

### Método de Cortezas Cilíndricas (eje $y$)

$$V = 2\pi \int_a^b x\, f(x)\, dx$$

**Regla mnemotécnica**: $V = 2\pi \int (\text{radio})(\text{altura})\, dx$.

**¿Cuándo usar cada método?**
- Discos/arandelas: más natural cuando los cortes son perpendiculares al eje de rotación.
- Cortezas: más natural cuando los cortes son paralelos al eje de rotación o cuando despejar la variable inversa sería complicado.

---

## 2.3 Longitud de Arco

Para $y = f(x)$ en $[a,b]$ (con $f'$ continua):
$$L = \int_a^b \sqrt{1 + [f'(x)]^2}\, dx$$

Para curva paramétrica $x = x(t)$, $y = y(t)$, $t \in [\alpha, \beta]$:
$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt$$

---

## 2.4 Área de Superficie de Revolución

Rotar $y = f(x)$ alrededor del eje $x$:
$$S = 2\pi \int_a^b f(x)\sqrt{1 + [f'(x)]^2}\, dx$$

---

## 2.5 Momentos y Centro de Masa

Para una placa plana con densidad uniforme $\rho$ delimitada por $f(x) \ge 0$ en $[a,b]$:

$$M_y = \rho \int_a^b x\, f(x)\, dx, \qquad M_x = \frac{\rho}{2} \int_a^b [f(x)]^2\, dx$$

$$\bar{x} = \frac{M_y}{m}, \qquad \bar{y} = \frac{M_x}{m}, \qquad m = \rho \int_a^b f(x)\, dx$$

---

## 2.6 Trabajo e Integrales Físicas

**Trabajo** con fuerza variable $F(x)$ a lo largo de $[a,b]$:
$$W = \int_a^b F(x)\, dx$$

**Ley de Hooke**: $F(x) = kx$ (resorte con constante $k$).

**Presión hidrostática**: $F = \rho g \int_a^b x\, w(x)\, dx$ donde $w(x)$ es el ancho de la placa a profundidad $x$.
