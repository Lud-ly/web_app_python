# Script python pour streamlit pour une interface pour détourer des images avec la lib rembg
import streamlit as st

st.title("Mon détoureur d'images")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.download_button("Télécharger", "newImage.png",uploaded_file, mime="image/png")
else:
    st.write("Upload an image")
