from preprocessing import nutrition_data
"""
The text documents represent the raw knowledge base of your system. They contain the information (e.g., nutritional data) that users will query
Example:Cornstarch: Contains 0.26g of protein, 91.27g of carbohydrates, 0.05g of fat, and 381 calories.
"""

# Convert rows to descriptive text
docs = nutrition_data.apply(
    lambda row: f"{row['name']}: Contains {row['protein']}g of protein, "
                f"{row['carbohydrate']}g of carbohydrate, {row['fat']}g of fat"
                f" and {row['calories']}g of calories.", axis=1).tolist()

with open("data/nutrition_documents.txt", "w") as file:
    for doc in docs:
        file.write(doc + "\n")



