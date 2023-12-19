import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Simulating dataset with TimeOnPage, Converted (as a proxy for likelihood of conversion)
# and Churned (as a proxy for likelihood of churn)
np.random.seed(0)  # Seed for reproducibility
num_records = 1000
df = pd.DataFrame({
    'TimeOnPage': np.random.exponential(scale=300, size=num_records),  # simulated time on page in seconds
    'Converted': np.random.binomial(1, p=0.2, size=num_records),  # simulated conversion event (1 for yes, 0 for no)
    'Churned': np.random.binomial(1, p=0.05, size=num_records)  # simulated churn event (1 for yes, 0 for no)
})
===========================================================================
# EDA Questions:
-------------------------------------------------------------------------

# Understanding Time Spent
# What is the distribution of time spent on each page across all users?
# Are there any specific pages where users spend significantly more or less time?
# Time and User Behavior
# How does the time spent on a page relate to the user's journey on the website?
# Does the time spent on initial pages influence the time spent on subsequent pages?
# Time and Conversion
# Is there a correlation between time spent on a page and the conversion rate for that page?
# Are there diminishing returns on time spent on a page with respect to conversion likelihood?
# Time and Churn
# Is there a pattern in time spent on pages that could indicate a higher likelihood of churn?
# How does time spent on a page correlate with other indicators of disengagement or dissatisfaction?
# Page Content and Time Spent
# Do pages with certain types of content (videos, images, text) have different average time spent metrics?
# How does the complexity or readability of page content relate to the time users spend on it?
# User Segmentation
# Do different user segments (e.g., new vs. returning, demographics) spend different amounts of time on certain types of pages?
# Is the correlation between time on page and conversion/churn consistent across different user segments?
# Outliers
# Are there any outliers in terms of time spent on pages, and what can these cases tell us?
# Do users who spend an unusually long or short amount of time on the site have anything in common?
# Temporal Trends
# Are there any temporal patterns in time spent on pages, such as time of day or day of the week?
# How do time spent and conversion rates fluctuate during marketing campaigns or seasonal events?
# Technical Aspects
# Does page load time affect the amount of time users spend on the page?
# Are there technical issues on certain pages that could be affecting user engagement metrics?
# Behavioral Patterns
# Can clustering of user sessions based on time spent reveal distinct behavioral patterns?
# What are the common pathways through the website for users who convert versus those who churn?
# Conversion Path Analysis
# What is the average time spent on pages along the conversion path?
# Is there a typical 'drop-off' point in the conversion funnel where time spent on a page correlates with exiting the site?
# Engagement and Content Optimization
# How does user engagement with page elements (like calls to action) relate to time spent on the page?
# Can A/B testing on page variations give insights into optimal time spent for conversion?
# Answering these EDA questions can provide valuable insights into user engagement and behavior, guiding content strategy and website optimization to enhance customer experience and business outcomes.
===========================================================================
# Splitting the data into features and target for conversion prediction
X = df[['TimeOnPage']]  # Feature: Time on page
y = df['Converted']  # Target: Conversion

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

(report, conf_matrix)
