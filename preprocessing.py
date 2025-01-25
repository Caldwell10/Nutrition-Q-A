import pandas as pd

#load the dataset
data =pd.read_csv('data/nutrition.csv')

# Select relevant columns
selected_columns=['name','protein', 'carbohydrate', 'fat', 'calories']
nutrition_data=data[selected_columns].copy()

# Display the first few rows
print(nutrition_data.head())

"""
Remove units like g or mg in numerical columns.
Convert these values to floats for calculations and comparisons.
"""

# Remove units and convert to numerical values
for col in ['protein', 'carbohydrate', 'fat', 'calories']:
    # Convert column to string
    nutrition_data[col] = nutrition_data[col].astype(str)

    # Replace alphabetic characters and strip whitespace
    nutrition_data[col]=nutrition_data[col].str.replace(r"[a-zA-Z]", "", regex=True).str.strip()

    # Convert cleaned strings back to numeric values
    nutrition_data[col]=pd.to_numeric(nutrition_data[col], errors='coerce')

# Drop rows with missing or invalid data
nutrition_data= nutrition_data.dropna()

# Reset index
nutrition_data.reset_index(drop=True, inplace=True)

