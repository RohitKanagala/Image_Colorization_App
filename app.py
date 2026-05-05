import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
from colorize import colorize

st.set_page_config(page_title="Image Colorization", layout="centered")
st.title("Black & White Image Colorization")
st.write("Drag & Drop or Browse a Black & White Image to Colorize")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"],
    help="Drag and drop or click to upload an image"
)
if uploaded is not None:
    image = Image.open(uploaded).convert("RGB")
    image_np = np.array(image)
    generate = st.button("Colorize Image")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, width="stretch")

    with col2:
        st.subheader("Colorized Image")
        result_placeholder = st.empty()
        download_placeholder = st.empty()

    if generate:

        with st.spinner("Colorizing image..."):

            img_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

            result = colorize(img_bgr)

            result = cv2.cvtColor(
                (result * 255).astype("uint8"),
                cv2.COLOR_BGR2RGB
            )

        result_placeholder.image(result, width="stretch")

        result_pil = Image.fromarray(result)
        buf = io.BytesIO()
        result_pil.save(buf, format="PNG")

        download_placeholder.download_button(
            label="Download Colorized Image",
            data=buf.getvalue(),
            file_name="colorized_image.png",
            mime="image/png"
        )
