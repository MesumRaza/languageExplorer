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
    st.sidebar.markdown("***")
    _max_width_()
    loadedDocuments = "data/imported/"
    oloadedDocuments = loadedDocuments
    fileList = [f for f in os.listdir(loadedDocuments) if os.path.isdir(os.path.join(loadedDocuments, f))]
    try:
        fileList.sort(key=int)
    except:
        fileList.sort()
    fileList.insert(0,"")
    if ".DS_Store" in fileList:
        fileList.remove(".DS_Store")
    if "config.txt" in fileList:
        fileList.remove("config.txt")
    textChooser = st.sidebar.selectbox("Document to view:", options = fileList)
    if textChooser == "":
        secondFileList = [f for f in os.listdir(loadedDocuments) if os.path.isfile(os.path.join(loadedDocuments, f))]
        if ".DS_Store" in secondFileList:
            secondFileList.remove(".DS_Store")
        if "config.txt" in secondFileList:
            secondFileList.remove("config.txt")
        try:
            secondFileList.sort(key=int)
        except:
            secondFileList.sort()
        subTextChooser = st.sidebar.selectbox("Text to view:", options = secondFileList)
        findInConfig = subTextChooser
    else:
        subdirectory = loadedDocuments + textChooser
        secondFileList = [f for f in os.listdir(subdirectory) if os.path.isfile(os.path.join(subdirectory, f))]
        if ".DS_Store" in secondFileList:
            secondFileList.remove(".DS_Store")
        if "config.txt" in secondFileList:
            secondFileList.remove("config.txt")
        loadedDocuments = loadedDocuments + textChooser + "/"
        try:
            secondFileList.sort(key=int)
        except:
            secondFileList.sort()
        subTextChooser = st.sidebar.selectbox("Subtext to view:", options = secondFileList)
        findInConfig = "subtextof" + textChooser
        print(findInConfig)


    # with open(loadedDocuments + textChooser) as text:
    #     sentence = text.read()
    #sentence is now the document
    config = oloadedDocuments + "config.txt"
    configFile = pd.read_csv(config, sep="\t", names=["fileName", "attributes"])

    atts = configFile[configFile['fileName'].str.fullmatch(findInConfig)].attributes.to_string(header=False,index=False,)

    atts = re.sub("^ ", "", atts)
    listAtts = atts.split(", ")
    attsToShow = listAtts
    attsToShow.remove("word")
    default_atts = attsToShow
    selectedAtts = st.sidebar.multiselect("Attributes to see", attsToShow, default_atts)
    sendAtts = selectedAtts
    sendAtts.insert(0,"index")
    documentText = pd.read_csv(loadedDocuments + subTextChooser, sep="\t", names=listAtts)
    #sentence is now the document
    documentText.reset_index(inplace=True)
    jsonDoc = documentText.to_json(orient="index")

    sentence = jsonDoc

    label = ""
    textSize = st.sidebar.slider("Font Size", min_value=14, max_value=36, value=24)

    st.sidebar.markdown("***")
    st.sidebar.markdown("The Greek New Testament texts used here are based on the OpenGNT, [available here](https://github.com/eliranwong/OpenGNT)")
    if textChooser == "":
        st.header(subTextChooser)
    else:
        st.header(textChooser + ": " + subTextChooser)
    v = st_custom_tooltip(label=label, textSize=textSize, selectedAttributes=sendAtts, sentence=sentence)
