#!/usr/bin/env python3
"""
Animated scatter plot of FICO vs LTV using matplotlib + PillowWriter.

This produces a traditional animated GIF (similar to what gganimate outputs).
It is fully self-contained and requires no browser.

The animation style mirrors the gganimate version:
- Points fade in for the current quarter
- Previous quarters remain visible as low-opacity shadows (portfolio build-up)
- Smooth transitions between quarters
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

# Load data
df = pd.read_csv("fico_ltv_sample_data.csv")
quarters = ["2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4",
            "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4"]

# Color map (matches R + Plotly)
colors = {
    "Super Prime": "#1a9850",
    "Prime":       "#91cf60",
    "Near Prime":  "#fc8d59",
    "Subprime":    "#d73027"
}

# Prepare figure with nice proportions
fig, ax = plt.subplots(figsize=(11.5, 7.8), dpi=110)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Fixed axis limits
ax.set_xlim(575, 855)
ax.set_ylim(48, 107)

# Reference lines (underwriting thresholds)
for x in [620, 680, 720, 760]:
    ax.axvline(x, color="#777777", linestyle=":", linewidth=0.9, alpha=0.55, zorder=0)
for y in [80, 90, 97]:
    ax.axhline(y, color="#777777", linestyle=":", linewidth=0.9, alpha=0.55, zorder=0)

# Small labels for thresholds
ax.text(622, 49.2, "620", fontsize=8.5, color="#555555", ha="left")
ax.text(682, 49.2, "680", fontsize=8.5, color="#555555", ha="left")
ax.text(722, 49.2, "720", fontsize=8.5, color="#555555", ha="left")
ax.text(762, 49.2, "760", fontsize=8.5, color="#555555", ha="left")
ax.text(577, 80.7, "80% LTV", fontsize=8, color="#555555", rotation=90, va="bottom")
ax.text(577, 90.7, "90% LTV", fontsize=8, color="#555555", rotation=90, va="bottom")

# Axis labels and title
ax.set_xlabel("FICO Credit Score", fontsize=12, fontweight="medium", labelpad=8)
ax.set_ylabel("Loan-to-Value Ratio (%)", fontsize=12, fontweight="medium", labelpad=8)
ax.set_title(
    "FICO Score vs. Loan-to-Value Ratio by Origination Quarter\n"
    "Mortgage Portfolio Evolution (Synthetic Data)",
    fontsize=15, fontweight="bold", pad=14
)

# Grid
ax.grid(True, linestyle="-", linewidth=0.4, alpha=0.35, color="#aaaaaa")
ax.set_axisbelow(True)

# Tick formatting
ax.set_xticks(range(600, 860, 40))
ax.set_yticks(range(50, 110, 10))
ax.set_yticklabels([f"{y}%" for y in range(50, 110, 10)])

# Legend elements (will be added after first draw)
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Super Prime"],
           markersize=9, label="Super Prime (≥760)"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Prime"],
           markersize=9, label="Prime (720-759)"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Near Prime"],
           markersize=9, label="Near Prime (680-719)"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor=colors["Subprime"],
           markersize=9, label="Subprime (<680)"),
]

# Text objects that will be updated each frame
quarter_text = ax.text(0.98, 0.96, "", transform=ax.transAxes,
                       fontsize=14, fontweight="bold", ha="right", va="top",
                       bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                                 edgecolor="#cccccc", alpha=0.95))
count_text = ax.text(0.98, 0.88, "", transform=ax.transAxes,
                     fontsize=10, ha="right", va="top", color="#444444")
caption = ax.text(0.01, -0.065, 
                  "Point size = Loan Amount   •   Dotted lines = common underwriting thresholds   •   Previous quarters shown faded",
                  transform=ax.transAxes, fontsize=8.5, color="#555555", va="top")

# Storage for scatter artists so we can remove them each frame
scatter_artists = []

def update(frame_idx):
    """Redraw all artists for the given quarter index."""
    global scatter_artists
    
    # Remove previous scatter objects
    for art in scatter_artists:
        art.remove()
    scatter_artists.clear()
    
    q = quarters[frame_idx]
    current = df[df["quarter"] == q]
    previous = df[df["quarter_num"] < (frame_idx + 1)]
    
    # Draw "shadow" points for all previous quarters (low opacity, small)
    if len(previous) > 0:
        for seg in ["Super Prime", "Prime", "Near Prime", "Subprime"]:
            sub = previous[previous["risk_segment"] == seg]
            if len(sub) == 0:
                continue
            # Scale size down a bit for shadows
            sizes = np.sqrt(sub["loan_amount"] / 18000) + 1.5
            sc = ax.scatter(
                sub["fico"], sub["ltv"],
                s=sizes,
                c=colors[seg],
                alpha=0.13,
                edgecolors="none",
                zorder=1
            )
            scatter_artists.append(sc)
    
    # Draw current quarter's points (full opacity, normal size)
    for seg in ["Super Prime", "Prime", "Near Prime", "Subprime"]:
        sub = current[current["risk_segment"] == seg]
        if len(sub) == 0:
            continue
        # Size mapping similar to Plotly/gganimate
        sizes = np.sqrt(sub["loan_amount"] / 12000) + 4.5
        sc = ax.scatter(
            sub["fico"], sub["ltv"],
            s=sizes,
            c=colors[seg],
            alpha=0.82,
            edgecolors="#222222",
            linewidths=0.25,
            zorder=3
        )
        scatter_artists.append(sc)
    
    # Update dynamic text
    quarter_text.set_text(q)
    count_text.set_text(f"{len(previous) + len(current):,} loans cumulative")
    
    return scatter_artists + [quarter_text, count_text]

# Initial draw (first frame)
update(0)

# Add legend
ax.legend(handles=legend_elements, loc="lower right", framealpha=0.96,
          fontsize=9.5, title="Credit Segment", title_fontsize=10)

# Tight layout
plt.tight_layout(rect=[0, 0.03, 1, 0.97])

# Create the animation
# 8 quarters → we do 2 frames per quarter transition + hold frames
frames_per_quarter = 11
total_frames = len(quarters) * frames_per_quarter

def frame_generator():
    """Yield quarter indices with hold frames for smoother viewing."""
    for qi in range(len(quarters)):
        for _ in range(frames_per_quarter):
            yield qi

anim = FuncAnimation(
    fig,
    update,
    frames=frame_generator(),
    interval=70,          # ms between frames (~14 fps)
    blit=False,
    repeat=True,
    repeat_delay=1200
)

# Save as GIF using Pillow
output_gif = "fico_ltv_animated_matplotlib.gif"
writer = PillowWriter(fps=13, metadata=dict(artist="matplotlib"))
anim.save(output_gif, writer=writer, dpi=110)

print(f"✓ Matplotlib GIF animation saved to: {output_gif}")
print(f"  Total frames: {total_frames}  |  ~{total_frames/13:.1f} seconds at 13 fps")
print("  File is viewable in browsers, Preview, Slack, etc.")

# Also save the final frame as a high-quality static PNG
plt.savefig("fico_ltv_matplotlib_final_frame.png", dpi=160, bbox_inches="tight")
print("✓ Final frame PNG saved to: fico_ltv_matplotlib_final_frame.png")

plt.close()