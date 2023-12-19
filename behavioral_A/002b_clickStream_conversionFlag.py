import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Simulating dataset
np.random.seed(0)  # Seed for reproducibility
data_size = 1000
df = pd.DataFrame({
    'TimeOnPage': np.random.exponential(scale=300, size=data_size),  # Time on page in seconds
    'NumberReviews': np.random.poisson(lam=5, size=data_size),  # Number of reviews
    'PageLayout': np.random.choice(['Layout1', 'Layout2', 'Layout3'], size=data_size),  # Simulated page layout
    'Converted': np.random.binomial(1, p=0.3, size=data_size)  # Conversion flag, 1 or 0
})

# Preprocessing
# Encoding categorical 'PageLayout' feature
categorical_features = ['PageLayout']
numeric_features = ['TimeOnPage', 'NumberReviews']
target = 'Converted'

# EDA
=======================================
# For a machine learning project that uses logistic regression or SVM to predict conversion based on user browsing sessions, including page layout as a feature, the following EDA questions can guide your analysis:

# Understanding User Sessions
# What is the distribution of time spent on page across sessions that converted versus those that did not?
# How does the number of user reviews interact with conversion rates?
# Page Layout Analysis
# Which page layout appears to be most effective in leading to conversions?
# Are there specific elements of page layouts that correlate with higher conversion rates?
# Conversion Pathways
# What are the common characteristics of browsing sessions that lead to conversion?
# Are there typical pathways or sequences of page views that are more likely to result in a conversion?
# User Engagement
# How does user engagement (e.g., clicks, page interactions) correlate with conversion?
# Do longer session durations always correlate with a higher likelihood of conversion, or is there a point of diminishing returns?
# Review Impact
# Is there a correlation between the sentiment of reviews and conversion rates?
# How do the number of reviews and the average review score relate to each other and to conversion rates?
# Traffic Sources
# Does the source of traffic (e.g., organic search, paid ads, social media) influence the likelihood of conversion?
# Are users from certain traffic sources more responsive to specific page layouts?
# User Demographics
# Do conversion rates differ significantly across user demographics such as age, gender, or location?
# How does the user segment (new vs. returning) relate to the effectiveness of different page layouts?
# Stock Availability
# Does the availability of products influence the conversion rate for users viewing those products?
# Are out-of-stock notifications on a page layout negatively impacting conversion rates?
# Technical Performance
# How does page load time affect user behavior and conversion rates?
# Are there any technical issues (e.g., broken links, images not loading) that correlate with lower conversion rates?
# A/B Testing
# How do variations in page layout from A/B testing correlate with changes in conversion rates?
# Which changes in page layout elements lead to statistically significant differences in user behavior?


# Create transformers for numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Split the data into features and target
X = df.drop(target, axis=1)
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline for SVM model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', SVC(probability=True))  # Using SVM with probability estimates
])

# Train the SVM model
pipeline.fit(X_train, y_train)

# Predict on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the model
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(report)
print(conf_matrix)
