import streamlit as st
import cv2
import numpy as np
from PIL import Image
from colorize import colorize

st.title("AI Image Colorization")

uploaded = st.file_uploader("Upload Black & White Image", type=["jpg","png","jpeg"])

if uploaded is not None:

    image = Image.open(uploaded).convert("RGB")

    st.subheader("Original Image")
    st.image(image)

    image = np.array(image)

    if st.button("Colorize Image"):

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        result = colorize(image)

        result = cv2.cvtColor((result*255).astype("uint8"), cv2.COLOR_BGR2RGB)

        st.subheader("Colorized Image")
        st.image(result)
