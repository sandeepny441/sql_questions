import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Create 12 random numerical entries for each numerical column
num_col1 = np.random.randn(12)
num_col2 = np.random.randn(12)

# Create 12 random binary entries for the categorical column
cat_col = np.random.choice([0, 1], size=12)

# Create a DataFrame with the data
dataset = pd.DataFrame({
    'Numerical_1': num_col1,
    'Numerical_2': num_col2,
    'Categorical_Binary': cat_col
})

print(dataset)




