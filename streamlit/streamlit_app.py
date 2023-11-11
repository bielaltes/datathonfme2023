from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import os
from streamlit_image_select import image_select


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


def print_images_generated(
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


def print_images(
    cols,
    image_ids,
):
    return image_select("", get_images(image_ids))

def convert_name(selected_name):


def generate(selected_image):
    image_converted = convert_name(selected_image)
    return deconvert_name()


"""
# Welcome to Mango!

Choosse a product to generate an outfit:
"""


cols = st.columns([1, 1, 1, 1, 1])
images_path = "../data/images/"
images_ids = get_image_ids(images_path)
outfit = []
selected_image = None
size = 12

if "start" not in st.session_state.keys():
    st.session_state["start"] = 0
    start = 0
else:
    start = st.session_state["start"]

selected_image = print_images(cols, images_ids[start : (start + size) : 1])

if st.button(
    "Next Page ->",
    key="NextPage",
    type="primary",
):
    st.session_state["start"] = start + size
    st.rerun()
if st.button(
    "Next Page ->",
    key="NextPage",
    type="primary",
):
    generate(selected_image)
    st.rerun()
