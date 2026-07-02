# Notación Matemática Compartida

Este archivo define las convenciones de notación que todos los tutores y `exercise-solver` deben seguir para producir documentos consistentes. Léelo siempre que vayas a generar o revisar LaTeX matemático.

---

## Análisis y Cálculo

| Concepto | Notación correcta | Notación a evitar |
|---|---|---|
| Diferencial | $dx$, $dy$ (sin `\text`) | $\text{d}x$ |
| Integral definida | $\int_a^b f(x)\, dx$ (espacio antes de $dx$) | $\int_a^b f(x)dx$ |
| Integral indefinida | $\int f(x)\, dx + C$ | Olvidar el $+C$ |
| Límite | $\lim_{x \to a} f(x)$ | $\lim_{x=a}$ |
| Límite al infinito | $\lim_{x \to \infty}$ | $\lim_{x \to +\infty}$ (salvo que se distinga de $-\infty$) |
| Derivada de orden $n$ | $f^{(n)}(x)$ | $f^n(x)$ |
| Derivada de Leibniz | $\frac{dy}{dx}$, $\frac{d^2y}{dx^2}$ | $\frac{d}{dx}y$ (en expresiones largas) |
| Derivada parcial | $\frac{\partial f}{\partial x}$ | $f_x$ solo en contextos informales |
| Evaluación | $\Big[F(x)\Big]_a^b$ | $F(x)\Big|_a^b$ (ambas aceptables, pero ser consistente) |
| Logaritmo natural | $\ln x$ | $\log x$ (reservar $\log$ para base 10 o base genérica) |
| Función exponencial | $e^x$ | $\exp(x)$ solo cuando el exponente es largo |

---

## Álgebra Lineal y Vectores

| Concepto | Notación correcta | Notación a evitar |
|---|---|---|
| Vectores | $\mathbf{v}$ (negrita) | $\vec{v}$ (solo en contexto de física/cálculo 2) |
| Norma | $\|\mathbf{v}\|$ | $|\mathbf{v}|$ |
| Producto punto | $\mathbf{u} \cdot \mathbf{v}$ | $\mathbf{u} \mathbf{v}$ |
| Producto cruz | $\mathbf{u} \times \mathbf{v}$ | $\mathbf{u} \wedge \mathbf{v}$ |
| Matriz | $A$, $B$ (mayúsculas) | $a$, $b$ |
| Transpuesta | $A^T$ | $A'$ |
| Determinante | $\det(A)$ o $|A|$ | $\|A\|$ |

---

## Probabilidad y Estadística

| Concepto | Notación correcta | Notación a evitar |
|---|---|---|
| Probabilidad | $P(A)$ | $\text{Pr}(A)$, $\mathbb{P}(A)$ |
| Probabilidad condicional | $P(A \mid B)$ (`\mid`) | $P(A\|B)$, $P(A/B)$ |
| Esperanza | $E[X]$ | $\mathbb{E}[X]$, $\mu_X$ (solo cuando sea claro) |
| Varianza | $\text{Var}(X)$ | $V(X)$, $\sigma^2_X$ (solo en contextos de parámetros) |
| Desviación estándar | $\sigma_X$ | $\text{SD}(X)$ |
| Distribución Normal | $X \sim N(\mu, \sigma^2)$ | $X \sim \mathcal{N}(\mu, \sigma^2)$ |
| CDF Normal estándar | $\Phi(z)$ | $F(z)$, $\Phi_0(z)$ |
| Estimador | $\hat{\theta}$ | $\tilde{\theta}$ (reservar para otros estimadores) |
| Muestra iid | $X_1, \ldots, X_n \overset{iid}{\sim} F$ | $X_i \sim F \; \forall i$ |
| Convergencia en prob. | $X_n \xrightarrow{P} X$ | $X_n \to^P X$ |
| Convergencia en dist. | $X_n \xrightarrow{d} X$ | $X_n \Rightarrow X$ |

---

## EDO

| Concepto | Notación correcta | Notación a evitar |
|---|---|---|
| Derivada respecto a $t$ | $\dot{y}$ (punto de Newton) o $y'$ | Mezclar ambas en el mismo documento |
| Solución general | $y = y_h + y_p$ | $y = y_c + y_p$ (ambas válidas; preferir $y_h$) |
| Transformada de Laplace | $\mathcal{L}\{f(t)\} = F(s)$ | $L\{f\}$ |
| Transformada inversa | $\mathcal{L}^{-1}\{F(s)\}$ | $L^{-1}\{F\}$ |
| Wronskiano | $W(y_1, y_2)(x)$ | $W[y_1, y_2]$ |

---

## Reglas Generales de LaTeX

- **Multiplicación**: usar `\cdot` en display math, nunca `*`.
- **Conjuntos numéricos**: `\mathbb{R}`, `\mathbb{N}`, `\mathbb{Z}`, `\mathbb{C}`.
- **Para todo / existe**: `\forall`, `\exists` (como símbolos, no escribir en texto).
- **Implica / si y solo si**: `\Rightarrow`, `\Leftrightarrow` en demostraciones; `\implies`, `\iff` en prosa.
- **Puntos suspensivos**: `\ldots` (en línea), `\cdots` (centrados), `\vdots` (vertical).
- **Texto en math mode**: `\text{...}` para palabras dentro de entornos matemáticos.
- **Alineación de derivaciones**: usar `align*` para cadenas de igualdades multi-línea.
