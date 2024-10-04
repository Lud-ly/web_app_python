import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError


# Cache data function
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


# Define translations
translations = {
    "en": {
        "choose_countries": "Choose countries",
        "select_error": "Please select at least one country.",
        "title": "Gross Agricultural Production ($B)",
        "connection_error": "**This demo requires internet access.**\nConnection error: %s"
    },
    "fr": {
        "choose_countries": "Choisissez des pays",
        "select_error": "Veuillez sélectionner au moins un pays.",
        "title": "Production agricole brute (milliards $)",
        "connection_error": "**Cette démo nécessite un accès Internet.**\nErreur de connexion : %s"
    }
}

# Language selection
language = st.sidebar.selectbox("Language / Langue", ["English", "Français"])
lang_code = "en" if language == "English" else "fr"

# Try block for internet connection and data fetching
try:
    df = get_UN_data()

    # Country selection
    countries = st.multiselect(
        translations[lang_code]["choose_countries"],
        list(df.index),
        ["China", "United States of America"]
    )

    # Error if no country selected
    if not countries:
        st.error(translations[lang_code]["select_error"])
    else:
        # Data transformation
        data = df.loc[countries]
        data /= 1000000.0
        st.write(f"### {translations[lang_code]['title']}", data.sort_index())

        # Prepare data for chart
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": translations[lang_code]["title"]}
        )

        # Altair chart
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y(f"{translations[lang_code]['title']}:Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)

# Handle connection errors
except URLError as e:
    st.error(translations[lang_code]["connection_error"] % e.reason)
