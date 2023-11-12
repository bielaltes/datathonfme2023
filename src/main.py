import pandas as pd

model_id = ''
df = pd.read_csv('items_data.csv')

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


cat = df.iloc['model' == model_id]['category']
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
        result = bimbimbambam
        if (result > selected[row_cat]['max']):
            selected[row_cat]['max'] = result
            selected[row_cat]['model'] = row['model']

# Return 

returned_items = []
for item in selected:
    if item['max'] > MIN_OUTPUT:
        returned_items.append(item['model'])

return returned_items