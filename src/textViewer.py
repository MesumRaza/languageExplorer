# Import the wrapper function from your package
from streamlit_custom_tooltip import st_custom_tooltip
import streamlit as st
from pathlib import Path
import os
import pandas as pd
import re

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

def textViewer():
    _max_width_()
    st.header("Text Viewer")
    loadedDocuments = "data/imported/"
    fileList = os.listdir(loadedDocuments)
    if ".DS_Store" in fileList:
        fileList.remove(".DS_Store")
    if "config.txt" in fileList:
        fileList.remove("config.txt")
    textChooser = st.sidebar.selectbox("Text to view:", options = fileList, index=0)
    # with open(loadedDocuments + textChooser) as text:
    #     sentence = text.read()
    #sentence is now the document
    config = loadedDocuments + "config.txt"
    configFile = pd.read_csv(config, sep="\t", names=["fileName", "attributes"])

    atts = configFile[configFile['fileName'].str.fullmatch(textChooser)].attributes.to_string(header=False,index=False,)

    atts = re.sub("^ ", "", atts)
    listAtts = atts.split(", ")
    attsToShow = listAtts
    attsToShow.remove("word")
    default_atts = attsToShow
    selectedAtts = st.sidebar.multiselect("Attributes to see", attsToShow, default_atts)
    sendAtts = selectedAtts
    sendAtts.insert(0,"index")
    print(sendAtts)
    documentText = pd.read_csv(loadedDocuments + textChooser, sep="\t", names=listAtts)
    #sentence is now the document
    documentText.reset_index(inplace=True)
    jsonDoc = documentText.to_json(orient="index")

    sentence = jsonDoc

    label = ""
    v = st_custom_tooltip(label=label, selectedAttributes=sendAtts, sentence=sentence)
