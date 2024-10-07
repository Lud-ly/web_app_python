from PIL import Image 
import streamlit as st
from io import BytesIO 
import uuid
from rembg import remove

st.set_page_config(page_title="Détoureur d'images", page_icon="skull", layout="wide")  # Configuration de la page

# Titre et logo de l'application
st.image("./images/logo.png", width=250)
st.write("Ce détoureur d'images est conçu pour supprimer l'arrière-plan d'une image.")

col1, col2 = st.columns(2)

st.write("**Note:** Ce détoureur fonctionne avec les formats PNG, JPG, WEBP et JPEG.")

# Fonction pour convertir l'image traitée en un format téléchargeable
def convert_image_to_downloadable(image):
   thebuf = BytesIO()
   image.save(thebuf, format="PNG")
   byte_in = thebuf.getvalue()
   return byte_in  

# Fonction pour traiter l'image (supprimer l'arrière-plan)
def create_image(image):
    
    # Supprime l'arrière-plan de rembg
    fixed = remove(image) 
    
    # Ouvre l'image téléchargée
    col1.write("Image originale")
    col1.image(image)
    
    # Appliquer mon style personnalisé à la colonne 2
    with col2:
        st.markdown('<div class="custom-column">', unsafe_allow_html=True)
        st.write("Image détourée")
        st.image(fixed)
        st.markdown('</div>', unsafe_allow_html=True)
    
     # Générer un identifiant unique pour le nom de fichier
    unique_id = uuid.uuid4()
    unique_filename = f"pymage_detouree_{unique_id}.png"
    
    st.sidebar.write("\n")
    # Crée un bouton pour télécharger l'image détourée
    st.sidebar.download_button("Télécharger l'image", convert_image_to_downloadable(fixed), unique_filename, 'image/png')

# Chargement du fichier téléversé
image_upload = st.sidebar.file_uploader("Glissez-déposez un fichier ici", type=["png", "jpg", "jpeg","webp"])

# Loader pour indiquer le traitement
if image_upload is not None:
    with st.spinner('Traitement de l\'image en cours...'):
        image = Image.open(image_upload)  # Ouvre l'image téléversée
        create_image(image)  # Passe l'image téléversée à la fonction de traitement
else:
    # Default view
    col1.write("Image originale")
    col1.image(("./images/goat.jpg"), width=350 )
    col2.write("Image détourée")
    col2.image(("./images/dgoat.png"), width=350)