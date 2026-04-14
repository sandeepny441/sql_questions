from __future__ import annotations

import random

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp


# -------------------------------------------------------------------
# Notebook-style inputs
# -------------------------------------------------------------------

df = pd.read_csv("dummy_nmls_values.csv")

MATCH_FEATURES = [
    "pro_score",
    "uwm_production",
    "overall_production",
    "conv_mix",
    "fha_mix",
    "va_mix",
    "purchase_pct",
    "total_ytd_closings",
]

CALIPERS = {
    "pro_score": 1.15,
    "overall_production": 1.65,
    "purchase_pct": 1.3,
    "total_ytd_closings": 1.35,
    "__pair_distance__": 3.1,
}

UNMATCHED_PENALTY = 1000.0
SEED = 42

UPLOAD_COLUMNS = [
    "nmls",
    "assignment",
    "pro_ranking",
    "pro_score",
    "uwm_production",
    "overall_production",
    "conv_mix",
    "fha_mix",
    "va_mix",
    "purchase_pct",
    "refi_pct",
    "total_ytd_closings",
    "jan_closings",
    "feb_closings",
    "march_closings",
    "pair_distance",
    "twin_nmls",
    "plot_x",
    "plot_y",
    "pair_id",
    "match_score",
]


# -------------------------------------------------------------------
# Standardize the matching features
# -------------------------------------------------------------------

scaled_df = df.copy()
for col in MATCH_FEATURES:
    mean = scaled_df[col].mean()
    std = scaled_df[col].std(ddof=0)
    scaled_df[col] = 0.0 if std == 0 else (scaled_df[col] - mean) / std


# -------------------------------------------------------------------
# Exact MILP solver for one rank bucket
# -------------------------------------------------------------------

def solve_bucket_exact(bucket_indices: list[int], edge_list: list[tuple[int, int, float]]) -> tuple[list[tuple[int, int, float]], list[int]]:
    nodes = list(bucket_indices)
    node_to_pos = {node: pos for pos, node in enumerate(nodes)}
    n_nodes = len(nodes)
    n_edges = len(edge_list)
    n_vars = n_edges + n_nodes

    objective = np.zeros(n_vars, dtype=float)
    integrality = np.ones(n_vars, dtype=int)
    lower = np.zeros(n_vars, dtype=float)
    upper = np.ones(n_vars, dtype=float)

    for edge_pos, (i, j, distance) in enumerate(edge_list):
        objective[edge_pos] = distance + (1e-8 * (node_to_pos[i] + node_to_pos[j]))

    objective[n_edges:] = UNMATCHED_PENALTY

    constraint_matrix = np.zeros((n_nodes, n_vars), dtype=float)
    for edge_pos, (i, j, _) in enumerate(edge_list):
        constraint_matrix[node_to_pos[i], edge_pos] = 1.0
        constraint_matrix[node_to_pos[j], edge_pos] = 1.0

    for node, pos in node_to_pos.items():
        constraint_matrix[pos, n_edges + pos] = 1.0

    result = milp(
        c=objective,
        integrality=integrality,
        bounds=Bounds(lower, upper),
        constraints=LinearConstraint(constraint_matrix, lb=np.ones(n_nodes), ub=np.ones(n_nodes)),
    )

    if not result.success or result.x is None:
        raise RuntimeError(f"MILP did not converge for bucket with {n_nodes} rows: {result.message}")

    chosen_edges = [edge for edge_pos, edge in enumerate(edge_list) if result.x[edge_pos] > 0.5]
    unmatched_nodes = [node for node, pos in node_to_pos.items() if result.x[n_edges + pos] > 0.5]
    return chosen_edges, unmatched_nodes


# -------------------------------------------------------------------
# Build candidate edges inside each exact pro_ranking bucket
# -------------------------------------------------------------------

rng = random.Random(SEED)
matched_pairs: list[dict[str, object]] = []
outlier_indices: list[int] = []

