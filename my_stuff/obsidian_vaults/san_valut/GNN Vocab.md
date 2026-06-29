Here's the full vocabulary, organized so you can learn it in roughly the order you'll encounter it. Work through this and you'll be able to read any GNN paper or PyG/DGL tutorial without hitting an unfamiliar term.

## 1. Graph fundamentals (the data structure itself)

| Term | What it means |
|---|---|
| Node (vertex) | A single entity in the graph. In fraud: a user, device, transaction, IP. |
| Edge (link) | A connection between two nodes. In fraud: "user X used device Y." |
| Directed edge | Edge with a direction ($u \to v \neq v \to u$). E.g., "money flowed from A to B." |
| Undirected edge | Edge without direction. E.g., "shared an IP." |
| Self-loop | An edge from a node to itself. Often added artificially so a node includes itself when aggregating. |
| Degree | Number of edges touching a node. **In-degree** and **out-degree** for directed graphs. |
| Neighborhood $\mathcal{N}(v)$ | The set of nodes directly connected to $v$. |
| $k$-hop neighborhood | Nodes reachable from $v$ in $\leq k$ steps. A 2-layer GNN sees the 2-hop neighborhood. |
| Path | A sequence of edges from one node to another. |
| Connected component | A maximal subgraph where every node can reach every other. |
| Subgraph | Any subset of nodes plus the edges between them. |
| Homogeneous graph | One node type, one edge type. |
| Heterogeneous graph | Multiple node types and/or edge types. Fraud graphs are almost always heterogeneous. |
| Bipartite graph | Two node types, edges only between types. E.g., users↔transactions. |
| Multigraph | Multiple edges allowed between the same pair of nodes. |
| Dynamic / temporal graph | Edges have timestamps; the graph evolves over time. Important for fraud (transactions are time-stamped). |
| Node features $x_v$ | Per-node feature vector. E.g., a user's age, account age, country. |
| Edge features $e_{uv}$ | Per-edge feature vector. E.g., transaction amount, timestamp. |
| Node label $y_v$ | The target for supervised learning. E.g., fraud / not-fraud. |

## 2. Matrix representations (how graphs become tensors)

| Term | What it means |
|---|---|
| Adjacency matrix $A$ | $n \times n$ matrix; $A_{ij}=1$ if edge exists, 0 otherwise. |
| Weighted adjacency | Same shape, but entries are edge weights instead of 0/1. |
| Degree matrix $D$ | Diagonal matrix with $D_{ii} = $ degree of node $i$. |
| Laplacian $L = D - A$ | Encodes graph structure; eigenvectors give "graph frequencies." |
| Normalized adjacency $\tilde{A} = D^{-1/2}(A+I)D^{-1/2}$ | The matrix GCN actually uses. The $+I$ adds self-loops; the $D^{-1/2}$ terms keep activations stable. |
| Feature matrix $X$ | $n \times d$ matrix stacking all node features. |
| Embedding matrix $H^{(k)}$ | $n \times d_k$ matrix of node embeddings at layer $k$. $H^{(0)} = X$. |
| Edge index | The standard sparse-format representation in PyG: a $2 \times \lvert E\rvert$ tensor listing edge endpoints. Replaces $A$ since real graphs are sparse. |

## 3. The message-passing machinery

