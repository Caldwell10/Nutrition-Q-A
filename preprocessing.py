import pandas as pd

# Load the dataset
data = pd.read_csv('data/nutrition.csv')

# Select relevant columns
selected_columns = ['name', 'protein', 'carbohydrate', 'fat', 'calories']
nutrition_data = data[selected_columns].copy()

# Remove units and convert to numeric values
for col in ['protein', 'carbohydrate', 'fat', 'calories']:
    # Convert to string
    nutrition_data[col] = nutrition_data[col].astype(str)

    # Replace non-numeric characters
    nutrition_data[col] = nutrition_data[col].str.replace(r"[^0-9.]", "", regex=True).str.strip()

    # Convert to numeric
    nutrition_data[col] = pd.to_numeric(nutrition_data[col], errors='coerce')

# Drop rows with missing or invalid values
nutrition_data = nutrition_data.dropna()

# Reset index
nutrition_data.reset_index(drop=True, inplace=True)

print("After Cleaning:")
print(nutrition_data.head())
