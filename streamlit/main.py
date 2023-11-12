import pandas as pd
import random

def get_best_outfit(model_id='41085800-02'):
    df = pd.read_csv('../src/data_preprocessed/items_data.csv', index_col ="model")

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
    selected = [
        {"model": "", "max": 0}, #Tops
        {"model": "", "max": 0}, #Bottoms
        {"model": "", "max": 0}, #Footwear
        {"model": "", "max": 0}, #Jewellery
        {"model": "", "max": 0}, #Outerwear
        {"model": "", "max": 0}, #Dresses, jumpsuits and Complete set
        {"model": "", "max": 0}, #Bags
        {"model": "", "max": 0}  #Hats, scarves and gloves
    ]

    selected[cat-1]['model'] = model_id
    selected[cat-1]['max'] = 1

    for index, row in df.iterrows(): 
        row_cat = row['category']
        if (row_cat == 6 and (cat == 1 or cat == 2)):
            continue
        if (cat == 6 and (row_cat == 1 or row_cat == 2)):
            continue
        if (row_cat == cat):
            continue
        
        # tirar al TF
        result = random.uniform(0.0, 1.0)
        if (result > selected[row_cat-1]['max']):
            selected[row_cat-1]['max'] = result
            selected[row_cat-1]['model'] = row.name

    # Return 

    returned_items = []
    for idx, item in enumerate(selected):
        if (idx == 0 or idx == 1) and (selected[5]['max'] > ((selected[5]['max'] + selected[5]['max'])/2)):
            continue
        if idx == 5 and (selected[5]['max'] < ((selected[0]['max'] + selected[1]['max'])/2)):
            continue
        print(item)
        if item['max'] > MIN_OUTPUT:
            returned_items.append(item['model'])

    return returned_items
