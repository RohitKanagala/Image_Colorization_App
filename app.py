import streamlit as st
import subprocess
from PIL import Image

st.title("AI Image Colorization")

uploaded = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded is not None:

    image = Image.open(uploaded)
    st.image(image, caption="Original Image")

    with open("input.jpg", "wb") as f:
        f.write(uploaded.getbuffer())

    if st.button("Colorize"):

        subprocess.run(["python", "colorize.py"])

        result = Image.open("output.jpg")
        st.image(result, caption="Colorized Image")