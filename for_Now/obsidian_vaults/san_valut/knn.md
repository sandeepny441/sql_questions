**K-Nearest Neighbors (KNN)** is a simple, intuitive supervised learning algorithm. It makes predictions based on the "similarity" (measured by distance) between a new data point and the existing training data points. It doesn't learn a model during training — it just stores the data — and does all the work at prediction time.

### 1. Training Phase (Almost No Math)
- Store all training examples:  
  Let the training set be $\{( \mathbf{x}_1, y_1 ), ( \mathbf{x}_2, y_2 ), \dots, ( \mathbf{x}_n, y_n ) \}$,  
  where $\mathbf{x}_i$ is a feature vector (e.g., [height, weight]) and $y_i$ is the label (class for classification, number for regression).

No formulas or optimization happen here.

### 2. Prediction Phase — Core Math

Given a new test point $\mathbf{x}^*$, KNN does the following:

#### Step A: Compute Distance to Every Training Point
The most common distance is **Euclidean distance** (straight-line distance):

$$
d(\mathbf{x}^*, \mathbf{x}_i) = \sqrt{ \sum_{j=1}^{m} (x^*_j - x_{i,j})^2 }
$$

where $m$ = number of features.

**Other popular distance metrics** (you can choose any):

- **Manhattan (L1)**:  
  $d(\mathbf{x}^*, \mathbf{x}_i) = \sum_{j=1}^{m} |x^*_j - x_{i,j}|$

- **Minkowski (general form)**:  
  $d(\mathbf{x}^*, \mathbf{x}_i) = \left( \sum_{j=1}^{m} |x^*_j - x_{i,j}|^p \right)^{1/p}$  
  (Euclidean when $p=2$, Manhattan when $p=1$)

- **Cosine distance** (for text/high-dimensional data):  
  $d(\mathbf{x}^*, \mathbf{x}_i) = 1 - \frac{\mathbf{x}^* \cdot \mathbf{x}_i}{||\mathbf{x}^*|| \ ||\mathbf{x}_i||}$

You calculate this distance for every single training point $\mathbf{x}_i$.

#### Step B: Find the K Nearest Neighbors
Sort all distances in ascending order and pick the **K smallest** ones.

Let the indices of the K nearest points be $N_K(\mathbf{x}^*)$.

#### Step C: Make the Prediction

**For Classification** (predicting a category):

- **Majority Vote** (standard KNN):  
  $$
  \hat{y} = \arg\max_{c} \sum_{i \in N_K(\mathbf{x}^*)} \mathbb{I}(y_i = c)
  $$
  where $\mathbb{I}$ is the indicator function (1 if true, 0 otherwise).  
  Simply: the class that appears most frequently among the K neighbors wins.

- **Distance-Weighted Vote** (often better):  
  $$
  \hat{y} = \arg\max_{c} \sum_{i \in N_K(\mathbf{x}^*)} w_i \cdot \mathbb{I}(y_i = c)
  $$
  where weight $w_i = \frac{1}{d(\mathbf{x}^*, \mathbf{x}_i) + \epsilon}$ ($\epsilon$ is a small number to avoid division by zero).

**For Regression** (predicting a number):

- **Simple Average**:  
  $$
  \hat{y} = \frac{1}{K} \sum_{i \in N_K(\mathbf{x}^*)} y_i
  $$

- **Distance-Weighted Average** (recommended):  
  $$
  \hat{y} = \frac{ \sum_{i \in N_K(\mathbf{x}^*)} w_i \cdot y_i }{ \sum_{i \in N_K(\mathbf{x}^*)} w_i }
  $$
  with the same weights $w_i = 1 / d(\mathbf{x}^*, \mathbf{x}_i)$ as above.

### Complete Prediction Algorithm (Summary)

1. For each training point $\mathbf{x}_i$, compute $d_i = d(\mathbf{x}^*, \mathbf{x}_i)$
2. Sort the points by $d_i$ (ascending)
3. Select the first K points → set $N_K$
4. Compute $\hat{y}$ using the appropriate formula above (classification or regression)

### Choosing K (Hyperparameter)
- Small K → more sensitive to noise (can overfit)
- Large K → smoother decision boundary (can underfit)
- Common rule of thumb: $K = \sqrt{n}$ (n = number of training samples), then tune with cross-validation.

### Optional Improvements

- **Feature Scaling** (very important!):  
  Before calculating distances, normalize or standardize features:  
  $x'_j = \frac{x_j - \mu_j}{\sigma_j}$ (standardization) or $x'_j = \frac{x_j - \min_j}{\max_j - \min_j}$ (min-max).

- **KD-Tree or Ball Tree**: For faster neighbor search in low dimensions (instead of brute force $O(n)$).

### Simple 2D Example (Intuition)
Suppose you have points on a plane (2 features).  
You plot a new point ★.  
You draw circles expanding until you hit K points.  
Look at those K points' labels → vote or average.

That's literally all the math behind KNN!

Would you like me to show a small numerical example with actual numbers, or explain how to implement it in Python (with formulas mapped to code)?