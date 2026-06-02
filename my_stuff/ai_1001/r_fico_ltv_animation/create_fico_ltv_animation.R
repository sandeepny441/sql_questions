# ==============================================================================
# FICO Score vs LTV Animated Scatter Plot
# Using gganimate for mortgage origination data visualization
# ==============================================================================
#
# This script generates realistic synthetic mortgage data and creates a smooth
# animated scatter plot showing how FICO/LTV distributions evolve over time
# (by origination quarter).
#
# REQUIREMENTS:
#   R >= 4.2
#   Packages: ggplot2, gganimate, dplyr, gifski (for GIF) or av (for MP4)
#
# INSTALLATION (run once):
#   install.packages(c("ggplot2", "gganimate", "dplyr", "gifski", "scales"))
#
# For MP4 output instead of GIF, also: install.packages("av")
#   and install ffmpeg:  brew install ffmpeg   (macOS)
#
# USAGE:
#   Rscript create_fico_ltv_animation.R
#
# OUTPUTS:
#   - fico_ltv_animated.gif   (main deliverable)
#   - fico_ltv_sample_data.csv
#   - fico_ltv_static_preview.png  (optional, requires ggimage or similar)
#
# ==============================================================================

suppressPackageStartupMessages({
  library(ggplot2)
  library(gganimate)
  library(dplyr)
  library(scales)
})

# -----------------------------
# Configuration
# -----------------------------
set.seed(2024)                    # Reproducible results
n_loans <- 520                    # Sample size
output_gif <- "fico_ltv_animated.gif"
output_csv <- "fico_ltv_sample_data.csv"
width_px  <- 1200
height_px <- 780
fps       <- 14
nframes   <- 140                  # ~10 seconds at 14 fps

# -----------------------------
# Generate realistic synthetic mortgage data
# -----------------------------
# FICO ranges (typical for conventional loans): 580-850
# LTV ranges: 50-105 (high LTV allowed with mortgage insurance)

quarters <- c("2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4",
              "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4")

# Base generation with negative correlation (higher FICO → modestly lower LTV)
raw <- tibble(
  loan_id = sprintf("LN%06d", 1:n_loans),
  fico_base = rnorm(n_loans, mean = 726, sd = 48),
  ltv_base  = rnorm(n_loans, mean = 82.5, sd = 10.8)
) %>%
  mutate(
    # Realistic clipping
    fico = pmax(585, pmin(848, round(fico_base))),
    ltv  = pmax(51,  pmin(104, round(ltv_base))),
    # Introduce correlation: every 10 point FICO increase → ~0.35% lower LTV on avg
    ltv = pmax(51, pmin(104, round(ltv - 0.034 * (fico - 720) + rnorm(n_loans, 0, 6.8))))
  )

# Assign origination quarters with realistic volume ramp + credit quality shift
# Later quarters show modest improvement in credit box (higher FICO, lower LTV)
raw <- raw %>%
  mutate(
    # Weighted sampling: more volume in 2024
    q_prob = case_when(
      row_number() <= n_loans * 0.38 ~ sample(1:4, n(), replace = TRUE, prob = c(0.22, 0.24, 0.26, 0.28)),
      TRUE ~ sample(5:8, n(), replace = TRUE, prob = c(0.20, 0.23, 0.27, 0.30))
    ),
    quarter = factor(quarters[q_prob], levels = quarters),
    quarter_num = as.integer(quarter)
  )

