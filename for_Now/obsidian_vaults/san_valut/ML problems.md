# **Data Problems → Common Classical ML Solutions**

| **Problem**                          | **Common Solution**             |
| ------------------------------------ | ------------------------------- |
| Imbalanced data                      | SMOTE                           |
| Missing values                       | Mean/Median Imputation          |
| Too many features                    | PCA                             |
| Multicollinearity                    | Ridge Regression                |
| Overfitting                          | Regularization                  |
| Underfitting                         | More complex model              |
| High variance                        | Bagging                         |
| High bias                            | Boosting                        |
| Nonlinear relationships              | Kernel Methods                  |
| Different feature scales             | Standardization                 |
| Outliers                             | Robust Scaling                  |
| Sparse categorical variables         | Target Encoding                 |
| High-cardinality categories          | CatBoost Encoding               |
| Too many correlated variables        | Feature Selection               |
| Curse of dimensionality              | Dimensionality Reduction        |
| Data leakage                         | Proper Train/Test Split         |
| Noisy labels                         | Label Cleaning                  |
| Skewed distributions                 | Log Transformation              |
| Non-stationary time series           | Differencing                    |
| Concept drift                        | Online Learning                 |
| Rare event detection                 | Anomaly Detection               |
| Unlabeled data                       | Clustering                      |
| Class overlap                        | Better Feature Engineering      |
| Large training time                  | Sampling                        |
| Slow inference                       | Model Compression               |
| Unstructured text                    | TF-IDF                          |
| Sequential dependence                | HMM / ARIMA                     |
| Temporal dependence                  | Lag Features                    |
| Missing timestamps                   | Time Interpolation              |
| Small dataset                        | Cross Validation                |
| Too many nulls                       | Missing Indicators              |
| Feature explosion                    | L1 Regularization               |
| Interpretability issues              | SHAP                            |
| Black-box models                     | Decision Trees                  |
| Data sparsity                        | Matrix Factorization            |
| Duplicate records                    | Deduplication                   |
| Unbalanced costs                     | Cost-sensitive Learning         |
| Highly skewed target                 | Quantile Transformation         |
| Extreme outliers                     | Winsorization                   |
| Heteroscedasticity                   | Weighted Regression             |
| Non-Gaussian residuals               | GLMs                            |
| Autocorrelation                      | Time-Series Models              |
| Correlated observations              | Mixed Effects Models            |
| High memory usage                    | Incremental Learning            |
| Large categorical space              | Embeddings                      |
| Feature drift                        | Monitoring Pipelines            |
| Label drift                          | Periodic Retraining             |
| Too many irrelevant features         | Recursive Feature Elimination   |
| Weak signal                          | Feature Construction            |
| Unstable model performance           | Ensemble Models                 |
| Poor calibration                     | Platt Scaling                   |
| Probability calibration issues       | Isotonic Regression             |
| Unknown fraud patterns               | Isolation Forest                |
| Networked fraud                      | Graph Analytics                 |
| Extreme class rarity                 | Focal Loss                      |
| Seasonal patterns                    | Seasonal Decomposition          |
| Trend + seasonality                  | Prophet                         |
| Nonlinear boundaries                 | SVM                             |
| Too many local minima                | Better Initialization           |
| Training instability                 | Batch Normalization             |
| Vanishing gradients                  | ReLU                            |
| High variance in trees               | Random Forest                   |
| Sensitive to noise                   | Robust Loss Functions           |
| Dataset shift                        | Domain Adaptation               |
| Covariate shift                      | Reweighting                     |
| Poor recommendation quality          | Collaborative Filtering         |
| Cold-start problem                   | Content-based Filtering         |
| User-item sparsity                   | ALS                             |
| Long-tail distribution               | Re-ranking                      |
| Sparse text vectors                  | Word Embeddings                 |
| Topic discovery                      | LDA                             |
| Fraud rings                          | Graph Neural Networks           |
| Survival prediction                  | Cox Proportional Hazards        |
| Time-to-event data                   | Survival Analysis               |
| Censored observations                | Kaplan-Meier                    |
| Competing risks                      | Fine-Gray Models                |
| Dynamic pricing                      | Multi-Armed Bandits             |
| Exploration vs exploitation          | Thompson Sampling               |
| Causal inference                     | Propensity Score Matching       |
| Selection bias                       | Inverse Propensity Weighting    |
| Hidden confounders                   | Instrumental Variables          |
| Uplift prediction                    | Uplift Modeling                 |
| Multiple treatment effects           | Causal Forests                  |
| Forecast uncertainty                 | Bayesian Models                 |
| Regime changes                       | Hidden Markov Models            |
| Rare catastrophic events             | Extreme Value Theory            |
| Portfolio risk                       | Monte Carlo Simulation          |
| Unknown feature interactions         | Gradient Boosting               |
| High-dimensional tabular data        | XGBoost                         |
| Limited interpretability in boosting | SHAP Values                     |
| Weak anomaly signals                 | Autoencoders                    |
| Sparse graphs                        | GraphSAGE                       |
| Link prediction                      | Node Embeddings                 |
| Customer churn                       | Survival Models                 |
| Ranking problems                     | Learning to Rank                |
| Delayed feedback                     | Reinforcement Learning          |
| Human feedback integration           | Active Learning                 |
| Expensive labeling                   | Semi-supervised Learning        |
| Low-quality labels                   | Weak Supervision                |
| Model uncertainty                    | Bayesian Inference              |
| Uncertainty estimation               | Monte Carlo Dropout             |
| Data privacy concerns                | Federated Learning              |
| Non-IID distributed data             | Personalized Federated Learning |
| Massive datasets                     | Distributed Training            |
| Real-time predictions                | Streaming Pipelines             |
| Low latency requirement              | Approximate Nearest Neighbors   |
| Vector similarity search             | FAISS                           |
| Retrieval augmentation               | RAG                             |
| Hallucinations in LLMs               | Grounded Retrieval              |
| Long documents                       | Chunking                        |
| Poor retrieval relevance             | Reranking Models                |
| Semantic search                      | Embeddings                      |
| Memory limitations                   | Quantization                    |
| Hallucinated SQL                     | Schema-aware Prompting          |
| Prompt instability                   | Prompt Templates                |
| Unsafe outputs                       | Guardrails                      |
| Drift in embeddings                  | Embedding Refresh               |
| Multi-modal mismatch                 | Contrastive Learning            |