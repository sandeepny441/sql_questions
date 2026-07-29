# Modern Japanese Magazine Light Data Viz Theme

Use this as a generic design template for histograms, bar charts, grouped bars, stacked bars, line charts, scatter plots, heatmaps, dashboards, and presentation visuals.

The agent must use the exact colors below. Do not let the agent invent, substitute, randomize, or "improve" the palette.

## Theme Summary

Create a refined light editorial data visualization style inspired by modern Japanese magazine design: warm paper background, sumi-ink typography, quiet gridlines, generous whitespace, and curated accent colors that feel memorable without looking loud.

Avoid default Matplotlib, Excel, Tableau, Google Sheets, or corporate dashboard colors.

## Fixed Core Colors

Use these exactly.

| Role | Hex |
|---|---:|
| Canvas background | `#F6F2EA` |
| Plot background | `#FBF8F0` |
| Panel background | `#EFE9DD` |
| Title text | `#232323` |
| Axis text | `#3A3631` |
| Secondary text | `#6D675F` |
| Text on dark fills | `#F5F1E9` |
| Gridlines | `#D8D0C3` |
| Axis baseline | `#BEB5A7` |
| Divider line | `#E4DDD1` |

## Fixed Categorical Palette

Use this order for categorical series. Do not reorder unless a semantic rule below applies.

| Order | Name | Hex |
|---:|---|---:|
| 1 | Indigo | `#1E2F5F` |
| 2 | Beni red | `#C75F66` |
| 3 | Aotake green | `#4FA078` |
| 4 | Warm gold | `#D9AD45` |
| 5 | Fuji violet | `#7560A8` |
| 6 | Asagi teal | `#357C84` |
| 7 | Ume plum | `#9B4F74` |
| 8 | Moss olive | `#6D7F3F` |
| 9 | Clay | `#A66A54` |
| 10 | Blue gray | `#6F8FAF` |

If there are more than 10 categories, reuse the palette only after changing mark style, such as line dash, marker shape, or small multiples. Do not add new colors.

## Fixed Semantic Colors

Use these assignments when the data has meaning.

| Meaning | Hex |
|---|---:|
| Primary series | `#1E2F5F` |
| Secondary series | `#7560A8` |
| Positive / higher / growth | `#4FA078` |
| Negative / lower / risk | `#C75F66` |
| Neutral / middle / baseline | `#D9AD45` |
| Important highlight | `#C7A24A` |
| Critical emphasis | `#8B263B` |
| Optional comparison | `#357C84` |

## Fixed Two-Series Palette

For grouped bars, stacked bars, and two-line comparisons:

```text
Series A: #D9AD45
Series B: #7560A8
```

Use dark text on `#D9AD45`:

```text
#1F1B12
```

Use light text on `#7560A8`:

```text
#F5F1E9
```

## Fixed Three-Series Palette

For three pillars, three states, or three summary groups:

```text
Group 1: #C75F66
Group 2: #D9AD45
Group 3: #4FA078
```

If the middle group is a baseline or reference point:

```text
Group 1: #C75F66
Baseline group: #1E2F5F with #C7A24A outline
Group 3: #4FA078
```

## Fixed Diverging Palette

Use only when values move away from a center, target, or baseline.

```text
Negative side, far to near:
#7F263A
#A93C4C
#C95E61
#DF8280
#EFAAA2
#F7D5CE

Center:
#1E2F5F
Outline: #C7A24A

Positive side, near to far:
#DDECD4
#BFDDB8
#97C996
#6CAD78
#3F8F66
#1D6F5E
```

## Fixed Sequential Palettes

Use these for ordered buckets, heatmaps, density, or magnitude.

### Red Sequential

```text
#F7D5CE
#EFAAA2
#DF8280
#C95E61
#A93C4C
#7F263A
```

### Green Sequential

```text
#DDECD4
#BFDDB8
#97C996
#6CAD78
#3F8F66
#1D6F5E
```

### Indigo Sequential

```text
#DDE3F0
#AEBBDA
#7C8FC0
#4F67A0
#2F467C
#1E2F5F
```

## Chart Rules

- Use solid fills by default.
- Use gradients only when the data itself is sequential or diverging.
- Use warm ivory backgrounds, never pure white backgrounds.
- Use subtle gridlines, not heavy chart scaffolding.
- Remove unnecessary top, left, and right borders.
- Keep the x-axis baseline slightly stronger than the grid.
- Place legends inside the plot at top-left when space allows.
- Use generous spacing between grouped bars.
- Avoid labels inside very small bars; place them above the bar.
- Keep labels short: maximum two lines inside a mark.
- Round display percentages for presentation charts.
- If a chart shows a complete distribution, make displayed rounded percentages add to 100.

## Typography

Use one clean sans-serif font:

```text
Inter, Avenir, Helvetica Neue, Source Sans 3, or Noto Sans
```

Recommended sizes:

```text
Title: 22-28 pt
Subtitle: 11-13 pt
Axis labels: 10-12 pt
Tick labels: 9-11 pt
Bar labels: 10-12 pt
Callout totals: 14-20 pt
Legend: 10-12 pt
```

Do not use oversized data labels that overlap or dominate the chart.

## Prompt To Reuse

```text
Create the chart using the Modern Japanese Magazine Light Data Viz Theme.

Use only this exact palette:
Canvas #F6F2EA, plot background #FBF8F0, title #232323, axis text #3A3631, secondary text #6D675F, gridlines #D8D0C3, baseline #BEB5A7.

Categorical colors in order: #1E2F5F, #C75F66, #4FA078, #D9AD45, #7560A8, #357C84, #9B4F74, #6D7F3F, #A66A54, #6F8FAF.

Use solid fills by default. Use gradients only for ordered or diverging values, and only from the fixed sequential/diverging palettes. Do not invent new colors. Do not use default chart colors. Keep the chart refined, spacious, high-contrast, and presentation-ready.
```

