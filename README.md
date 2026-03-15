# Image Colorization Using Deep Learning 

Working App Link: https://imagecolorizationapp.streamlit.app/

## Project Description
This project implements an **Convolutional Neural Network(CNN) based Image Colorization system** that automatically converts grayscale (black-and-white) images into colored images using a pretrained deep learning model.

A **CNN (Convolutional Neural Network)** is a type of **deep learning neural network** mainly used to process images, videos, and other grid-like data. It is widely used in computer vision tasks such as image classification, object detection, and facial recognition.

The application provides a simple web interface built with **Streamlit** where users can upload grayscale images and generate colorized outputs instantly.

The goal of this project is to demonstrate how **deep learning techniques can restore color information in grayscale images and historical photographs**.

---

## Technologies Used

### Programming Language
- Python

### Libraries and Frameworks
- OpenCV – Image processing and deep learning inference
- NumPy – Numerical computations and matrix operations
- Streamlit – Web application framework
- Pillow – Image loading and manipulation

---

## Model Used

This project uses the **Image Colorization model by Richard Zhang et al.**

The model predicts the missing **a and b color channels** in the LAB color space using the **L (lightness) channel** from grayscale images.

Model files used:

```
colorization_deploy_v2.prototxt
colorization_release_v2.caffemodel
pts_in_hull.npy
```

---

## How the System Works

The image colorization process follows these steps:

1. **Image Upload**
   - User uploads a grayscale image through the Streamlit interface.

2. **Image Conversion**
   - Image is converted from RGB to **LAB color space**.

3. **Feature Extraction**
   - The **L channel** (grayscale information) is extracted.

4. **Color Prediction**
   - The deep neural network predicts the **a and b color channels**.

5. **Image Reconstruction**
   - Predicted color channels are combined with the original L channel.

6. **Final Output**
   - LAB image is converted back to RGB to produce the colorized result.

---

## Project Structure

```
Image_Colorization_App
│
├── app.py
├── colorize.py
├── requirements.txt
│
├── model
│   ├── colorization_deploy_v2.prototxt
│   ├── colorization_release_v2.caffemodel
│   └── pts_in_hull.npy
│
├── .gitignore
├── .gitattributes
└── README.md
```

### File Description

| File | Description |
|-----|-------------|
| app.py | Streamlit web interface |
| colorize.py | Deep learning colorization logic |
| requirements.txt | Python dependencies |
| model/ | Pretrained model files |

---

## Installation

Clone the repository:

```
git clone https://github.com/RohitKanagala/Image_Colorization_App.git
cd Image_Colorization_App
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Application

```
streamlit run app.py
```

Then open the provided local URL in your browser.

---

## Applications

This technology can be used for:

- Restoring historical black-and-white photographs
- Film restoration
- Image enhancement in computer vision
- AI-based image editing tools

---

## References

1. Zhang, R., Isola, P., & Efros, A. A. (2016).  
   **Colorful Image Colorization**  
   ECCV 2016.

2. Project Page  
   http://richzhang.github.io/colorization/

3. OpenCV Documentation  
   https://docs.opencv.org/

4. Streamlit Documentation  
   https://docs.streamlit.io/