# Apply time-based distribution shift (illustrative of market conditions)
data <- raw %>%
  group_by(quarter) %>%
  mutate(
    # Progressive tightening / recovery in credit standards through 2023-2024
    fico_shift = (quarter_num - 4.5) * 1.35,
    ltv_shift  = (quarter_num - 4.5) * -0.55,
    fico = pmax(585, pmin(848, round(fico + fico_shift + rnorm(n(), 0, 4)))),
    ltv  = pmax(51,  pmin(104, round(ltv  + ltv_shift  + rnorm(n(), 0, 3.5))))
  ) %>%
  ungroup() %>%
  mutate(
    # Credit risk segments (common industry buckets)
    risk_segment = case_when(
      fico >= 760 ~ "Super Prime",
      fico >= 720 ~ "Prime",
      fico >= 680 ~ "Near Prime",
      TRUE        ~ "Subprime"
    ),
    risk_segment = factor(risk_segment,
                          levels = c("Super Prime", "Prime", "Near Prime", "Subprime")),

    # Loan size for point sizing (typical conventional range)
    loan_amount = round(rnorm(n_loans, mean = 298000, sd = 112000)),
    loan_amount = pmax(92000, pmin(685000, loan_amount)),

    # Optional: purchase vs refinance flag (affects typical LTV)
    purpose = sample(c("Purchase", "Refinance"), n_loans, replace = TRUE,
                     prob = c(0.61, 0.39))
  ) %>%
  select(loan_id, fico, ltv, quarter, quarter_num, risk_segment, loan_amount, purpose)

# Quick summary printed to console
cat("\n=== Synthetic Mortgage Dataset Summary ===\n")
print(summary(data[, c("fico", "ltv", "loan_amount")]))
cat("\nRisk segment distribution:\n")
print(table(data$risk_segment))
cat("\nLoans per quarter:\n")
print(table(data$quarter))

# Export CSV for reproducibility / further analysis
write.csv(data, output_csv, row.names = FALSE)
cat("\n✓ Sample data exported to:", output_csv, "\n")

# -----------------------------
# Build the animated ggplot
# -----------------------------
# Color palette: green (low risk) → yellow → orange → red (higher risk)
risk_colors <- c(
  "Super Prime" = "#1a9850",   # dark green
  "Prime"       = "#91cf60",   # light green
  "Near Prime"  = "#fc8d59",   # orange
  "Subprime"    = "#d73027"    # red
)

# Reference lines for underwriting guidelines (common conventional thresholds)
fico_lines <- c(620, 680, 720, 760)
ltv_lines  <- c(80, 90, 97)

p <- ggplot(data, aes(x = fico, y = ltv)) +
  # Faint background points (all quarters) using shadow_mark later
  # Main points
  geom_point(
    aes(color = risk_segment, size = loan_amount),
    alpha = 0.72,
    stroke = 0.25
  ) +
  # Reference lines (underwriting guardrails)
  geom_vline(xintercept = fico_lines, linetype = "dotted",
             color = "gray45", alpha = 0.55, linewidth = 0.45) +
  geom_hline(yintercept = ltv_lines, linetype = "dotted",
             color = "gray45", alpha = 0.55, linewidth = 0.45) +
  # Small labels for reference lines (only drawn once, not animated)
  annotate("text", x = 622, y = 48.5, label = "620", size = 3.1,
           color = "gray40", hjust = 0) +
  annotate("text", x = 682, y = 48.5, label = "680", size = 3.1,
           color = "gray40", hjust = 0) +
  annotate("text", x = 722, y = 48.5, label = "720", size = 3.1,
           color = "gray40", hjust = 0) +
  annotate("text", x = 762, y = 48.5, label = "760", size = 3.1,
           color = "gray40", hjust = 0) +
  annotate("text", x = 577, y = 80.8, label = "80% LTV", size = 3.0,
           color = "gray40", hjust = 0, angle = 90, vjust = -0.3) +
  annotate("text", x = 577, y = 90.8, label = "90% LTV", size = 3.0,
           color = "gray40", hjust = 0, angle = 90, vjust = -0.3) +
  # Scales
  scale_x_continuous(
    limits = c(575, 855),
    breaks = seq(600, 840, by = 40),
    labels = comma_format()
  ) +
  scale_y_continuous(
    limits = c(48, 107),
    breaks = seq(50, 100, by = 10),
    labels = function(x) paste0(x, "%")
  ) +
  scale_color_manual(values = risk_colors, name = "Credit Segment") +
  scale_size_continuous(
    range = c(1.6, 7.8),
    guide = "none"   # size legend is noisy; we explain in caption
  ) +
  # Labels and theming
  labs(
    title = "FICO Score vs. Loan-to-Value Ratio by Origination Quarter",
    subtitle = "Quarter: {closest_state}   •   Loans shown: {n}   •   Point size = Loan Amount",
    x = "FICO Credit Score",
    y = "Loan-to-Value Ratio (LTV)",
    caption = paste0(
      "Synthetic data generated for illustration | ",
      "n = ", nrow(data), " loans | ",
      "Dotted lines = common underwriting thresholds\n",
      "Animation built with gganimate + ggplot2"
    )
  ) +
  theme_minimal(base_size = 13) +
  theme(
    plot.title = element_text(face = "bold", size = 18, margin = margin(b = 6)),
    plot.subtitle = element_text(size = 14, color = "gray25", margin = margin(b = 10)),
    plot.caption = element_text(size = 9.5, color = "gray40", margin = margin(t = 12)),
    legend.position = "right",
    legend.title = element_text(face = "bold", size = 11),
    legend.text = element_text(size = 10.5),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray88", linewidth = 0.35),
    axis.title = element_text(face = "bold", size = 12),
    axis.text = element_text(size = 10.5),
    plot.margin = margin(18, 22, 14, 16)
  ) +
  guides(color = guide_legend(override.aes = list(size = 4.5, alpha = 0.9)))

