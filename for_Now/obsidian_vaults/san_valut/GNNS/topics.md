# Chapter 1: Graph Fundamentals

## 1. What is a graph?

- Technical Definition: A graph is a mathematical structure made of nodes (entities) and edges (relationships).
    
- Layman Example: Think of a social network where people are connected through friendships.
    

## 2. Nodes and edges

- Technical Definition: Nodes represent entities, while edges represent relationships between entities.
    
- Layman Example: Borrowers are nodes and shared addresses between them are edges.
    

## 3. Directed vs undirected graphs

- Technical Definition: Directed graphs have one-way relationships, while undirected graphs have two-way relationships.
    
- Layman Example: Sending money is directional, while friendship is usually mutual.
    

## 4. Weighted vs unweighted graphs

- Technical Definition: Weighted graphs assign importance or strength to edges.
    
- Layman Example: Two borrowers sharing ten loans have a stronger connection than sharing one loan.
    

## 5. Bipartite graphs

- Technical Definition: A graph containing two different types of nodes connected across groups.
    
- Layman Example: Borrowers connected to properties.
    

## 6. Adjacency matrix

- Technical Definition: A matrix representation showing whether node pairs are connected.
    
- Layman Example: A spreadsheet showing which borrowers are linked to which employers.
    

## 7. Adjacency list

- Technical Definition: A list storing neighboring nodes for each node.
    
- Layman Example: A contact list showing everyone connected to a borrower.
    

## 8. Degree of a node

- Technical Definition: The number of connections attached to a node.
    
- Layman Example: A loan officer connected to hundreds of suspicious loans.
    

## 9. Paths, cycles and connectivity

- Technical Definition: Paths describe routes between nodes; cycles are loops.
    
- Layman Example: Borrower → Employer → Broker → Borrower forming a suspicious loop.
    

## 10. Real-world graph examples in ML

- Technical Definition: Graph structures used in practical machine learning systems.
    
- Layman Example: Fraud rings, recommendation systems and social networks.
    

---

# Chapter 2: Classical Graph Algorithms

## 11. Breadth-First Search (BFS)

- Technical Definition: A traversal method exploring neighbors level by level.
    
- Layman Example: Investigating all people directly connected to a suspicious borrower first.
    

## 12. Depth-First Search (DFS)

- Technical Definition: A traversal method exploring deeply before backtracking.
    
- Layman Example: Following one fraud chain as far as possible.
    

## 13. Shortest path algorithms

- Technical Definition: Algorithms finding the minimum connection distance between nodes.
    
- Layman Example: Finding the shortest relationship chain between two fraudsters.
    

## 14. Dijkstra’s algorithm

- Technical Definition: An algorithm computing shortest weighted paths.
    
- Layman Example: Finding the least costly transaction route.
    

## 15. PageRank intuition

- Technical Definition: Ranking nodes based on importance from connected nodes.
    
- Layman Example: Identifying influential brokers in a fraud network.
    

## 16. Community detection

- Technical Definition: Identifying tightly connected node groups.
    
- Layman Example: Detecting colluding borrower groups.
    

## 17. Centrality measures

- Technical Definition: Metrics measuring node importance inside graphs.
    
- Layman Example: Finding the main organizer in a fraud ring.
    

## 18. Graph clustering

- Technical Definition: Grouping similar nodes based on connectivity.
    
- Layman Example: Grouping borrowers with similar suspicious behavior.
    

## 19. Random walks on graphs

- Technical Definition: Sequential movement through graph connections probabilistically.
    
- Layman Example: Simulating how fraud risk spreads across connected entities.
    

## 20. Graph embeddings intuition

- Technical Definition: Converting graph structure into numerical vectors.
    
- Layman Example: Giving each borrower a behavioral fingerprint.
    

---

# Chapter 3: Foundations of Graph Machine Learning

## 21. What is graph machine learning?

- Technical Definition: Machine learning applied directly on graph structures.
    
- Layman Example: Teaching AI to detect fraud using relationships.
    

## 22. Node features and edge features

- Technical Definition: Attributes attached to nodes and edges.
    
- Layman Example: Borrower income and shared-address relationships.
    

## 23. Message passing concept

- Technical Definition: Nodes exchange information with neighboring nodes.
    
- Layman Example: Suspicion spreads from one borrower to connected borrowers.
    

## 24. Neighborhood aggregation

- Technical Definition: Combining neighboring node information.
    
- Layman Example: A borrower becomes risky because nearby entities are risky.
    

## 25. Graph convolution intuition

