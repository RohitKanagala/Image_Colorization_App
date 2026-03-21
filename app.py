import streamlit as st
import cv2
import numpy as np
from PIL import Image
from colorize import colorize

st.set_page_config(page_title="AI Image Colorization", layout="centered")

st.title("Black & White Image Colorization")
st.write("Drag & Drop or Browse a Black & White Image to Colorize")

# File uploader (supports drag & drop automatically)
uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"],
    help="Drag and drop or click to upload an image"
)

if uploaded is not None:

    image = Image.open(uploaded).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_column_width=True)

    image_np = np.array(image)

    if st.button("Colorize Image"):

        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        result = colorize(image_np)

        result = cv2.cvtColor((result * 255).astype("uint8"),
                              cv2.COLOR_BGR2RGB)

        with col2:
            st.subheader("Colorized Image")
            st.image(result, use_column_width=True)
