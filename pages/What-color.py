import streamlit as st
from PIL import Image
import numpy as np
from collections import Counter

def rgb_to_hex(rgb):
    """Convertir RGB en Hex"""
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def get_dominant_colors(image, num_colors=5):
    # Convertir l'image en format RGB
    image = image.convert("RGB")
    # Convertir l'image en tableau numpy
    image_array = np.array(image)
    
    # Reshaping de l'image pour avoir une liste de pixels
    pixels = image_array.reshape(-1, 3)
    
    # Compter les couleurs
    color_counts = Counter(map(tuple, pixels))
    
    # Obtenir les n couleurs les plus courantes
    most_common_colors = color_counts.most_common(num_colors)
    
    # Convertir les couleurs en hexadécimal
    hex_colors = [(rgb_to_hex(color), count) for color, count in most_common_colors]
    
    return hex_colors

# Titre de l'application
st.title("Outil d'Extraction de Couleurs")
st.image("./images/color.png", width=200)
st.write("Téléchargez une image pour obtenir les couleurs dominantes en hexadécimal.")

# Uploader l'image
uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Ouvrir l'image avec PIL
    image = Image.open(uploaded_file)
    
    # Afficher l'image
    st.image(image, caption='Image Téléchargée.', use_column_width=True, width=250)
    
    # Extraire les couleurs dominantes
    dominant_colors = get_dominant_colors(image)
    
    # Afficher les couleurs dominantes
    st.write("Couleurs Dominantes:")
    
    for hex_color, count in dominant_colors:
        st.write(f"Couleur: {hex_color}")
        # Afficher la couleur
        st.markdown(
            f"<div style='background-color: {hex_color}; width: 100px; height: 50px;'></div>", 
            unsafe_allow_html=True
        )