- Technical Definition: Learning patterns from local graph neighborhoods.
    
- Layman Example: Detecting suspicious local borrower-loan clusters.
    

## 26. What is a Graph Neural Network (GNN)?

- Technical Definition: A neural network designed for graph-structured data.
    
- Layman Example: A fraud AI that understands relationships instead of rows.
    

## 27. Graph Laplacian intuition

- Technical Definition: A matrix describing graph structure and smoothness.
    
- Layman Example: Measuring how connected a fraud network is.
    

## 28. Spectral vs spatial methods

- Technical Definition: Two approaches to graph learning using matrix properties or neighborhoods.
    
- Layman Example: Studying fraud globally vs locally.
    

## 29. Over-smoothing problem

- Technical Definition: Node representations becoming too similar after many layers.
    
- Layman Example: All borrowers starting to look identical to the model.
    

## 30. Mini-batching in graphs

- Technical Definition: Training graph models on smaller graph portions.
    
- Layman Example: Investigating one fraud neighborhood at a time.
    

---

# Chapter 4: Core Graph Neural Network Architectures

## 31. Graph Convolutional Networks (GCN)

- Technical Definition: GNNs using convolution-style neighborhood aggregation.
    
- Layman Example: Averaging nearby borrower behaviors to detect risk.
    

## 32. GraphSAGE

- Technical Definition: A scalable GNN sampling neighborhoods during training.
    
- Layman Example: Studying a subset of connected borrowers instead of the entire graph.
    

## 33. Graph Attention Networks (GAT)

- Technical Definition: GNNs assigning attention weights to neighbors.
    
- Layman Example: Some suspicious relationships matter more than others.
    

## 34. Gated Graph Neural Networks

- Technical Definition: GNNs using gating mechanisms similar to RNNs.
    
- Layman Example: Remembering important fraud signals over steps.
    

## 35. Heterogeneous GNNs

- Technical Definition: GNNs supporting multiple node and edge types.
    
- Layman Example: Borrowers, loan officers and properties all together.
    

## 36. Temporal / dynamic GNNs

- Technical Definition: GNNs handling changing graphs over time.
    
- Layman Example: Monitoring evolving fraud activity daily.
    

## 37. Knowledge graph networks

- Technical Definition: Graphs representing entities and semantic relationships.
    
- Layman Example: Linking borrowers, employers, regulations and properties.
    

## 38. Autoencoders for graphs

- Technical Definition: Models compressing and reconstructing graph information.
    
- Layman Example: Detecting abnormal fraud patterns by reconstruction errors.
    

## 39. Self-supervised graph learning

- Technical Definition: Learning graph patterns without labeled data.
    
- Layman Example: Discovering suspicious structures automatically.
    

## 40. Graph transformers intuition

- Technical Definition: Transformer architectures adapted for graph data.
    
- Layman Example: Capturing long-range fraud relationships across the network.
    

---

# Chapter 5: Graph Neural Networks in Practice

## 41. Node classification

- Technical Definition: Predicting labels for graph nodes.
    
- Layman Example: Predicting whether a borrower is fraudulent.
    

## 42. Link prediction

- Technical Definition: Predicting missing or future graph connections.
    
- Layman Example: Predicting hidden collusion between brokers.
    

## 43. Graph classification

- Technical Definition: Predicting labels for entire graphs.
    
- Layman Example: Determining whether a loan network is suspicious.
    

## 44. Fraud detection using GNNs

- Technical Definition: Using graph learning to identify fraudulent structures.
    
- Layman Example: Detecting organized mortgage fraud rings.
    

## 45. Recommendation systems with graphs

- Technical Definition: Graph-based systems recommending relevant items.
    
- Layman Example: Suggesting relevant mortgage products using borrower relationships.
    

## 46. Social network analysis

- Technical Definition: Studying behavior patterns in social graphs.
    
- Layman Example: Understanding broker referral ecosystems.
    

## 47. Molecular and drug discovery graphs

- Technical Definition: Representing molecules as graph structures.
    
- Layman Example: Atoms connected like borrower-property relationships.
    

## 48. Building graph datasets

- Technical Definition: Constructing graph data from raw relational information.
    
- Layman Example: Creating borrower-property-loan officer networks from mortgage records.
    

## 49. Training and scaling GNNs

- Technical Definition: Optimizing graph models efficiently on large datasets.
    
- Layman Example: Running fraud models on millions of loans.
    

## 50. Explainability in graph neural networks

- Technical Definition: Understanding why graph models make predictions.
    
- Layman Example: Showing investigators which relationships triggered fraud alerts.