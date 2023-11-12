import pandas as pd
import random
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D
import tensorflow as tf
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split



def getProcesedImg(ruta):
    img_path = '../datathon/' + ruta
    img = Image.open(img_path)
    img = img.resize((100, 140))
    img_array1 = np.array(img) / 255.0
    return img_array1

def get_best_outfit(model_id='41085800-02'):

    df = pd.read_csv('../src/data_preprocessed/items_data.csv', index_col ="model")
    df.sample(frac=1)
    MIN_OUTPUT = 0.75

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

    i = 0
    for index, row in df.iterrows(): 
        row_cat = row['category']
        if (row_cat == 6 and (cat == 1 or cat == 2)):
            continue
        if (cat == 6 and (row_cat == 1 or row_cat == 2)):
            continue
        if (row_cat == cat):
            continue
        
        # tirar al TF
        model = tf.keras.models.load_model('../src/model')

        new_row = {
        'color1': df.loc[model_id].color, 
        'fabric1':  df.loc[model_id].fabric,  
        'category1': df.loc[model_id].category,
        'color2': row['color'], 
        'fabric2':  row['fabric'],  
        'category2': row['category'],
        }

        numerical_features = pd.DataFrame(new_row, index=[0]).values.tolist()[0]
        input = [   np.expand_dims(getProcesedImg(df.loc[model_id].image), axis=0),     np.expand_dims(getProcesedImg(row['image']), axis=0), np.expand_dims(np.asarray(numerical_features).astype(np.float32), axis=0)  ] 
        result = model.predict(input)

        if (result > selected[row_cat-1]['max']):
            selected[row_cat-1]['max'] = result
            selected[row_cat-1]['model'] = row.name
        
        i += 1
        if i > 400:
            break
        print(i)

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
