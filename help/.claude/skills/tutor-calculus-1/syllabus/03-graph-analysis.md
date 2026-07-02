# Tema 3 — Análisis Gráfico de Funciones

**Referencias**: Stewart, *Calculus: Early Transcendentals* (8th ed.), Ch. 4; Spivak, *Calculus*, Ch. 11.

---

## 3.1 Criterio de la Primera Derivada

- $f'(x) > 0$ en $(a,b)$ $\Rightarrow$ $f$ es **creciente** en $(a,b)$.
- $f'(x) < 0$ en $(a,b)$ $\Rightarrow$ $f$ es **decreciente** en $(a,b)$.

**Punto Crítico**: $c$ donde $f'(c) = 0$ o $f'(c)$ no existe.

**Test de la primera derivada en puntos críticos**:
- Si $f'$ cambia de $+$ a $-$ en $c$: **máximo local**.
- Si $f'$ cambia de $-$ a $+$ en $c$: **mínimo local**.
- Si no cambia de signo: ni máximo ni mínimo.

---

## 3.2 Criterio de la Segunda Derivada

- $f''(x) > 0$ en $(a,b)$ $\Rightarrow$ $f$ es **cóncava hacia arriba** en $(a,b)$.
- $f''(x) < 0$ en $(a,b)$ $\Rightarrow$ $f$ es **cóncava hacia abajo** en $(a,b)$.

**Punto de Inflexión**: donde $f''$ cambia de signo (la concavidad cambia).

**Test de la segunda derivada en puntos críticos**: si $f'(c) = 0$:
- $f''(c) > 0$ $\Rightarrow$ mínimo local.
- $f''(c) < 0$ $\Rightarrow$ máximo local.
- $f''(c) = 0$ $\Rightarrow$ test no concluyente (usar el de la primera derivada).

---

## 3.3 Extremos Absolutos

**Teorema de Weierstrass**: $f$ continua en $[a,b]$ alcanza su máximo y mínimo absolutos.

**Algoritmo para extremos en $[a,b]$**:
1. Encontrar todos los puntos críticos en $(a,b)$.
2. Evaluar $f$ en los puntos críticos y en los extremos $a$, $b$.
3. El mayor valor es el máximo absoluto; el menor, el mínimo absoluto.

**En intervalos abiertos o infinitos**: analizar el comportamiento en los extremos del dominio y comparar con los valores locales.

---

## 3.4 Asíntotas

**Vertical** $x = a$: $\lim_{x \to a^{\pm}} f(x) = \pm\infty$. Buscar donde el denominador se anula.

**Horizontal** $y = L$: $\lim_{x \to \pm\infty} f(x) = L$.

**Oblicua** $y = mx + b$:
$$m = \lim_{x \to \infty} \frac{f(x)}{x}, \qquad b = \lim_{x \to \infty}[f(x) - mx]$$
Solo existe cuando no hay asíntota horizontal.

---

## 3.5 Esquema de Análisis Completo

Para trazar o analizar $f$:

1. **Dominio**: dónde está definida.
2. **Simetrías**: ¿par ($f(-x)=f(x)$)? ¿impar ($f(-x)=-f(x)$)?
3. **Interceptos**: $f(0)$ (eje $y$), $f(x)=0$ (eje $x$).
4. **Asíntotas**: vertical, horizontal, oblicua.
5. **Crecimiento/decrecimiento**: signo de $f'$.
6. **Extremos locales**: puntos críticos + test.
7. **Concavidad**: signo de $f''$.
8. **Puntos de inflexión**: donde $f''$ cambia de signo.
9. **Extremos absolutos** (si el dominio es cerrado y acotado).
