import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import openpyxl
from fpdf import FPDF
from pdf2docx import Converter
import tempfile
import os

# Fonction pour convertir PDF en Word
def convert_pdf_to_word(pdf_file):
    # Créez un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
        tmp_pdf.write(pdf_file.getbuffer())  # Écrivez le contenu du fichier uploadé
        tmp_pdf.close()  # Fermez le fichier pour pouvoir le lire

        # Convertir le fichier temporaire en Word
        word_file = tempfile.NamedTemporaryFile(suffix=".docx", delete=False)
        cv = Converter(tmp_pdf.name)
        cv.convert(word_file.name, start=0, end=None)
        cv.close()
    return word_file.name

# Fonction pour convertir Word en PDF
def convert_word_to_pdf(word_file):
    pdf_filename = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name
    doc = Document(word_file.name)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)

    pdf.output(pdf_filename)
    return pdf_filename

# Fonction pour convertir Excel en PDF
def convert_excel_to_pdf(excel_file):
    pdf_filename = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False).name
    workbook = openpyxl.load_workbook(excel_file.name)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for sheet in workbook.sheetnames:
        ws = workbook[sheet]
        pdf.cell(200, 10, txt=f"Sheet: {sheet}", ln=True)
        for row in ws.iter_rows(values_only=True):
            pdf.cell(200, 10, txt=str(row), ln=True)

    pdf.output(pdf_filename)
    return pdf_filename

# Fonction pour convertir Word en texte
def convert_word_to_text(word_file):
    doc = Document(word_file.name)
    return "\n".join([para.text for para in doc.paragraphs])

# Fonction principale
def main():
    st.title("Convertisseur de Fichiers")
    st.image("./images/convert.jpg", width=200)
    # Upload du fichier
    uploaded_file = st.file_uploader("Choisissez un fichier...", type=["pdf", "docx", "xlsx"])

    if uploaded_file is not None:
        # Sélectionner le format de conversion
        conversion_format = st.selectbox(
            "Convertir en :",
            options=["PDF", "Word", "Texte"]
        )

        # Convertir selon le type de fichier et le format sélectionné
        if conversion_format == "PDF":
            if uploaded_file.name.endswith(".docx"):
                st.write("Conversion Word à PDF...")
                pdf_filename = convert_word_to_pdf(uploaded_file)
                st.success(f"Fichier converti en PDF : {pdf_filename}")
                with open(pdf_filename, 'rb') as f:
                    st.download_button("Télécharger le fichier PDF", f, file_name=os.path.basename(pdf_filename))
            elif uploaded_file.name.endswith(".xlsx"):
                st.write("Conversion Excel à PDF...")
                pdf_filename = convert_excel_to_pdf(uploaded_file)
                st.success(f"Fichier converti en PDF : {pdf_filename}")
                with open(pdf_filename, 'rb') as f:
                    st.download_button("Télécharger le fichier PDF", f, file_name=os.path.basename(pdf_filename))
            else:
                st.error("La conversion PDF n'est pas disponible pour ce format.")

        elif conversion_format == "Word":
            if uploaded_file.name.endswith(".pdf"):
                st.write("Conversion PDF à Word...")
                word_file = convert_pdf_to_word(uploaded_file)
                st.success(f"Fichier converti en Word : {word_file}")
                with open(word_file, 'rb') as f:
                    st.download_button("Télécharger le fichier Word", f, file_name=os.path.basename(word_file))
            else:
                st.error("La conversion Word n'est pas disponible pour ce format.")

        elif conversion_format == "Texte":
            if uploaded_file.name.endswith(".docx"):
                st.write("Conversion Word à Texte...")
                text_data = convert_word_to_text(uploaded_file)
                st.success("Fichier converti en texte !")
                st.text_area("Contenu texte:", value=text_data, height=300)
            else:
                st.error("La conversion en texte n'est pas disponible pour ce format.")

if __name__ == "__main__":
    main()