for pro_ranking, bucket_df in df.groupby("pro_ranking", sort=True):
    bucket_indices = bucket_df.index.tolist()
    edge_list: list[tuple[int, int, float]] = []

    for offset, i in enumerate(bucket_indices):
        for j in bucket_indices[offset + 1:]:
            diff = scaled_df.loc[i, MATCH_FEATURES].to_numpy(dtype=float) - scaled_df.loc[j, MATCH_FEATURES].to_numpy(dtype=float)
            distance = float(np.sqrt(np.sum(np.square(diff))))

            if distance > CALIPERS["__pair_distance__"]:
                continue

            keep_edge = True
            for feature, limit in CALIPERS.items():
                if feature == "__pair_distance__":
                    continue
                feature_gap = abs(float(scaled_df.loc[i, feature]) - float(scaled_df.loc[j, feature]))
                if feature_gap > limit:
                    keep_edge = False
                    break

            if keep_edge:
                edge_list.append((i, j, distance))

    chosen_edges, unmatched_nodes = solve_bucket_exact(bucket_indices, edge_list)

    for i, j, distance in chosen_edges:
        control_idx, treatment_idx = (i, j) if rng.random() < 0.5 else (j, i)
        matched_pairs.append(
            {
                "pair_distance": float(distance),
                "control_idx": control_idx,
                "treatment_idx": treatment_idx,
                "pro_ranking": pro_ranking,
            }
        )

    outlier_indices.extend(unmatched_nodes)

matched_pairs.sort(key=lambda pair: pair["pair_distance"])
for pair_id, pair in enumerate(matched_pairs, start=1):
    pair["pair_id"] = pair_id

outlier_indices.sort(key=lambda idx: (df.loc[idx, "pro_ranking"], int(df.loc[idx, "nmls"])))


# -------------------------------------------------------------------
# Pair-level match score
# -------------------------------------------------------------------

pair_distances = [float(pair["pair_distance"]) for pair in matched_pairs]
if pair_distances:
    min_distance = min(pair_distances)
    max_distance = max(pair_distances)
else:
    min_distance = max_distance = 0.0


# -------------------------------------------------------------------
# 2D coordinates for the HTML overview map
# -------------------------------------------------------------------

all_indices = list(df.index)
n_rows = len(all_indices)
distance_matrix = np.zeros((n_rows, n_rows), dtype=float)

for pos_i, i in enumerate(all_indices):
    for pos_j, j in enumerate(all_indices[pos_i + 1:], start=pos_i + 1):
        diff = scaled_df.loc[i, MATCH_FEATURES].to_numpy(dtype=float) - scaled_df.loc[j, MATCH_FEATURES].to_numpy(dtype=float)
        distance = float(np.sqrt(np.sum(np.square(diff))))
        distance_matrix[pos_i, pos_j] = distance
        distance_matrix[pos_j, pos_i] = distance

if n_rows == 0:
    coords = np.empty((0, 2))
elif n_rows == 1:
    coords = np.zeros((1, 2))
else:
    squared = np.square(distance_matrix)
    centering = np.eye(n_rows) - np.ones((n_rows, n_rows)) / n_rows
    gram = -0.5 * centering @ squared @ centering
    eigvals, eigvecs = np.linalg.eigh(gram)
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]
    positive = np.maximum(eigvals[:2], 0.0)
    coords = eigvecs[:, :2] * np.sqrt(positive)
    if coords.shape[1] < 2:
        coords = np.pad(coords, ((0, 0), (0, 2 - coords.shape[1])), mode="constant")

if len(coords):
    x = coords[:, 0]
    y = coords[:, 1]
    span_x = max(float(x.max() - x.min()), 1e-9)
    span_y = max(float(y.max() - y.min()), 1e-9)
    plot_x = 52 + ((x - x.min()) / span_x) * (1000 - 104)
    plot_y = 520 - (52 + ((y - y.min()) / span_y) * (520 - 104))
    coord_map = {
        idx: (round(float(plot_x[pos]), 2), round(float(plot_y[pos]), 2))
        for pos, idx in enumerate(all_indices)
    }
else:
    coord_map = {}


# -------------------------------------------------------------------
# Final upload-ready DataFrame
# -------------------------------------------------------------------

output_rows: list[dict[str, object]] = []

