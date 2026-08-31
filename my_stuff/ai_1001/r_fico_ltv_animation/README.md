# FICO vs LTV Animated Scatter Plot

Animated visualization of mortgage credit risk characteristics (FICO score vs Loan-to-Value ratio) using **gganimate**.

## What This Shows

- **X-axis**: FICO credit score (585–848)
- **Y-axis**: Loan-to-Value ratio (51%–104%)
- **Color**: Credit risk segment (Super Prime → Subprime)
- **Size**: Loan amount
- **Animation**: Evolution by origination quarter (2023-Q1 → 2024-Q4)

The animation uses `shadow_mark()` so previous quarters remain visible (faded) while new loans appear each quarter. This illustrates how a mortgage portfolio's credit profile builds over time.

Reference lines mark common underwriting thresholds (FICO 620/680/720/760 and LTV 80/90/97%).

## Generated Outputs

| File | Description |
|------|-------------|
| `fico_ltv_animated.gif` | Main deliverable – 1200×780 px, ~10s loop |
| `fico_ltv_sample_data.csv` | 520-row synthetic dataset for reuse |
| `create_fico_ltv_animation.R` | Fully commented, reproducible R script |

## How to Run

### 1. Install R (if not already installed)

**macOS (Homebrew recommended):**
```bash
brew install r
```

**Other platforms:** Download from https://cran.r-project.org/

### 2. Install required R packages

Open R or RStudio and run:

```r
install.packages(c(
  "ggplot2",
  "gganimate",
  "dplyr",
  "gifski",      # GIF encoder (recommended)
  "scales"
))
```

For **MP4 video output** (higher quality, smaller files) also install:

```r
install.packages("av")           # requires ffmpeg
# macOS: brew install ffmpeg
```

### 3. Run the script

```bash
cd r_fico_ltv_animation
Rscript create_fico_ltv_animation.R
```

The script will:
- Generate synthetic but realistic data
- Print summary statistics
- Export `fico_ltv_sample_data.csv`
- Render and save `fico_ltv_animated.gif`

### 4. View the result

- Open `fico_ltv_animated.gif` in any browser, Preview, or media player
- In RStudio, you can also just run the script and the animation will preview in the Viewer pane

## Data Generation Details

The synthetic data mimics real mortgage origination patterns:

- **Negative correlation** between FICO and LTV (stronger borrowers put down more equity)
- **Time trend**: modest credit box tightening/recovery across 2023–2024 (higher avg FICO, slightly lower LTV in later quarters)
- **Risk segmentation** follows standard industry buckets:
  - Super Prime: FICO ≥ 760
  - Prime: 720–759
  - Near Prime: 680–719
  - Subprime: < 680
- **Volume ramp**: more loans originated in 2024 than early 2023
- Realistic ranges and outliers included

## Customization Ideas

Edit `create_fico_ltv_animation.R` and re-run:

- Change `n_loans` for larger/smaller sample
- Modify the `risk_colors` palette
- Add `facet_wrap(~purpose)` before `transition_states()`
- Switch to MP4: change `gifski_renderer(...)` to `av_renderer("output.mp4")`
- Use `transition_reveal(quarter_num)` instead of states for pure cumulative reveal

## Python Alternative (for comparison)

If you want a similar animation without installing R, see the sibling Python implementation using `plotly.express` (interactive HTML with scrubber) or `matplotlib.animation` (GIF export).

## Credits

Built with:
- [ggplot2](https://ggplot2.tidyverse.org/)
- [gganimate](https://gganimate.com/)
- Synthetic data inspired by Fannie Mae/Freddie Mac conventional loan guidelines

---

**Note**: All data is synthetic and generated for visualization/educational purposes only. No real borrower information is included.