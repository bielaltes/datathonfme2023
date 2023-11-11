from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import os


@st.cache_data
def get_image_ids(images_path):
    return os.listdir(f"{images_path}")


def get_images(image_ids):
    return list(
        map(
            lambda id: Image.open(f"{images_path}{id}"),
            image_ids,
        )
    )


def print_images(
    cols,
    image_ids,
):
    images = get_images(image_ids)
    size = len(images)
    n = 0
    for col in cols:
        i = n
        while i < size:
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
images_ids = get_image_ids(images_path)
outfit = []
selected_image = None
size = 15

if "start" not in st.session_state.keys():
    st.session_state["start"] = 15
    start = 0
else:
    start = st.session_state["start"]

print_images(cols, images_ids[start : (start + size) : 1])

if st.button(
    "Next Page ->",
    type="primary",
):
    st.session_state["start"] = start + size