for pair in matched_pairs:
    distance = float(pair["pair_distance"])
    match_score = 100.0 if max_distance == min_distance else round(
        100 * (1 - (distance - min_distance) / (max_distance - min_distance)),
        1,
    )

    control = df.loc[pair["control_idx"]]
    treatment = df.loc[pair["treatment_idx"]]
    control_x, control_y = coord_map[pair["control_idx"]]
    treatment_x, treatment_y = coord_map[pair["treatment_idx"]]

    output_rows.append(
        {
            "nmls": int(control["nmls"]),
            "assignment": "control",
            "pro_ranking": control["pro_ranking"],
            "pro_score": float(control["pro_score"]),
            "uwm_production": float(control["uwm_production"]),
            "overall_production": float(control["overall_production"]),
            "conv_mix": float(control["conv_mix"]),
            "fha_mix": float(control["fha_mix"]),
            "va_mix": float(control["va_mix"]),
            "purchase_pct": float(control["purchase_pct"]),
            "refi_pct": float(control["refi_pct"]),
            "total_ytd_closings": float(control["total_ytd_closings"]),
            "jan_closings": int(control["jan_closings"]),
            "feb_closings": int(control["feb_closings"]),
            "march_closings": int(control["march_closings"]),
            "pair_distance": round(distance, 4),
            "twin_nmls": int(treatment["nmls"]),
            "plot_x": control_x,
            "plot_y": control_y,
            "pair_id": int(pair["pair_id"]),
            "match_score": match_score,
        }
    )

    output_rows.append(
        {
            "nmls": int(treatment["nmls"]),
            "assignment": "treatment",
            "pro_ranking": treatment["pro_ranking"],
            "pro_score": float(treatment["pro_score"]),
            "uwm_production": float(treatment["uwm_production"]),
            "overall_production": float(treatment["overall_production"]),
            "conv_mix": float(treatment["conv_mix"]),
            "fha_mix": float(treatment["fha_mix"]),
            "va_mix": float(treatment["va_mix"]),
            "purchase_pct": float(treatment["purchase_pct"]),
            "refi_pct": float(treatment["refi_pct"]),
            "total_ytd_closings": float(treatment["total_ytd_closings"]),
            "jan_closings": int(treatment["jan_closings"]),
            "feb_closings": int(treatment["feb_closings"]),
            "march_closings": int(treatment["march_closings"]),
            "pair_distance": round(distance, 4),
            "twin_nmls": int(control["nmls"]),
            "plot_x": treatment_x,
            "plot_y": treatment_y,
            "pair_id": int(pair["pair_id"]),
            "match_score": match_score,
        }
    )

for idx in outlier_indices:
    row = df.loc[idx]
    plot_x, plot_y = coord_map[idx]
    output_rows.append(
        {
            "nmls": int(row["nmls"]),
            "assignment": "outlier",
            "pro_ranking": row["pro_ranking"],
            "pro_score": float(row["pro_score"]),
            "uwm_production": float(row["uwm_production"]),
            "overall_production": float(row["overall_production"]),
            "conv_mix": float(row["conv_mix"]),
            "fha_mix": float(row["fha_mix"]),
            "va_mix": float(row["va_mix"]),
            "purchase_pct": float(row["purchase_pct"]),
            "refi_pct": float(row["refi_pct"]),
            "total_ytd_closings": float(row["total_ytd_closings"]),
            "jan_closings": int(row["jan_closings"]),
            "feb_closings": int(row["feb_closings"]),
            "march_closings": int(row["march_closings"]),
            "pair_distance": np.nan,
            "twin_nmls": np.nan,
            "plot_x": plot_x,
            "plot_y": plot_y,
            "pair_id": np.nan,
            "match_score": np.nan,
        }
    )

assignment_order = {"control": 0, "treatment": 1, "outlier": 2}

final_df = pd.DataFrame(output_rows)[UPLOAD_COLUMNS]
final_df["_assignment_sort"] = final_df["assignment"].map(assignment_order)
final_df = (
    final_df
    .sort_values(["pair_id", "_assignment_sort", "nmls"], na_position="last")
    .drop(columns="_assignment_sort")
    .reset_index(drop=True)
)

for col in ["nmls", "jan_closings", "feb_closings", "march_closings"]:
    final_df[col] = final_df[col].astype("Int64")
for col in ["twin_nmls", "pair_id"]:
    final_df[col] = final_df[col].astype("Int64")

pair_summary_df = pd.DataFrame(
    [
        {
            "pair_id": int(pair["pair_id"]),
            "pair_distance": round(float(pair["pair_distance"]), 4),
            "control_nmls": int(df.loc[pair["control_idx"], "nmls"]),
            "treatment_nmls": int(df.loc[pair["treatment_idx"], "nmls"]),
            "pro_ranking": df.loc[pair["control_idx"], "pro_ranking"],
        }
        for pair in matched_pairs
    ]
)

outlier_df = df.loc[outlier_indices].copy().reset_index(drop=True) if outlier_indices else df.iloc[0:0].copy()


# Optional export step, only when you want to download a CSV:
# final_df.to_csv("test_twin_data.csv", index=False)
