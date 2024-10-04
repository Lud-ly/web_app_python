from PIL import Image  # Bibliothèque pour ouvrir et manipuler des images
import streamlit as st  # Framework pour créer des applications web interactives
from io import BytesIO  # Permet de gérer les flux de données en mémoire (utile pour l'enregistrement d'images)
from rembg import remove  # Bibliothèque pour supprimer l'arrière-plan des images

st.set_page_config(page_title="Détoureur d'images", page_icon="skull", layout="centered")  # Configuration de la page

# Titre de l'application
st.sidebar.title("Mon détoureur d'images")
st.write("Ce détoureur d'images est conçu pour supprimer l'arrière-plan d'une image.")

col1, col2 = st.columns(2)

st.write("**Note:** Ce détoureur fonctionne avec les formats PNG, JPG et JPEG.")

# Fonction pour convertir l'image traitée en un format téléchargeable
def convert_image_to_downloadable(image):
   buf = BytesIO()
   image.save(buf, format="PNG")
   byte_in = buf.getvalue()
   return byte_in  

# Fonction pour traiter l'image (supprimer l'arrière-plan)
def fix_image(image):
    # Ouvre l'image téléchargée ou par défaut
    col1.write("Image originale")
    col1.image(image)
    fixed = remove(image)  # Supprime l'arrière-plan
    col2.write("Image détourée")
    col2.image(fixed)
    
    st.sidebar.write("\n")
    # Crée un bouton pour télécharger l'image détourée
    st.sidebar.download_button("Télécharger l'image", convert_image_to_downloadable(fixed), 'image_detouree.png', 'image/png')

# Chargement du fichier téléversé
image_upload = st.sidebar.file_uploader("Glissez-déposez un fichier ici", type=["png", "jpg", "jpeg"])

# Loader pour indiquer le traitement
with st.spinner('Traitement de l\'image en cours...'):
    if image_upload:
        image = Image.open(image_upload)  # Ouvre l'image téléversée
        fix_image(image)  # Passe l'image téléversée à la fonction de traitement
    else:
        image = Image.open("./images/goat.jpg") 
        default_image = Image.open("./images/dgoat.png")
        col1.write("Image originale")
        col1.image(image)
        col2.write("Image détourée")
        col2.image(default_image)
