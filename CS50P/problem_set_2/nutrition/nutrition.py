import pandas as pd

# Get data
url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"
data = pd.read_html(url)
data = data[0]

# Build dataframe
df = data.iloc[:, [0,1]]
df.columns = ["fruits", "calories"]

# Get items
fruits = []
for row in df["fruits"]:
    fruit = row.partition(" ")[0]
    fruits.append(fruit)
       
calories = list(df["calories"])

# Rename some fruits
fruits[17] = "Sweet Cherries"

# Put in dictionary
keys = fruits
values = calories
dictionary = dict(zip(keys, values))


# Convert fruits to calories
fruit = input("Item: ").casefold().capitalize()
print("Calories: ", dictionary[fruit])