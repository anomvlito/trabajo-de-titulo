# Ejercicio: Teorema de Comparación de Sturm e Identidades del Wronskiano

**Problema:**
Sean las ecuaciones diferenciales lineales de segundo orden:
\begin{align}
  -y'' &= f(x)y \\
  -z'' &= g(x)z
\end{align}
donde $f$ y $g$ son continuas en el intervalo $[a, b]$, con $f(x) \ge g(x)$, $\forall x \in [a, b]$.
Sean $y_1(x)$ y $z_1(x)$ soluciones de (1) y (2) en $[a, b]$, respectivamente. Asumiendo que $z_1$ es tal que: $z_1(a) = z_1(b) = 0$ y $z_1(x) \neq 0$ en el abierto $(a, b)$.
Probar que, o bien existe $x_0 \in (a, b)$ tal que $y_1(x_0) = 0$, o bien $f(x) = g(x)$ en $[a, b]$ y las soluciones son proporcionales ($y_1(x) = C z_1(x)$).

---
**Desarrollo:**

Supongamos que la primera alternativa no ocurre, es decir, que no existe ningún punto $x_0 \in (a, b)$ tal que $y_1(x_0) = 0$.
Por ser $y_1$ continua en $[a, b]$, esto implica que $y_1$ conserva su signo constante en el intervalo abierto $(a, b)$.
Sin pérdida de generalidad, asumamos que $y_1(x) > 0$ y $z_1(x) > 0$ para todo $x \in (a, b)$.
Por continuidad, en las fronteras se cumple:
$$ y_1(a) \ge 0, \quad y_1(b) \ge 0, \quad z_1(a) = z_1(b) = 0 $$

Dado que $z_1(x) > 0$ en el abierto y se anula en los extremos, se tiene de forma estricta que las pendientes en los extremos satisfacen:
$$ z_1'(a) > 0 \quad \text{y} \quad z_1'(b) < 0 $$

Definimos el Wronskiano de ambas soluciones:
$$ W(x) = W[y_1, z_1](x) = y_1(x) z_1'(x) - z_1(x) y_1'(x) $$

Derivando con respecto a $x$:
$$ W'(x) = y_1 z_1'' + y_1' z_1' - z_1' y_1' - z_1 y_1'' = y_1 z_1'' - z_1 y_1'' $$

Sustituyendo $y_1'' = -f(x)y_1$ y $z_1'' = -g(x)z_1$ desde las EDOs (1) y (2):
$$ W'(x) = y_1 (-g(x)z_1) - z_1 (-f(x)y_1) = (f(x) - g(x)) y_1(x) z_1(x) $$

Como $f(x) \ge g(x) \implies f(x) - g(x) \ge 0$ en $[a, b]$, y dado que $y_1(x) > 0$ y $z_1(x) > 0$ en el abierto $(a, b)$:
$$ W'(x) \ge 0 \quad \forall x \in (a, b) $$

Integrando respecto a $x$ a ambos lados en el intervalo $[a, b]$:
$$ \int_a^b W'(x) \, dx = W(b) - W(a) = \int_a^b (f(x) - g(x)) y_1(x) z_1(x) \, dx \ge 0 $$

Evaluando el Wronskiano en los límites de integración $x = a$ y $x = b$:
$$ W(a) = y_1(a) z_1'(a) - 0 \cdot y_1'(a) = y_1(a) z_1'(a) $$
$$ W(b) = y_1(b) z_1'(b) - 0 \cdot y_1'(b) = y_1(b) z_1'(b) $$

Analizando los signos de estos términos en las fronteras:
* En $x = a$: $W(a) \ge 0$ (ya que $y_1(a) \ge 0$ y $z_1'(a) > 0$).
* En $x = b$: $W(b) \le 0$ (ya que $y_1(b) \ge 0$ y $z_1'(b) < 0$).

Restando ambas relaciones:
$$ W(b) - W(a) \le 0 $$

Para que se cumplan las dos desigualdades obtenidas:
$$ W(b) - W(a) = 0 \implies W(b) = 0 \quad \text{y} \quad W(a) = 0 $$

Dado que $z_1'(a) > 0$ y $z_1'(b) < 0$, esto exige que:
$$ y_1(a) = 0 \quad \text{y} \quad y_1(b) = 0 $$

Reemplazando en la integral definida obtenemos:
$$ \int_a^b (f(x) - g(x)) y_1(x) z_1(x) \, dx = 0 $$

Como el integrando es continuo y no negativo, debe ser idénticamente nulo en todo $[a, b]$. Puesto que $y_1(x) z_1(x) > 0$ en $(a, b)$, concluimos:
$$ f(x) - g(x) = 0 \implies f(x) = g(x) \quad \forall x \in [a, b] $$

Al ser las dos ecuaciones diferenciales idénticas y tener las mismas condiciones de frontera homogéneas, por el teorema de unicidad concluimos la dependencia lineal de las soluciones:
$$ y_1(x) = C z_1(x) $$

**Solución:**
Queda demostrado que, o bien existe $x_0 \in (a, b)$ tal que $y_1(x_0) = 0$, o bien $f(x) = g(x)$ en $[a, b]$ e $y_1(x) = C z_1(x)$.
