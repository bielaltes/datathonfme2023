from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import os

image_path = "../data/images/"
partial_images = os.listdir(image_path)

col1, col2, col3, col4, col5 = st.columns(5)
img1 = col1.image(Image.open(f'{image_path}{partial_images[0]}'))
img2 = col2.image(Image.open(f'{image_path}{partial_images[1]}'))
img3 = col3.image(Image.open(f'{image_path}{partial_images[2]}'))
img4 = col4.image(Image.open(f'{image_path}{partial_images[3]}'))
img5 = col5.image(Image.open(f'{image_path}{partial_images[4]}'))

i = 0
n = 5

def print_images():
    global img1, img2, img3, img4, img5, i, n, col1, col2, col3, col4, col5
    img1.empty()
    img2.empty()
    img3.empty()
    img4.empty()
    img5.empty()
    for j in range(i, n):
        if j - i == 0:
            img1 = col1.image(Image.open(f'{image_path}{partial_images[j]}'))
        elif j - i == 1:
            img2 = col2.image(Image.open(f'{image_path}{partial_images[j]}'))
        elif j - i == 2:
            img3 = col3.image(Image.open(f'{image_path}{partial_images[j]}'))
        elif j - i == 3:
            img4 = col4.image(Image.open(f'{image_path}{partial_images[j]}'))
        elif j - i == 4:
            img5 = col5.image(Image.open(f'{image_path}{partial_images[j]}'))

more_images = st.button("More clothes")

if (more_images):
    if (n < len(partial_images)):
        i += 5
        n += 5
    print_images()
