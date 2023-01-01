import streamlit as st
from PIL import Image

with st.expander("Open to start your camera"):
    uploaded_image = st.camera_input("Camera")

with st.expander("Open to upload a file from your computer"):
    uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)
