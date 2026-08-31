from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "function_plots"

BG = "#f7f4ee"
AX_BG = "#fffdf9"
GRID = "#d7d0c2"
TEXT = "#1f2937"
SPINE = "#b9b1a2"

PALETTE = {
    "step": "#e76f51",
    "sigmoid": "#2a9d8f",
    "tanh": "#264653",
    "relu": "#f4a261",
    "leaky_relu": "#8b5cf6",
    "softmax_a": "#2563eb",
    "softmax_b": "#ef4444",
    "softmax_c": "#10b981",
    "logit": "#7c3aed",
    "probit": "#0f766e",
    "log_softmax_a": "#1d4ed8",
    "log_softmax_b": "#dc2626",
    "log_softmax_c": "#059669",
    "identity": "#111827",
}


def setup_style():
    plt.rcParams.update(
        {
            "figure.facecolor": BG,
            "axes.facecolor": AX_BG,
            "axes.edgecolor": SPINE,
            "axes.labelcolor": TEXT,
            "axes.titlecolor": TEXT,
            "xtick.color": TEXT,
            "ytick.color": TEXT,
            "text.color": TEXT,
            "font.family": "DejaVu Sans",
            "axes.titleweight": "bold",
            "axes.titlesize": 21,
            "axes.labelsize": 13,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
        }
    )


def configure_axes(ax, title, xlim=None, ylim=None, xlabel="Input", ylabel="Output"):
    ax.set_title(title, pad=16)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle="--", linewidth=0.8, color=GRID, alpha=0.9)
    ax.set_axisbelow(True)
    ax.axhline(0, color=SPINE, linewidth=1.1)
    ax.axvline(0, color=SPINE, linewidth=1.1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(SPINE)
    ax.spines["bottom"].set_color(SPINE)
    if xlim is not None:
        ax.set_xlim(*xlim)
    if ylim is not None:
        ax.set_ylim(*ylim)


def save_plot(fig, filename):
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=220, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def scalar_plot(title, x, y, color, filename, xlim=None, ylim=None, fill_to=0):
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, title, xlim=xlim, ylim=ylim)
    ax.plot(x, y, color=color, linewidth=3.5)
    ax.fill_between(x, y, fill_to, color=color, alpha=0.12)
    save_plot(fig, filename)


def make_step_plot():
    x = np.linspace(-6, 6, 600)
    y = (x >= 0).astype(float)
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, "Step Function", xlim=(-6, 6), ylim=(-0.15, 1.15))
    ax.step(x, y, where="post", color=PALETTE["step"], linewidth=3.5)
    ax.fill_between(x, y, 0, step="post", color=PALETTE["step"], alpha=0.14)
    save_plot(fig, "01_step_function.png")


def make_sigmoid_plot():
    x = np.linspace(-6, 6, 700)
    y = 1 / (1 + np.exp(-x))
    scalar_plot("Sigmoid", x, y, PALETTE["sigmoid"], "02_sigmoid.png", (-6, 6), (-0.05, 1.05))


def make_tanh_plot():
    x = np.linspace(-6, 6, 700)
    y = np.tanh(x)
    scalar_plot("Tanh", x, y, PALETTE["tanh"], "03_tanh.png", (-6, 6), (-1.1, 1.1))


def make_relu_plot():
    x = np.linspace(-6, 6, 700)
    y = np.maximum(0, x)
    scalar_plot("ReLU", x, y, PALETTE["relu"], "04_relu.png", (-6, 6), (-0.6, 6.6))


def make_leaky_relu_plot():
    x = np.linspace(-6, 6, 700)
    y = np.where(x >= 0, x, 0.1 * x)
    scalar_plot(
        "Leaky ReLU",
        x,
        y,
        PALETTE["leaky_relu"],
        "05_leaky_relu.png",
        (-6, 6),
        (-1.2, 6.6),
    )


def three_class_softmax(x):
    logits = np.stack([x, np.zeros_like(x), np.full_like(x, -2.0)], axis=1)
    shifted = logits - logits.max(axis=1, keepdims=True)
    exp_vals = np.exp(shifted)
    return exp_vals / exp_vals.sum(axis=1, keepdims=True)


