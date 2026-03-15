import streamlit as st
import subprocess
from PIL import Image
import os
import time

st.title("Black & White Image Colorization")

uploaded = st.file_uploader("Upload Black & White Image", type=["jpg","png","jpeg"])

if uploaded is not None:

    image = Image.open(uploaded)
    st.image(image, caption="Original Image")

    # save uploaded image
    with open("input.jpg", "wb") as f:
        f.write(uploaded.getbuffer())

    if st.button("Colorize"):

        # delete old output if exists
        if os.path.exists("output.jpg"):
            os.remove("output.jpg")

        subprocess.run(["python", "colorize.py"])

        # small delay to ensure file is written
        time.sleep(1)

        result = Image.open("output.jpg")
        st.image(result, caption="Colorized Image")