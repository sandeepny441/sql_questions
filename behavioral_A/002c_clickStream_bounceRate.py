import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Simulating dataset
np.random.seed(0)  # Seed for reproducibility
num_pages = 1000
df = pd.DataFrame({
    'PageLoadTime': np.random.normal(loc=3, scale=1.5, size=num_pages),  # Page load time in seconds
    'NumberOfImages': np.random.poisson(lam=3, size=num_pages),  # Number of images on a page
    'AmountOfText': np.random.poisson(lam=500, size=num_pages),  # Amount of text on a page (number of words)
    'PageLayoutType': np.random.choice(['Simple', 'Complex', 'Moderate'], size=num_pages),  # Type of page layout
    'BounceRate': np.random.uniform(low=0, high=100, size=num_pages)  # Bounce rate percentage
})

# EDA
# For a project analyzing bounce rates with regression analysis, here are several EDA questions that could guide the exploration of the data:

# General Analysis
# What is the distribution of bounce rates across the entire website?
# Are there certain pages or types of content with particularly high or low bounce rates?
# Page Features
# How does page load time correlate with bounce rates?
# What is the distribution of the number of images on a page, and how does this relate to bounce rates?
# Does the amount of text on a page influence the likelihood of a bounce?
# Page Layout Analysis
# Are there differences in bounce rates between different page layout types?
# Which layout elements are most common on pages with low bounce rates?
# Content Analysis
# Is there a content type that is associated with higher engagement and lower bounce rates?
# Do multimedia elements like videos and interactive content influence bounce rates?
# User Engagement
# How do engagement metrics like time on page or click-through rates relate to bounce rates?
# Are there common exit points on the website that could be optimized to reduce bounce rates?
# Traffic Sources
# Does the source of traffic (e.g., direct, search engines, social media) impact bounce rates?
# Are bounce rates higher for new visitors compared to returning visitors?
# Technical Performance
# How does mobile versus desktop browsing affect bounce rates?
# Are there technical issues on the site that may be causing higher bounce rates, such as broken links or error pages?
# Behavioral Patterns
# Can clustering of page features reveal distinct groups of pages with similar bounce rates?
# Is there a pattern in user behavior prior to bouncing, such as specific actions or inactions?
# Temporal Patterns
# Are there times of day, days of the week, or seasons where bounce rates are noticeably different?
# How do bounce rates change in response to marketing campaigns or site updates?
# Conversion Paths
# How do bounce rates vary across different stages of the conversion funnel?
# Are there particular pages that are critical in the conversion path that have high bounce rates?



# Convert categorical 'PageLayoutType' feature to dummy variables
df = pd.get_dummies(df, columns=['PageLayoutType'], drop_first=True)

# Define features (X) and target (y)
X = df.drop('BounceRate', axis=1)
y = df['BounceRate']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict bounce rates on the test set
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output model coefficients
coefficients = pd.Series(model.coef_, index=X.columns)

# Print metrics and model coefficients
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared Score: {r2}")
print("Model Coefficients:")
print(coefficients)
