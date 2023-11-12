from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
from PIL import ImageChops
import os
from streamlit_image_select import image_select
from main import get_best_outfit

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
            i = i + 3
        n = n + 1


def print_images(
    images,
):
    return image_select("", images)


def getIndex(images_shown, selected_image):
    i = 0
    for image in images_shown:
        diff = ImageChops.difference(image, selected_image)
        if not diff.getbbox():
            return i
        else:
            i += 1
    return -1


def convert_name(selected_name):
    converted_name = selected_name[0:11].replace("_", "-")
    return converted_name


def deconvert_name(outfit):
    outfit_converted = []
    for product_id in outfit:
        outfit_converted.append(product_id.replace("-", "_") + ".jpg")
    return outfit_converted


def generate(image_ids, index, start):
    image_converted = convert_name(image_ids[index + start])
    print(image_converted)
    outfit = get_best_outfit(image_converted)
    print(outfit)
    st.write(deconvert_name([image_converted]))
    return deconvert_name(outfit)


"""
# Welcome to Minga!

Choose a product to generate a matching outfit:
"""


cols = st.columns([1, 1, 1])
images_path = "../data/images/"
image_ids = get_image_ids(images_path)
# S'HA DE CANVIAR COM AGAFEM LES IMATGES
# VOSALTRES POSEU IMATGES DE MODELS QUE 'NO EXISTEIXEN' FILLS DE PUTA
outfit = []
selected_image = None
size = 12

if "start" not in st.session_state.keys():
    st.session_state["start"] = 0
    start = 0
else:
    start = st.session_state["start"]

if "show_outfit" not in st.session_state.keys() or not st.session_state["show_outfit"]:
    images_shown = get_images(image_ids[start : (start + size) : 1])
    selected_image = print_images(images_shown)

    if start > 0:
        if st.button(
            "<- Previous Page",
            key="PreviousPage",
            type="primary",
        ):
            st.session_state["start"] = start - size
            st.rerun()

    if st.button(
        "Next Page ->",
        key="NextPage",
        type="primary",
    ):
        st.session_state["start"] = start + size
        st.rerun()
    
    if st.button(
        "Generate Outfit",
        key="Generate",
        type="primary",
        use_container_width=True,
    ):
        i = getIndex(images_shown, selected_image)
        st.session_state["outfit"] = generate(image_ids, i, start)
        st.session_state["show_outfit"] = True
        st.rerun()
else:
    print_images_generated(cols, st.session_state["outfit"])
    if st.button(
        "Make an outfit with another product",
        key="ChooseOutfit",
        type="primary",
    ):
        st.session_state["show_outfit"] = False
        st.rerun()
