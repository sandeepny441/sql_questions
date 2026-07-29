
Below is a **timeline-style list of classical statistics-based outlier detection methods**, excluding modern ML-based approaches like Isolation Forest, One-Class SVM, Autoencoders, LOF, DBSCAN, etc.

**Statistics-Based Outlier Detection Models by Timeline**

|**Approx. Period**|**Method**|**Core Idea**|**Simple Methodology**|
|---|---|---|---|
|1800s|**Visual inspection / extreme value checking**|Look for unusually large or small values|Sort the data or plot it. Points far away from the rest are treated as suspicious.|
|1860s|**Chauvenet’s Criterion**|Outliers are values too unlikely under a normal distribution|Assume data is normal. If the probability of seeing a value that extreme is too small for the sample size, flag it.|
|Late 1800s|**Peirce’s Criterion**|Remove observations that are statistically inconsistent with the rest|Similar to Chauvenet, but more formal and can handle multiple outliers.|
|Early 1900s|**Z-Score Method**|Outliers are many standard deviations away from the mean|Compute: value minus mean divided by standard deviation. If absolute z-score is above 2, 3, or 4, flag it.|
|Early 1900s|**Modified Z-Score**|Uses median instead of mean|Replace mean with median and standard deviation with median absolute deviation. More robust when outliers already exist.|
|1920s|**Grubbs’ Test**|Tests whether the largest deviation from the mean is an outlier|Find the point farthest from the mean. Compare its standardized distance to a critical threshold.|
|1930s|**Dixon’s Q Test**|Useful for very small samples|Compare the gap between the suspicious value and its nearest neighbor to the overall range. Large gap means possible outlier.|
|1940s–1950s|**Studentized Residuals**|Outliers in regression are points with unusually large residuals|Fit a regression model. Look at errors divided by their estimated standard error. Very large residuals are flagged.|
|1950s|**Standardized Residuals**|Simpler regression-based outlier check|Fit a regression model. Standardize the residuals. Residuals above 2 or 3 standard deviations are suspicious.|
|1950s|**Mahalanobis Distance**|Multivariate version of z-score|Measures how far a point is from the center of the data while accounting for correlation between variables.|
|1950s–1960s|**Hotelling’s T-Squared**|Multivariate control-chart method|Used when monitoring several variables together. Flags observations far from the multivariate mean.|
|1960s|**Tukey’s IQR Method**|Outliers are values outside boxplot fences|Compute Q1 and Q3. IQR = Q3 minus Q1. Values below Q1 − 1.5 IQR or above Q3 + 1.5 IQR are outliers.|
|1960s|**Boxplot Rule**|Visual form of IQR method|Plot a boxplot. Points beyond whiskers are treated as potential outliers.|
|1960s|**Cook’s Distance**|Finds influential regression points|Measures how much the regression line changes if one observation is removed. Large Cook’s distance means high influence.|
|1970s|**Leverage / Hat Values**|Finds unusual x-values in regression|Points with unusual predictor values can strongly affect the model. High leverage points are flagged.|
|1970s|**DFFITS**|Measures influence on fitted value|Checks how much a single point changes its own predicted value when removed.|
|1970s|**DFBETAS**|Measures influence on regression coefficients|Checks how much each coefficient changes if one observation is removed.|
|1970s|**Elliptic Envelope / Gaussian Ellipse**|Multivariate normal boundary|Assume data follows a multivariate Gaussian shape. Points outside the confidence ellipse are outliers.|
|1970s–1980s|**MAD Method**|Robust deviation method|Compute median absolute deviation from the median. Points many MADs away are flagged.|
|1980s|**Generalized ESD Test**|Detects multiple outliers|Extension of Grubbs’ test. Repeatedly removes the most extreme value and tests whether it is an outlier.|
|1980s|**Robust Covariance Distance**|Robust Mahalanobis distance|Estimate center and covariance in a way less affected by outliers, then compute Mahalanobis distance.|
|1980s–1990s|**MCD: Minimum Covariance Determinant**|Robust multivariate outlier detection|Finds a subset of data with the smallest covariance. Points far from this robust center are outliers.|
|1990s|**Hampel Identifier**|Rolling median outlier detection|Common in time series. Compare each point to a rolling median and rolling MAD. Large deviations are flagged.|
|1990s|**STL Residual Outlier Detection**|Time-series decomposition method|Decompose time series into trend, seasonality, and residual. Outliers are extreme residuals.|
|1990s–2000s|**Control Charts**|Industrial process outlier detection|Monitor whether values fall outside statistical control limits.|
|1990s–2000s|**Shewhart Chart**|Simple control chart|Flag values outside mean ± 3 standard deviations.|
|1990s–2000s|**CUSUM Chart**|Detects small persistent shifts|Tracks cumulative deviations from the expected mean. Useful when changes are gradual.|
|1990s–2000s|**EWMA Chart**|Smooths recent observations|Gives more weight to recent data. Flags when the smoothed value crosses control limits.|
|2000s|**Extreme Value Theory**|Models rare tail events|Focuses only on the extreme ends of the distribution and estimates how rare a point is.|
|2000s|**Peak Over Threshold Method**|EVT method for tail anomalies|Pick a high threshold. Model values above that threshold using a generalized Pareto distribution.|
|2000s|**Generalized Extreme Value Model**|Models block maxima or minima|Split data into blocks, take maximum or minimum from each block, and model extreme behavior.|
|2000s–2010s|**Bayesian Outlier Detection**|Uses probability and prior beliefs|Build a statistical model and compute whether each point has low probability under the model.|
|2000s–2010s|**Mixture Distribution Outlier Model**|Assumes data has normal and abnormal components|Model data as mostly regular observations plus a small outlier-generating distribution.|
|2010s|**Robust PCA Residual Detection**|Statistical decomposition approach|Decompose data into low-rank structure and sparse abnormal part. Large sparse residuals are outliers.|
|2010s|**Time-Series Forecast Residual Method**|Outliers are unexpected forecast errors|Fit ARIMA, ETS, or another statistical forecasting model. If actual value is far from forecast interval, flag it.|
|2010s|**Prediction Interval Method**|Uses statistical uncertainty bands|Build expected range, such as 95 percent or 99 percent interval. Points outside the interval are anomalies.|
|2010s–Present|**Robust Time-Series Decomposition**|Modern robust statistical anomaly detection|Separate trend, seasonality, and noise using robust methods. Extreme residuals become outliers.|