def make_softmax_plot():
    x = np.linspace(-6, 6, 700)
    probs = three_class_softmax(x)
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, "Softmax", xlim=(-6, 6), ylim=(-0.02, 1.02), ylabel="Probability")
    ax.plot(x, probs[:, 0], color=PALETTE["softmax_a"], linewidth=3, label="Class A")
    ax.plot(x, probs[:, 1], color=PALETTE["softmax_b"], linewidth=3, label="Class B")
    ax.plot(x, probs[:, 2], color=PALETTE["softmax_c"], linewidth=3, label="Class C")
    ax.legend(frameon=False, loc="center left")
    save_plot(fig, "06_softmax.png")


def make_logit_plot():
    p = np.linspace(0.001, 0.999, 700)
    y = np.log(p / (1 - p))
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, "Logit", xlim=(0, 1), ylim=(-7.5, 7.5), xlabel="Probability")
    ax.plot(p, y, color=PALETTE["logit"], linewidth=3.5)
    ax.fill_between(p, y, 0, color=PALETTE["logit"], alpha=0.12)
    save_plot(fig, "07_logit.png")


def make_probit_plot():
    p = np.linspace(0.001, 0.999, 700)
    nd = NormalDist()
    y = np.array([nd.inv_cdf(value) for value in p])
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, "Probit", xlim=(0, 1), ylim=(-3.5, 3.5), xlabel="Probability")
    ax.plot(p, y, color=PALETTE["probit"], linewidth=3.5)
    ax.fill_between(p, y, 0, color=PALETTE["probit"], alpha=0.12)
    save_plot(fig, "08_probit.png")


def make_log_softmax_plot():
    x = np.linspace(-6, 6, 700)
    log_probs = np.log(three_class_softmax(x))
    fig, ax = plt.subplots(figsize=(9, 5.6))
    configure_axes(ax, "Log-softmax", xlim=(-6, 6), ylim=(-8.2, 0.2), ylabel="Log probability")
    ax.plot(x, log_probs[:, 0], color=PALETTE["log_softmax_a"], linewidth=3, label="Class A")
    ax.plot(x, log_probs[:, 1], color=PALETTE["log_softmax_b"], linewidth=3, label="Class B")
    ax.plot(x, log_probs[:, 2], color=PALETTE["log_softmax_c"], linewidth=3, label="Class C")
    ax.legend(frameon=False, loc="center left")
    save_plot(fig, "09_log_softmax.png")


def make_identity_plot():
    x = np.linspace(-6, 6, 700)
    y = x
    scalar_plot(
        "Linear / Identity",
        x,
        y,
        PALETTE["identity"],
        "10_linear_identity.png",
        (-6, 6),
        (-6.6, 6.6),
    )


def make_overview():
    files = [
        ("Step", "01_step_function.png"),
        ("Sigmoid", "02_sigmoid.png"),
        ("Tanh", "03_tanh.png"),
        ("ReLU", "04_relu.png"),
        ("Leaky ReLU", "05_leaky_relu.png"),
        ("Softmax", "06_softmax.png"),
        ("Logit", "07_logit.png"),
        ("Probit", "08_probit.png"),
        ("Log-softmax", "09_log_softmax.png"),
        ("Linear", "10_linear_identity.png"),
    ]
    fig, axes = plt.subplots(2, 5, figsize=(18, 8), facecolor=BG)
    for ax, (label, filename) in zip(axes.ravel(), files):
        image = plt.imread(OUTPUT_DIR / filename)
        ax.imshow(image)
        ax.set_title(label, fontsize=13, pad=8, color=TEXT)
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "overview.png", dpi=180, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    setup_style()
    make_step_plot()
    make_sigmoid_plot()
    make_tanh_plot()
    make_relu_plot()
    make_leaky_relu_plot()
    make_softmax_plot()
    make_logit_plot()
    make_probit_plot()
    make_log_softmax_plot()
    make_identity_plot()
    make_overview()
    print(f"Created plots in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
