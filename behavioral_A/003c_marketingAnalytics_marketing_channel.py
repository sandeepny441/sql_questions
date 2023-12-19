import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Simulating dataset
np.random.seed(0)  # Seed for reproducibility
data_size = 1000
df = pd.DataFrame({
    'Age': np.random.randint(18, 65, size=data_size),  # User age
    'Gender': np.random.choice(['Male', 'Female'], size=data_size),  # User gender
    'InteractionHistory': np.random.poisson(5, size=data_size),  # Number of past interactions
    'MarketingChannel': np.random.choice(['Email', 'PPC', 'Display', 'Social Media'], size=data_size)  # Marketing channel
})

# Convert categorical data to numerical using one-hot encoding
categorical_features = ['Gender', 'MarketingChannel']
numeric_features = ['Age', 'InteractionHistory']


# EDA

# Understanding Marketing Channel Effectiveness
# What is the distribution of conversions across different marketing channels (e.g., email, PPC, display, social media)?
# How do user demographics relate to the preferred marketing channels?
# User Demographics and Channel Preference
# Are certain age groups more responsive to specific marketing channels?
# Does gender play a role in the effectiveness of different marketing channels?
# Interaction History
# How does a user's interaction history correlate with their response to marketing channels?
# Are users with more interactions more likely to be influenced by certain types of marketing?
# Channel Engagement
# Which marketing channels have the highest engagement rates?
# Do specific channels lead to more conversions than others?
# Temporal Trends
# Are there seasonal patterns in marketing channel effectiveness?
# How do trends in marketing channel performance evolve over time?
# Channel and Content Type Relationship
# Does the content type (image, video, text) used in marketing campaigns affect the channel effectiveness?
# Are there specific combinations of content type and channel that result in higher engagement or conversion rates?
# Conversion Pathways
# What are the common pathways or sequences of marketing channel interactions that lead to a conversion?
# Is there a typical 'time to conversion' for different channels?
# ROI Analysis
# Which marketing channels are most cost-effective in terms of ROI?
# How does the cost per acquisition compare across different channels?
# Behavioral Patterns
# Are there identifiable user behaviors that predict success in a particular marketing channel?
# Do users exhibit channel loyalty, preferring to engage with the brand through specific channels consistently?
# Traffic Source Impact
# How does the original source of website traffic (organic, referral, direct) influence the effectiveness of subsequent marketing channels?
# Are certain marketing channels more effective at retaining users originally acquired through other channels?
# Technical Aspects
# Does the technical performance of ad delivery (e.g., ad load times) influence marketing channel effectiveness?
# Are there technical improvements that could enhance the performance of specific channels?
# Multichannel Interactions
# How do interactions with multiple channels impact overall engagement and conversion rates?
# Are users who engage with multichannel campaigns more valuable in terms of LTV?


# Preprocessing for categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Prepare features and target variable
X = df.drop('MarketingChannel', axis=1)
y = df['MarketingChannel']

# Encode the target variable
y = pd.factorize(y)[0]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with preprocessing and classifier
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))])

# Train the Random Forest classifier
pipeline.fit(X_train, y_train)

# Predict the marketing channel on the test set
predictions = pipeline.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
class_report = classification_report(y_test, predictions)

# Print the accuracy and classification report
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(class_report)
