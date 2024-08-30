import pandas as pd

# Sample DataFrame
data = {
    'productId': [7602, 7848, 7907, 7938, 7966],
    'lifestyles': [
        [{"code": "SNAP", "formattedName": "plant based", "largeImageUrl": "url1", "name": "SNAP EBT ELIGIBLE", "description": "SNAP EBT ELIGIBLE"}],
        [{"code": "SNAP", "formattedName": "SNAP EBT eligible", "largeImageUrl": "url2", "name": "SNAP EBT ELIGIBLE", "description": "SNAP EBT ELIGIBLE"}],
        [{"code": "SNAP", "formattedName": "gluten free", "largeImageUrl": "url3", "name": "gluten free", "description": "SNAP EBT ELIGIBLE"}],
        [{"code": "SNAP", "formattedName": "SNAP EBT eligible", "largeImageUrl": "url4", "name": "SNAP EBT ELIGIBLE", "description": "SNAP EBT ELIGIBLE"}],
        [{"code": "SNAP", "formattedName": "SNAP EBT eligible", "largeImageUrl": "url5", "name": "SNAP EBT ELIGIBLE", "description": "SNAP EBT ELIGIBLE"}]
    ]
}

df = pd.DataFrame(data)

# Function to filter and combine keys
def filter_and_combine_keys(lifestyle_list):
    combined_list = []
    for d in lifestyle_list:
        if 'name' in d:
            combined_list.append(d['name'])
        if 'formattedName' in d:
            combined_list.append(d['formattedName'])
    # Remove duplicates
    combined_list = list(set(combined_list))
    return combined_list

# Apply the function to each row in the 'lifestyles' column
df['lifestyles'] = df['lifestyles'].apply(filter_and_combine_keys)
pd.set_option('display.max_colwidth', None)

# Display the result
df



# Flatten the DataFrame
flattened_data = []
for index, row in df.iterrows():
    product_id = row['productId']
    for lifestyle in row['lifestyles']:
        flattened_data.append({'productId': product_id, 'lifestyle': lifestyle})

flattened_df = pd.DataFrame(flattened_data)

# Display the result
flattened_df


# Flatten the DataFrame
flattened_data = []
for index, row in df.iterrows():
    product_id = row['productId']
    for lifestyle in row['lifestyles']:
        flattened_data.append({'productId': product_id, 'lifestyle': lifestyle})

flattened_df = pd.DataFrame(flattened_data)

# Extract all unique lifestyle values
unique_lifestyles = flattened_df['lifestyle'].unique()

# Filter the DataFrame dynamically (without hardcoding)
filtered_df = flattened_df[flattened_df['lifestyle'].isin(unique_lifestyles)]

filtered_df


# Pivot the DataFrame
pivot_df = filtered_df.pivot_table(index='productId', columns='lifestyle', aggfunc='size', fill_value=0)

# Ensure all expected columns are present, even if they are missing in the filtered DataFrame
for col in unique_lifestyles:
    if col not in pivot_df.columns:
        pivot_df[col] = 0

# Select only 'gluten free' and 'plant based' columns
required_columns = ['gluten free', 'plant based']
for col in required_columns:
    if col not in pivot_df.columns:
        pivot_df[col] = 0

# Filter the pivot_df to include only the required columns
pivot_df = pivot_df[required_columns]

# Reset the index to include 'productId' as a column
pivot_df.reset_index(inplace=True)

pivot_df



