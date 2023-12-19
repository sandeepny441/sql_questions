import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Simulating dataset with 'CTAClicks' and 'Converted'
data = {
    'CTAClicks': np.random.poisson(lam=2, size=1000),  # Number of CTA clicks (simulated)
    'Converted': np.random.binomial(n=1, p=0.3, size=1000)  # Whether a conversion occurred (simulated)
}
df = pd.DataFrame(data)
# eda

# Conversion Rate Analysis
# What is the overall conversion rate for the website?
# How does the conversion rate vary with the number of CTA clicks?
# CTA Effectiveness
# Which CTAs have the highest conversion rates?
# Are there CTAs that seem to be underperforming compared to others?
# User Behavior
# Is there a typical number of CTA clicks before a user converts?
# How does user behavior differ between those who convert and those who don't?
# CTA Placement and Design
# Where are the most effective CTAs located on the page (top, middle, bottom)?
# Does the design of the CTA (size, color, text) impact its effectiveness?
# Time Analysis
# How long does it take on average for a user to click a CTA after landing on a page?
# Is there a time decay effect on CTA clicks (do earlier clicks lead to more conversions)?
# Demographics and Segmentation
# Do certain demographic segments have higher conversion rates from CTA clicks?
# How do different user segments interact with CTAs differently?
# Traffic Source Impact
# Does the source of website traffic influence the likelihood of CTA clicks leading to conversion?
# Are users coming from certain channels (organic search, paid ads, email) more likely to convert?
# Page Content
# What type of content (text, video, images) is most commonly associated with high-converting CTAs?
# How does the amount of content on a page relate to the number of CTA clicks and conversions?
# Technical Performance
# Does page speed impact the likelihood of a user clicking a CTA?
# Are there any technical issues that correlate with lower CTA effectiveness?
# Pathway Analysis
# What are the common pathways that lead to a CTA click and subsequent conversion?
# Are there specific pages that act as bottlenecks or hotspots for conversions?
# A/B Testing
# How do changes from A/B tests of CTAs impact conversion rates?
# Which variations of CTAs perform the best in terms of driving conversions?

# Define the features and target variable
X = df[['CTAClicks']]  # Features
y = df['Converted']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize the logistic regression model
logistic_model = LogisticRegression()

# Train the model
logistic_model.fit(X_train, y_train)

# Predict on the test set
logistic_predictions = logistic_model.predict(X_test)

# Evaluate the logistic regression model
logistic_accuracy = accuracy_score(y_test, logistic_predictions)
logistic_report = classification_report(y_test, logistic_predictions)

# Initialize the decision tree model
decision_tree_model = DecisionTreeClassifier()

# Train the model
decision_tree_model.fit(X_train, y_train)

# Predict on the test set
decision_tree_predictions = decision_tree_model.predict(X_test)

# Evaluate the decision tree model
decision_tree_accuracy = accuracy_score(y_test, decision_tree_predictions)
decision_tree_report = classification_report(y_test, decision_tree_predictions)

# Output the evaluation results
print("Logistic Regression Accuracy:", logistic_accuracy)
print("Logistic Regression Classification Report:")
print(logistic_report)
print("\nDecision Tree Accuracy:", decision_tree_accuracy)
print("Decision Tree Classification Report:")
print(decision_tree_report)
