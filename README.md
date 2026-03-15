# Image_Colorization_App
Find the working of app: https://imagecolorizationapp.streamlit.app/

# Project Description

This project implements an AI-based Image Colorization system that automatically converts grayscale (black-and-white) images into colored images. The application uses a pretrained Convolutional Neural Network (CNN) model to predict color information from grayscale images.

A simple web interface built with Streamlit allows users to upload grayscale images and generate colorized outputs instantly.

The goal of this project is to demonstrate how deep learning techniques can be used to restore color information in historical photographs or grayscale images.

# Technologies Used
Programming Language

Python

# Libraries and Frameworks

OpenCV – Used for image processing and deep learning model inference

NumPy – Used for array and matrix operations

Streamlit – Used to create the web interface

Pillow – Used for image handling and conversion

# Model Used

The project uses the pretrained Image Colorization model developed by Richard Zhang et al.

The model is trained to predict the ab color channels in the LAB color space from the L (lightness) channel of grayscale images.

# Model files used in this project:

colorization_deploy_v2.prototxt
colorization_release_v2.caffemodel
pts_in_hull.npy

These files contain the network architecture and pretrained weights.

# How the System Works

The image colorization process follows these steps:

1. Image Upload

The user uploads a grayscale image through the Streamlit web interface.

2. Image Conversion

The image is converted from RGB to LAB color space.

LAB color space separates:

L channel → Lightness

a channel → Green-Red color

b channel → Blue-Yellow color

3. Feature Extraction

The L channel (grayscale information) is passed to the deep neural network.

4. Color Prediction

The CNN model predicts the missing a and b color channels.

5. Image Reconstruction

The predicted a and b channels are combined with the original L channel.

6. Final Output

The LAB image is converted back to RGB format to produce the final colorized image.


# Project Structure
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

# Applications

This technology can be used for:

Restoring historical black-and-white photographs

Film restoration

Image enhancement in computer vision

AI-based image editing tools

# References

Richard Zhang, Phillip Isola, Alexei A. Efros
“Colorful Image Colorization”
ECCV 2016

Zhang et al. Project Page
http://richzhang.github.io/colorization/

OpenCV Deep Learning Module Documentation
https://docs.opencv.org/

Streamlit Documentation
https://docs.streamlit.io/
