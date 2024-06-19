import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    upload_image = st.file_uploader("Upload from device")
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

if upload_image:
    img = Image.open(upload_image)
    gray_img = img.convert("L")
    st.image(gray_img)
