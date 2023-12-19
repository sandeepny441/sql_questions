from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Loading the dataset from the file
file_path = '/mnt/data/best_datas_dummy_dataset.csv'
df = pd.read_csv(file_path)

# Preprocessing
# Encoding categorical variables
categorical_features = ['Category', 'CampaignType', 'UserSegment', 'StockAvailability', 'Season']
numeric_features = ['Price', 'Discount', 'HistoricalLikes', 'HistoricalDislikes', 'ReviewScore', 'NumberReviews', 'SalesLastMonth']

# Pipeline for transforming categorical variables
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Pipeline for scaling numerical variables
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

# Combining preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
===========================================================================
# EDA Questions:
-------------------------------------------------------------------------
# Distribution Questions:

# What is the distribution of the historical likes count for different product categories?
# How is the price distributed across different campaign types and does it influence likes?

import matplotlib.pyplot as plt
import seaborn as sns

# For the purposes of this code, we will assume that the dataset contains 'HistoricalLikes', 'Category', and 'CampaignType' features.

# Sample data generation for 'HistoricalLikes', 'Category', and 'CampaignType'
# This is just simulated data and does not represent real information
data = {
    'HistoricalLikes': np.random.poisson(lam=100, size=num_records),
    'Category': np.random.choice(['Electronics', 'Appliances', 'Games', 'Computers', 'Mobile'], size=num_records),
    'CampaignType': np.random.choice(['Email', 'Social Media', 'In-store', 'Online Ads', 'TV Commercials'], size=num_records),
    'Price': np.random.uniform(50, 500, size=num_records)  # Prices between $50 and $500
}

df = pd.DataFrame(data)

# Plotting the distribution of historical likes count for different product categories
plt.figure(figsize=(12, 6))
sns.boxplot(x='Category', y='HistoricalLikes', data=df)
plt.title('Distribution of Historical Likes Count by Product Category')
plt.ylabel('Historical Likes Count')
plt.xlabel('Product Category')
plt.show()

# Plotting the distribution of price across different campaign types
plt.figure(figsize=(12, 6))
sns.boxplot(x='CampaignType', y='Price', data=df)
plt.title('Price Distribution Across Different Campaign Types')
plt.ylabel('Price')
plt.xlabel('Campaign Type')
plt.show()

# Trend Questions:

# Is there a trend in likes count over the months or seasons captured in the dataset?
# How have sales last month influenced the historical likes?

# Simulating additional data for 'Month', 'Season', and 'SalesLastMonth' to demonstrate EDA for the new questions.

# Generate 'Month' and 'Season' data
months = np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], num_records)
seasons = np.random.choice(['Spring', 'Summer', 'Fall', 'Winter'], num_records)

# Generate 'SalesLastMonth' data
sales_last_month = np.random.randint(50, 200, num_records)  # Random sales numbers between 50 and 200

# Add the new columns to the dataframe
df['Month'] = months
df['Season'] = seasons
df['SalesLastMonth'] = sales_last_month

# EDA for trend in likes count over the months
plt.figure(figsize=(14, 7))
sns.lineplot(x='Month', y='HistoricalLikes', data=df, estimator=np.mean, ci=None, sort=False)
plt.title('Trend of Likes Count Over the Months')
plt.ylabel('Average Historical Likes Count')
plt.xlabel('Month')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# EDA for influence of sales last month on historical likes
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SalesLastMonth', y='HistoricalLikes', data=df)
plt.title('Relationship Between Sales Last Month and Historical Likes')
plt.xlabel('Sales Last Month')
plt.ylabel('Historical Likes Count')
plt.show()


# Correlation Questions:

# Which features are most strongly correlated with the projected likes count?
# Is there a correlation between discount levels and likes count?
# Simulating additional 'ProjectedLikes' and 'Discount' data for the correlation analysis.

# Generate 'ProjectedLikes' data (simulated based on historical likes with some random noise)
df['ProjectedLikes'] = df['HistoricalLikes'] + np.random.randint(-10, 10, num_records)

