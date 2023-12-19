import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Simulated dataset
np.random.seed(0)  # Seed for reproducibility
data_size = 1000
df = pd.DataFrame({
    'EngagementScore': np.random.rand(data_size),  # Simulated engagement score between 0 and 1
    'Shares': np.random.poisson(lam=10, size=data_size),  # Simulated number of shares
    'ConversionRate': np.random.rand(data_size),  # Simulated conversion rate between 0 and 1
    'ContentType': np.random.choice(['Image', 'Video', 'Text'], size=data_size)  # Types of content
})

# Mapping content types to numerical values
content_type_mapping = {'Image': 0, 'Video': 1, 'Text': 2}
df['ContentType'] = df['ContentType'].map(content_type_mapping)

# EDA

# Content Type Effectiveness
# Which ad content type has the highest average engagement score?
# What is the distribution of shares for each content type (image, video, text)?
# Which content type results in the highest conversion rates?
# Content and User Interaction
# How do engagement scores correlate with the number of shares and conversion rates for each content type?
# Are certain content types more likely to be shared or have higher engagement during specific times or events?
# Comparative Analysis
# How do the different content types perform across various platforms (e.g., social media, website, email)?
# Is there a significant difference in the performance of content types based on the length or format of the ad?
# Trends Over Time
# Are there any visible trends in content type performance over time?
# How does seasonality affect the engagement and conversion rates of different ad content types?
# Conversion Pathways
# What are the common characteristics of ads that lead to conversions?
# Is there a typical 'pathway' or sequence of content types that leads to higher conversion rates?
# Demographics and Segmentation
# Do certain demographic segments respond differently to various content types?
# How does the effectiveness of content types vary by user segments (e.g., new vs. returning customers)?
# Traffic Sources and Content Type
# Does the source of traffic influence which content type is more effective?
# Are certain content types more successful in attracting organic traffic compared to paid traffic?
# Technical Performance
# How does the technical performance of ad delivery (e.g., load times, responsiveness) affect the engagement of different content types?
# Are technical issues more common with certain types of content (e.g., videos requiring more bandwidth)?
# User Experience
# How does the user experience with different content types influence engagement and conversion rates?
# Are there user experience elements (e.g., call-to-action button size, placement) that correlate with content type success?
# Content Strategy
# What insights can be drawn about the content strategy based on the historical performance of different content types?
# Are there identifiable patterns in the content that leads to high engagement but low conversion, or vice versa?


# Features and target variable
X = df.drop('ContentType', axis=1)
y = df['ContentType']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Predict the content type on the test set
predictions = rf_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
class_report = classification_report(y_test, predictions)

# Print the accuracy and classification report
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(class_report)