---

**Easier Grouping by Data Type**

**1. Single Variable Outlier Detection**

Use when you have one column, like income, loan amount, transaction amount, or credit score.

|**Method**|**Best For**|**Simple Explanation**|
|---|---|---|
|Z-score|Normal data|Too many standard deviations from the mean|
|Modified Z-score|Skewed or dirty data|Too far from the median|
|IQR / Tukey Rule|General use|Outside the boxplot fences|
|MAD|Robust detection|Median-based distance|
|Grubbs’ Test|One outlier|Tests the most extreme point|
|Dixon’s Q|Very small samples|Checks if one value is separated by a big gap|
|Generalized ESD|Multiple outliers|Repeatedly tests extreme values|

---

**2. Multiple Variable Outlier Detection**

Use when the outlier is not obvious in one column but is strange across multiple columns.

Example:  
A borrower’s income may not be strange alone.  
Loan amount may not be strange alone.  
But **income = 40K and loan amount = 1.2M** together may be strange.

|**Method**|**Best For**|**Simple Explanation**|
|---|---|---|
|Mahalanobis Distance|Multivariate numeric data|Measures distance from the center while considering correlations|
|Hotelling’s T-Squared|Process monitoring|Multivariate version of control chart|
|Elliptic Envelope|Gaussian-shaped data|Flags points outside the normal ellipse|
|Robust Covariance|Dirty multivariate data|Robust version of Mahalanobis|
|MCD|Data with many outliers|Finds clean core data first, then flags far points|

---