# Generate 'Discount' data (random discounts between 0% and 50%)
df['Discount'] = np.random.uniform(0, 0.5, num_records)

# EDA for correlation of features with projected likes count
# We will use a heatmap to visualize the correlation matrix
correlation_matrix = df[['HistoricalLikes', 'Price', 'SalesLastMonth', 'ProjectedLikes', 'Discount']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Features with Projected Likes Count')
plt.show()

# Since we are specifically interested in the correlation between discount levels and likes count,
# we extract those specific correlation coefficients
discount_likes_correlation = correlation_matrix.loc['Discount', 'HistoricalLikes']
discount_projected_likes_correlation = correlation_matrix.loc['Discount', 'ProjectedLikes']

(discount_likes_correlation, discount_projected_likes_correlation)


# Comparative Questions:

# How do likes vary between different user segments?
# Are there significant differences in review scores across different stock availability statuses?
# Simulating 'UserSegment' and 'StockAvailability' data for the EDA questions

# Generate 'UserSegment' and 'StockAvailability' data
df['UserSegment'] = np.random.choice(['New Customer', 'Returning Customer', 'Loyal Customer', 'Window Shopper'], num_records)
df['StockAvailability'] = np.random.choice(['In Stock', 'Out of Stock', 'Limited Stock'], num_records)
df['ReviewScore'] = np.random.uniform(1, 5, num_records)  # Review scores between 1 and 5

# EDA for how likes vary between different user segments
plt.figure(figsize=(12, 6))
sns.boxplot(x='UserSegment', y='HistoricalLikes', data=df)
plt.title('Distribution of Historical Likes by User Segment')
plt.xlabel('User Segment')
plt.ylabel('Historical Likes Count')
plt.show()

# EDA for differences in review scores across different stock availability statuses
plt.figure(figsize=(12, 6))
sns.boxplot(x='StockAvailability', y='ReviewScore', data=df)
plt.title('Review Scores by Stock Availability Status')
plt.xlabel('Stock Availability')
plt.ylabel('Review Score')
plt.show()


# Outliers Questions:

# Are there any outliers in the historical likes or sales data that could influence the model?
# What are the characteristics of products that have an exceptionally high or low number of reviews?
# Simulating additional 'NumberReviews' data for the EDA questions
df['NumberReviews'] = np.random.randint(0, 500, num_records)  # Random number of reviews between 0 and 500

# EDA for outliers in historical likes or sales data
plt.figure(figsize=(14, 7))
sns.boxplot(x='HistoricalLikes', data=df)
plt.title('Boxplot for Historical Likes to Identify Outliers')
plt.xlabel('Historical Likes Count')
plt.show()

plt.figure(figsize=(14, 7))
sns.boxplot(x='SalesLastMonth', data=df)
plt.title('Boxplot for Sales Last Month to Identify Outliers')
plt.xlabel('Sales Last Month')
plt.show()

# EDA for characteristics of products with high or low number of reviews
# For the purpose of identifying characteristics, we'll consider high and low to be above and below the 75th and 25th percentiles, respectively.
high_review_threshold = df['NumberReviews'].quantile(0.75)
low_review_threshold = df['NumberReviews'].quantile(0.25)

high_reviews_df = df[df['NumberReviews'] > high_review_threshold]
low_reviews_df = df[df['NumberReviews'] < low_review_threshold]

# We can now describe these subsets to find their characteristics.
high_reviews_characteristics = high_reviews_df.describe()
low_reviews_characteristics = low_reviews_df.describe()

(high_reviews_characteristics, low_reviews_characteristics)




# Categorical Data Questions:

# Which product category receives the highest average likes?
# What is the average number of likes per campaign type?
# Assuming the 'Category' and 'CampaignType' columns exist in our simulated dataframe and contain categorical data,
# we will calculate the average likes for these categorical features.

# Calculate the highest average likes by product category
average_likes_by_category = df.groupby('Category')['HistoricalLikes'].mean().sort_values(ascending=False)

# Calculate the average number of likes per campaign type
average_likes_by_campaign = df.groupby('CampaignType')['HistoricalLikes'].mean().sort_values(ascending=False)

# Visualize the highest average likes by product category
plt.figure(figsize=(12, 6))
average_likes_by_category.plot(kind='bar', color='skyblue')
plt.title('Average Historical Likes by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Historical Likes')
plt.show()

# Visualize the average number of likes per campaign type
plt.figure(figsize=(12, 6))
average_likes_by_campaign.plot(kind='bar', color='lightgreen')
plt.title('Average Historical Likes by Campaign Type')
plt.xlabel('Campaign Type')
plt.ylabel('Average Historical Likes')
plt.show()

(average_likes_by_category, average_likes_by_campaign)

# Cross-Feature Interaction Questions:

# Is there an interaction effect between discount and category on the number of likes?
# How does the combination of user segment and campaign type affect likes count?
# To analyze the interaction effects, we'll use grouped bar plots to visualize the impact of combinations of features on likes count.

# Interaction effect between discount and category on the number of likes
# For visualization, we'll categorize the discount into bins (e.g., Low, Medium, High)
df['DiscountCategory'] = pd.qcut(df['Discount'], q=3, labels=['Low', 'Medium', 'High'])

# Grouping data by category and discount category for average likes
category_discount_interaction = df.groupby(['Category', 'DiscountCategory'])['HistoricalLikes'].mean().unstack()

# Plotting the interaction effect
plt.figure(figsize=(12, 6))
category_discount_interaction.plot(kind='bar')
plt.title('Interaction Effect of Discount and Category on Likes Count')
plt.xlabel('Product Category')
plt.ylabel('Average Historical Likes')
plt.legend(title='Discount Category')
plt.show()

# Interaction effect of user segment and campaign type on likes count
user_campaign_interaction = df.groupby(['UserSegment', 'CampaignType'])['HistoricalLikes'].mean().unstack()

# Plotting the interaction effect
plt.figure(figsize=(12, 6))
user_campaign_interaction.plot(kind='bar')
plt.title('Interaction Effect of User Segment and Campaign Type on Likes Count')
plt.xlabel('User Segment')
plt.ylabel('Average Historical Likes')
plt.legend(title='Campaign Type')
plt.show()

# Returning the grouped data for detailed inspection
(category_discount_interaction, user_campaign_interaction)


# Review-Related Questions:

# Is there a relationship between the number of reviews a product has and the number of likes?
# Do products with higher review scores tend to receive more likes?
# To analyze the relationship between review-related features and likes, we'll use scatter plots.

# Scatter plot for the relationship between the number of reviews and the number of likes
plt.figure(figsize=(10, 6))
sns.scatterplot(x='NumberReviews', y='HistoricalLikes', data=df)
plt.title('Relationship Between Number of Reviews and Historical Likes')
plt.xlabel('Number of Reviews')
plt.ylabel('Historical Likes Count')
plt.show()

# Scatter plot for the relationship between review scores and the number of likes
plt.figure(figsize=(10, 6))
sns.scatterplot(x='ReviewScore', y='HistoricalLikes', data=df)
plt.title('Relationship Between Review Scores and Historical Likes')
plt.xlabel('Review Score')
plt.ylabel('Historical Likes Count')
plt.show()

# To quantify these relationships, we can calculate the correlation coefficients
review_likes_correlation = df['NumberReviews'].corr(df['HistoricalLikes'])
score_likes_correlation = df['ReviewScore'].corr(df['HistoricalLikes'])

(review_likes_correlation, score_likes_correlation)


# Price Sensitivity Questions:

# Is there a price point at which likes tend to increase or decrease notably?
# How does the price elasticity affect the likes for products in different categories?
# To analyze price sensitivity questions, we'll use scatter plots and line plots.

# Scatter plot for the relationship between price and likes count
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='HistoricalLikes', data=df)
plt.title('Relationship Between Price and Historical Likes')
plt.xlabel('Price')
plt.ylabel('Historical Likes Count')
plt.show()

