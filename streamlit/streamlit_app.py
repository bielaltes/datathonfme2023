from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import os


def print_images(
    cols,
    images_ids,
    start,
    size
):
    images = list(
        map(
            lambda id: Image.open(f"{images_path}{id}"),
            images_ids[start:(start + size):1],
        )
    )
    n = 0
    for col in cols:
        i = n
        while i < 15:
            with col:
                st.image(images[i])
            i = i + 5
        n = n + 1

"""
# Welcome to Mango!

Choosse a product to generate an outfit:
"""


cols = st.columns([1, 1, 1, 1, 1])
images_path = "../data/images/"

images_ids = os.listdir(f"{images_path}")
# images_generated = []
# images_generated_ids = [
#     "2019_41005828_05",
#     "2019_41017020_08",
#     "2019_41025020_02",
#     "2019_41025782_23",
#     "2024_67050279_CO",
# ]
# for image_id in images_generated_ids:
#     images_generated.append(Image.open(f"{images_path}{image_id}.jpg"))
size = 15
if 'start' not in st.session_state.keys():
    st.session_state['start'] = 0
if st.button(
    "Next Page ->",
    type="primary",
):
    st.session_state['start'] = st.session_state['start']+size

print_images(cols, images_ids, st.session_state['start'], size)

# st.button("Generate", type="primary")
# for col in cols:
#     i = n
#     while i < len(images_generated):
#         with col:
#             st.image(images_generated[i], width=100)
#         i = i + 5
#     n = n + 1