import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
st.write("OpenCV Version:", cv2.__version__)
st.write("Has readNetFromCaffe:", hasattr(cv2.dnn, "readNetFromCaffe"))
from colorize import colorize

st.set_page_config(
    page_title="AI Image Colorizer",
    page_icon=None,
    layout="wide"
)

st.title("AI Black & White Image Colorizer")
st.write("Upload a black & white image and let AI add realistic colors.")

uploaded = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded is not None:

    image = Image.open(uploaded).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

        st.write(f"Image Size: {image.width} × {image.height}")

    if st.button("Colorize Image"):

        with st.spinner("Colorizing... Please wait."):

            try:

                image_np = np.array(image)

                image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

                result = colorize(image_np)

                result = (result * 255).astype(np.uint8)

                result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

                with col2:

                    st.subheader("Colorized Image")

                    st.image(result, use_container_width=True)

                    result_image = Image.fromarray(result)

                    buffer = BytesIO()

                    result_image.save(buffer, format="PNG")

                    st.download_button(
                        label="Download Colorized Image",
                        data=buffer.getvalue(),
                        file_name="colorized_image.png",
                        mime="image/png"
                    )

            except Exception as e:

                st.error(f"Error: {e}")