# To determine if there's a price point where likes increase or decrease notably, we'll group the data by price ranges and calculate the average likes.
df['PriceRange'] = pd.qcut(df['Price'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
price_likes_grouped = df.groupby('PriceRange')['HistoricalLikes'].mean()

# Line plot for average likes across different price ranges
plt.figure(figsize=(10, 6))
price_likes_grouped.plot(kind='line', marker='o')
plt.title('Average Historical Likes Across Different Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Average Historical Likes')
plt.show()

# Analyzing price elasticity effect on likes for different categories
# We calculate the average likes for each category within each price range
category_price_likes = df.groupby(['Category', 'PriceRange'])['HistoricalLikes'].mean().unstack()

# Plotting the interaction effect
plt.figure(figsize=(12, 6))
category_price_likes.plot(kind='line', marker='o')
plt.title('Effect of Price on Historical Likes for Different Categories')
plt.xlabel('Price Range')
plt.ylabel('Average Historical Likes')
plt.legend(title='Price Range', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

(price_likes_grouped, category_price_likes)


# Stock Availability Questions:

# How does stock availability correlate with likes?
# Are products that are frequently out of stock receiving more likes due to scarcity?
# To analyze stock availability questions, we'll use a bar plot to visualize the relationship with likes.

# Bar plot for average likes based on stock availability
average_likes_by_stock = df.groupby('StockAvailability')['HistoricalLikes'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
average_likes_by_stock.plot(kind='bar', color='coral')
plt.title('Average Historical Likes by Stock Availability')
plt.xlabel('Stock Availability')
plt.ylabel('Average Historical Likes')
plt.show()

# To further investigate whether products that are frequently out of stock receive more likes due to scarcity,
# we can check if there's a notable difference in likes between frequently and rarely out-of-stock products.
# For this, we'll assume a product is frequently out of stock if it appears in the 'Out of Stock' or 'Limited Stock' category more often than 'In Stock'.

# Grouping data to see how often each product is out of stock
stock_frequency = df.groupby('Category')['StockAvailability'].value_counts(normalize=True).unstack()

# Assuming that a category is frequently out of stock if the combined percentage of 'Out of Stock' and 'Limited Stock' is greater than 'In Stock'
frequently_out_of_stock_categories = stock_frequency[(stock_frequency['Out of Stock'] + stock_frequency['Limited Stock']) > stock_frequency['In Stock']]

# Average likes for frequently out of stock categories
average_likes_frequent_out_of_stock = df[df['Category'].isin(frequently_out_of_stock_categories.index)].groupby('Category')['HistoricalLikes'].mean()

(average_likes_by_stock, frequently_out_of_stock_categories, average_likes_frequent_out_of_stock)




# These questions can guide the visual and statistical EDA process, helping you to uncover insights, inform feature engineering, and hypothesis generation for model development. Visualization techniques like histograms, box plots, scatter plots, and heatmaps can be particularly useful in this exploration.
===========================================================================

# Define the target variable
target = 'ProjectedLikes'

# Split the data into training and test sets
X = df.drop(columns=[target, 'ProductID', 'ProductName', 'ReleaseYear'])
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Defining the models to be trained
models = {
    'LinearRegression': LinearRegression(),
    'RandomForestRegressor': RandomForestRegressor(random_state=0)
}

# Placeholder for the best model and its name
best_model = None
best_model_name = ""
best_score = float('-inf')

# Train and evaluate models
for model_name, model in models.items():
    # Create a pipeline that first preprocessed the data then trains the model
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)])
    
    # Train the model
    pipeline.fit(X_train, y_train)
    
    # Evaluate the model
    scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    mean_score = -scores.mean()
    
    if mean_score > best_score:
        best_score = mean_score
        best_model = pipeline
        best_model_name = model_name
    
    print(f"{model_name} cross-validation MSE: {mean_score}")

# Output the best model
print(f"Best model is {best_model_name} with MSE: {best_score}")

# Evaluate the best model on the test set
y_pred = best_model.predict(X_test)
test_mse = mean_squared_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)

print(f"Test MSE: {test_mse}")
print(f"Test R-squared: {test_r2}")