| Term | What it means |
|---|---|
| Message-passing neural network (MPNN) | The general framework that almost all GNNs fit into. |
| Message function | Computes what each neighbor sends. Often just $W h_u$. |
| Aggregation function | Combines incoming messages into one vector. Must be **permutation-invariant** (sum, mean, max). |
| Update function | Combines a node's old embedding with the aggregated messages to make the new embedding. Usually an MLP or GRU. |
| Readout / pooling function | Combines all node embeddings into a single graph-level embedding (only needed for graph-level tasks, not node classification). |
| Permutation invariance | Output is unchanged if you reorder the inputs. Required for aggregation. |
| Permutation equivariance | If you permute inputs, outputs permute the same way. The property a GNN layer has at the node level. |
| Receptive field | Set of nodes that influence a given node's embedding. Grows by one hop per layer. |
| Inductive vs. transductive | **Transductive**: trained and tested on the same fixed graph (can't handle new nodes). **Inductive**: can generalize to unseen nodes/graphs. GraphSAGE was the first popular inductive GNN. |

## 4. The named architectures

| Term | What it means |
|---|---|
| GCN | Graph Convolutional Network. Uses normalized adjacency; the canonical baseline. |
| GraphSAGE | "SAmple and aggreGatE." Inductive, samples a fixed number of neighbors per node. The workhorse for large graphs. |
| GAT | Graph Attention Network. Learns attention weights over neighbors. |
| GIN | Graph Isomorphism Network. Sum-aggregation + MLP; theoretically most expressive of vanilla MPNNs. |
| R-GCN | Relational GCN. Separate weight matrix per edge type. The go-to for heterogeneous graphs. |
| HGT | Heterogeneous Graph Transformer. Attention-based, type-aware. |
| MPNN | Both a general framework name (above) and a specific architecture from Gilmer et al. 2017. |
| Spectral GNN | A family using graph Fourier transforms / Laplacian eigendecomposition. Mostly theoretical interest now; spatial methods (above) won. |
| Spatial GNN | Methods defined directly via neighborhood aggregation. Everything above is spatial. |

## 5. Training and scaling

| Term | What it means |
|---|---|
| Node classification | Predict a label per node. **Your task.** |
| Link prediction | Predict whether an edge should exist between two nodes. |
| Graph classification | Predict a label for the whole graph. |
| Neighbor sampling | Instead of using all neighbors (which explodes for hubs), sample $k$ per layer. The trick that makes GraphSAGE scale. |
| Mini-batch (for GNNs) | A batch of "computation subgraphs" — each target node plus its sampled $k$-hop neighborhood. Not as simple as MLP batching. |
| Cluster-GCN | Scaling trick: partition the graph into clusters, train on one cluster at a time. |
| GraphSAINT | Another scaling trick: sample subgraphs via random walks. |
| Full-batch training | Use the whole graph each step. Only works for graphs that fit in GPU memory. |
| Over-smoothing | Stacking too many layers makes all node embeddings converge to the same vector. Caps practical depth at 2–4. |
| Over-squashing | Information from distant nodes gets compressed through bottleneck edges and is lost. A separate failure mode from over-smoothing. |
| Jumping Knowledge (JK) connections | Concatenate or pool embeddings from multiple layers — like skip connections — to mitigate over-smoothing. |
| Dropout / DropEdge | Standard dropout, plus DropEdge: randomly drop edges during training as a regularizer. |
| Label leakage | In transductive setups, accidentally letting test labels influence training through the graph. Watch for this. |

## 6. Heterogeneous and temporal graphs (relevant to fraud)

| Term | What it means |
|---|---|
| Node type / edge type | The category a node or edge belongs to (user, device, "uses," "transacts"). |
| Metapath | A type-sequence describing a kind of path. E.g., User→Device→User = "users sharing a device." |
| Type-specific weights | One weight matrix per node/edge type, the core idea of R-GCN. |
| Temporal GNN | A GNN that respects edge timestamps; only past edges influence a node's current embedding. |
| TGN, TGAT | Two popular temporal GNN architectures. Worth knowing exist; not needed day one. |

## 7. Fraud-specific terms

| Term | What it means |
|---|---|
| Camouflage | When fraudsters deliberately connect to legitimate nodes to hide. |
| Class imbalance | Fraud is typically <1% of labels. Drives loss-function and sampling choices. |
| CARE-GNN | Fraud-specific GNN that handles camouflage via reinforcement-learned neighbor filtering. |
| PC-GNN | "Pick and Choose" GNN — fraud-specific sampler that balances classes during neighbor sampling. |
| Focal loss | Loss function that down-weights easy examples; useful under class imbalance. |
| Weighted cross-entropy | Cross-entropy with per-class weights; the simpler imbalance fix. |
| Negative sampling | When training link prediction, sample non-edges as negatives (true non-edges are too numerous to use all). |

## 8. Tooling

| Term | What it means |
|---|---|
| PyTorch Geometric (PyG) | The most popular GNN library. Built on PyTorch. Clean API. |
| DGL | Deep Graph Library. PyG's main competitor; better for very large graphs. |
| `Data` object (PyG) | A container holding `x` (features), `edge_index`, `y` (labels), etc. |
| `HeteroData` (PyG) | Same idea, for heterogeneous graphs. |
| `MessagePassing` base class | The class you subclass to implement a custom GNN layer in PyG. |
| OGB | Open Graph Benchmark. Standard datasets; useful for sanity-checking implementations. |
| NeighborLoader (PyG) | The mini-batch loader that does neighbor sampling. |

## How to use this list

Don't memorize it cold. Instead, work through it in **three passes**:

**Pass 1 (skim, ~30 min).** Read every row. You're just registering "these terms exist" — when you see "over-smoothing" in a tutorial later, you'll think "right, I know what bucket that's in."

**Pass 2 (focus, ~few hours).** Sections 1, 2, 3, and 5 are the load-bearing ones. Make sure you can write down (a) what the normalized adjacency matrix does and why, (b) the message → aggregate → update template from memory, (c) why aggregation must be permutation-invariant, and (d) what over-smoothing is. If you can explain these four, you understand 80% of GNNs.

**Pass 3 (build).** Skip section 6 and most of section 7 until you've trained a 2-layer GCN on Cora (the "MNIST of GNNs") in PyG — about 30 lines of code. Only after that working baseline should you swap in GraphSAGE, then GAT, then move to a heterogeneous fraud-shaped dataset.

The trap to avoid: reading about CARE-GNN and HGT before you've trained a vanilla GCN. You'll get lost in the fraud-specific tricks without grounding in what the tricks are modifying.

Want me to put together a concrete "first GNN in PyG" walkthrough — the Cora baseline — as your week-one milestone?