# -----------------------------
# Add animation layers (gganimate)
# -----------------------------
# Strategy:
# - transition_states by quarter (smooth interpolation between quarters)
# - shadow_mark keeps prior quarters visible at low opacity (portfolio build-up)
# - enter_fade + exit_fade for elegant appearance/disappearance of new points
# - ease_aes for natural motion

anim_plot <- p +
  transition_states(
    quarter,
    transition_length = 2.2,
    state_length = 1.6,
    wrap = FALSE
  ) +
  enter_fade(alpha = 0.0) +
  exit_fade(alpha = 0.0) +
  shadow_mark(
    alpha = 0.16,
    size = 2.1,
    color = "gray55",
    fill = NA
  ) +
  ease_aes("cubic-in-out")

# -----------------------------
# Render and save the animation
# -----------------------------
cat("\nRendering animation (this may take 20-60 seconds)...\n")

anim <- animate(
  anim_plot,
  nframes = nframes,
  fps = fps,
  width = width_px,
  height = height_px,
  res = 110,                    # DPI-ish for text sharpness
  renderer = gifski_renderer(output_gif, loop = TRUE),
  device = "png",               # higher quality than default
  type = "cairo"                # best font rendering on macOS
)

cat("✓ Animation saved to:", output_gif, "\n")
cat("  Dimensions:", width_px, "x", height_px, "px @", fps, "fps\n")
cat("  Total frames:", nframes, "\n\n")

# Optional: also save last frame as static preview (using anim_save or just ggsave on p with last state)
# gganimate makes it easy to save any specific frame:
# anim_save("fico_ltv_final_frame.png", animation = animate(p + transition_states(quarter) + ... , nframes=1, ...))

cat("Done! Open", output_gif, "to view the animation.\n")
cat("Tip: In RStudio you can also just print(anim) to preview in the viewer.\n")

# ==============================================================================
# ADVANCED VARIANTS (uncomment to experiment)
# ==============================================================================
#
# 1) Cumulative only (no fading of old points, just new ones appearing):
#    Remove shadow_mark and use transition_reveal(quarter_num) instead.
#
# 2) MP4 video output (better quality, smaller file):
#    install.packages("av")
#    Then: renderer = av_renderer("fico_ltv_animated.mp4")
#
# 3) Highlight only the *new* loans each quarter (previous quarters grayed):
#    Add a column `is_new = TRUE` for the current state and map alpha to it.
#
# 4) Faceted by purpose (Purchase vs Refinance):
#    Add + facet_wrap(~purpose) before the transition_states layer.
#
# 5) Add dynamic stats text (avg FICO per quarter):
#    Precompute quarterly means and use geom_text with the same transition.
#
# ==============================================================================