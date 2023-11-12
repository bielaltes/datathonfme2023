import pandas as pd
import random

model_id = '41085800-02'
df = pd.read_csv('../data/items_data.csv', index_col ="model")

MIN_OUTPUT = 0.7

""" category_mapping = {
    'EMPTY': 0,
    'Tops': 1,
    'Bottoms': 2,
    'Footwear': 3,
    'Jewellery': 4,
    'Outerwear': 5,
    'Dresses, jumpsuits and Complete set': 6,
    'Bags': 7,
    'Hats, scarves and gloves': 8
} """


cat = df.loc[model_id].category
print(df)
selected = [
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0},
    {"model": "", "max": 0}
]

selected[cat]['model'] = model_id
selected[cat]['max'] = 1

for index, row in df.iterrows(): 
    row_cat = row['category']
    if (row_cat == 6 and (cat == 1 or cat == 2)):
        continue
    if (cat == 6 and (row_cat == 1 or row_cat == 2)):
        continue

    if (row_cat != cat):
        # tirar al TF
        result = random.uniform(0.0, 1.0)
        if (result > selected[row_cat-1]['max']):
            selected[row_cat-1]['max'] = result
            selected[row_cat-1]['model'] = row.name

# Return 

returned_items = []
for item in selected:
    if item['max'] > MIN_OUTPUT:
        returned_items.append(item['model'])

with open("shared_variable.txt", "w") as f: 
    f.write(str(returned_items)) 