**3. Regression-Based Outlier Detection**

Use when you are predicting one variable using others.

Example:  
Predict loan amount from income, credit score, DTI, and property value.  
If one observation has a huge prediction error, it may be suspicious.

|**Method**|**Best For**|**Simple Explanation**|
|---|---|---|
|Standardized Residuals|Basic regression outliers|Error is too large|
|Studentized Residuals|More reliable residual check|Error adjusted by uncertainty|
|Leverage|Unusual input values|X-values are far from the rest|
|Cook’s Distance|Influential observations|Point changes the model too much|
|DFFITS|Prediction influence|Point heavily changes fitted value|
|DFBETAS|Coefficient influence|Point heavily changes model coefficients|

---

**4. Time-Series Outlier Detection**

Use when the data changes over time.

Example:  
Daily loan submissions, weekly fraud rates, monthly prepayment rates, daily transaction counts.

|**Method**|**Best For**|**Simple Explanation**|
|---|---|---|
|Rolling Z-score|Simple time-series monitoring|Compare today to recent average|
|Rolling Median + MAD|Robust monitoring|Compare today to recent median|
|Hampel Filter|Spike detection|Rolling median-based spike detector|
|STL Residuals|Seasonal data|Remove trend and seasonality first|
|ARIMA Residuals|Forecast-based detection|Actual value is far from forecast|
|Prediction Intervals|Forecast uncertainty|Actual value falls outside expected band|
|EWMA Chart|Slow drift|Smooths recent values|
|CUSUM Chart|Persistent shift|Accumulates small changes|
|Shewhart Chart|Sudden spikes|Flags values beyond control limits|

---

**5. Extreme Tail Detection**

Use when you care about rare, very large, or very small events.

Example:  
Very large claims, rare fraud losses, extreme mortgage prepayments, unusually high chargebacks.

|**Method**|**Best For**|**Simple Explanation**|
|---|---|---|
|Extreme Value Theory|Rare event modeling|Focuses only on tails|
|Peak Over Threshold|Very high values|Models values above a high cutoff|
|Generalized Extreme Value|Block maxima/minima|Models maximum or minimum values over time windows|

---

**Most Practical Methods to Learn First**

For practical analytics work, learn these first:

| **Priority** | **Method**             | **Why It Matters**                         |
| ------------ | ---------------------- | ------------------------------------------ |
| 1            | IQR / Tukey Rule       | Simple, explainable, no strong assumptions |
| 2            | Z-score                | Classic baseline method                    |
| 3            | Modified Z-score / MAD | Better when data is skewed or dirty        |
| 4            | Mahalanobis Distance   | Essential for multivariate outliers        |
| 5            | Studentized Residuals  | Useful in regression modeling              |
| 6            | Cook’s Distance        | Finds influential records                  |
| 7            | Hampel Filter          | Very useful for time-series spikes         |
| 8            | STL Residuals          | Useful when seasonality exists             |
| 9            | Control Charts         | Useful for monitoring business processes   |
| 10           | Extreme Value Theory   | Useful for rare events and tail risk       |

---

**Simple Rule of Thumb**

| **Situation**                 | **Use This**                            |
| ----------------------------- | --------------------------------------- |
| One column, clean data        | Z-score                                 |
| One column, skewed data       | IQR or MAD                              |
| Multiple numeric columns      | Mahalanobis Distance                    |
| Regression model              | Studentized residuals + Cook’s Distance |
| Time-series spikes            | Hampel Filter                           |
| Seasonal time series          | STL residuals                           |
| Process monitoring            | Shewhart, CUSUM, EWMA                   |
| Rare extreme events           | Extreme Value Theory                    |
| Dirty data with many outliers | Robust covariance or MCD                |

**In one line**

**Statistics-based outlier detection means you define what “normal” looks like using probability, distance, residuals, distribution shape, or time-series behavior, then flag points that are too unlikely or too far away from that normal pattern.**

|                              |
| ---------------------------- |
| Correlation is Not Causation |
Interaction Effects