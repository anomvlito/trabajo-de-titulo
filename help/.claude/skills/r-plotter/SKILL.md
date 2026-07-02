---
name: r-plotter
description: Generates statistical figures (boxplots, histograms, density plots) using R + ggplot2, saves as PDF in {root}/output/figures/, ready to embed in LaTeX via \includegraphics. Use for any statistical diagram that needs to look clean and professional.
---

# R Plotter

## When to use this skill

Use R instead of TikZ for:
- **Boxplot / diagrama de caja y bigotes** — ggplot2 handles quartiles, whiskers, and outliers automatically
- **Histograma con frecuencias** — when bars need to look polished
- **Density plot / curva de distribución**
- Any plot where precise geometric layout in TikZ would be tedious

Keep using TikZ for: Venn diagrams, probability trees (use mermaid-diagram instead), simple number lines.

---

## Output Convention

Always save to `{root}/output/figures/{name}.pdf` — PDF embeds in LaTeX without resolution loss.

```r
ggsave("{root}/output/figures/{name}.pdf",
       plot = p, width = W, height = H, device = "pdf")
```

Typical sizes:
- Boxplot horizontal: `width = 6.5, height = 2.6`
- Histogram: `width = 6, height = 3.5`
- Density: `width = 6, height = 3`

---

## Boxplot Template

```r
library(ggplot2)

datos <- c(...)   # vector of values, n observations
df <- data.frame(y = datos, x = "")

p <- ggplot(df, aes(x = x, y = y)) +
  geom_boxplot(
    width = 0.38, fill = "grey93", color = "black",
    linewidth = 0.55, outlier.shape = 16,
    outlier.size = 2.2, outlier.color = "black"
  ) +
  # Q labels — stagger to avoid overlap:
  # Q1 and Q3 above (x = 1.22), Q2 below (x = 0.72)
  annotate("text", x = 1.22, y = Q1, label = paste0("Q1 = ", Q1), size = 3.1) +
  annotate("text", x = 0.72, y = Q2, label = paste0("Q2 = ", Q2), size = 3.1) +
  annotate("text", x = 1.22, y = Q3, label = paste0("Q3 = ", Q3), size = 3.1) +
  # outlier labels (vjust = -0.9 puts label above the point)
  annotate("text", x = 1, y = outlier1, label = "val1", size = 2.8, vjust = -0.9) +
  labs(x = NULL, y = expression("Variable"~(units))) +
  scale_y_continuous(breaks = seq(min, max, by = step)) +
  coord_flip() +
  theme_classic(base_size = 12) +
  theme(
    axis.text.y        = element_blank(),
    axis.ticks.y       = element_blank(),
    axis.line.y        = element_blank(),
    panel.grid.major.x = element_line(color = "grey82", linewidth = 0.3)
  )
```

### Critical rules for boxplot annotations
- **Never use Unicode subscripts** (₁ ₂ ₃ ✱ etc.) — R's PDF device renders them as `...`. Use plain `Q1`, `Q2`, `Q3`.
- **Stagger Q1/Q2/Q3 labels** to avoid overlap: Q1 and Q3 on the upper side (`x = 1.22`), Q2 on the lower side (`x = 0.72`). Adjust if values are far apart.
- For outliers not in `datos`, add them manually with `annotate("point", ...)` + `annotate("text", ...)`.

---

## Embedding in LaTeX

After generating the PDF, add `\graphicspath{{figures/}}` to the LaTeX preamble (done once), then:

```latex
\begin{figure}[H]
  \centering
  \includegraphics[width=0.88\textwidth]{boxplot_bmu.pdf}
\end{figure}
```

No caption needed in exercise solutions — the surrounding text provides context.

---

## Calling from exercise-solver

When `exercise-solver` detects a boxplot or histogram exercise, it should:
1. Extract the data values from the image.
2. Call this skill with the data and computed statistics (Q1, Q2, Q3, outliers).
3. Use the generated PDF path when calling `latex-writer`.

---

## Constraints

- **Device must be `"pdf"`** for clean LaTeX embedding. Never PNG for boxplots/histograms (resolution issues).
- **`theme_classic()`** as base — removes gray background, keeps clean axis lines.
- **No Unicode** in labels or axis text.
- Save script to `/tmp/{name}.R` and run with `Rscript /tmp/{name}.R` — don't leave R scripts in the project directory.
