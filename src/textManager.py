# Import the wrapper function from your package
import streamlit as st
import os
from pathlib import Path
import re

def textManager():
    st.sidebar.markdown("***")
    st.header("Text Manager")

    tool_type = st.sidebar.radio("What would you like to do?", options = ["Add a document"])
    if tool_type == "Add a document":
        document_creator()
    else:
        loadedDocuments = "data/imported/"
        fileList = os.listdir(loadedDocuments)
        if ".DS_Store" in fileList:
            fileList.remove(".DS_Store")
        if "config.txt" in fileList:
            fileList.remove("config.txt")
        scorpus = st.selectbox("Delete a user document", fileList)
        confirm = st.button(f'Delete {scorpus}', )
        if confirm:
            with st.spinner("Wait for it..."):
                try:
                    fpath = loadedDocuments + scorpus
                    os.remove(fpath)
                except:
                    print("could not delete user document")


def document_creator():
    corpusfailed = False
    documentName = st.text_area("Define Text Name", "")
    addAttributes = st.text_area("Define Text Attributes", "")
    documentText = st.text_area("Paste tab-separated vertical text here", "")
    attributesToAdd = addAttributes
    ccorpus = st.button("Create Text", )
    if ccorpus:
        with st.spinner('Wait for it...'):
            try:
                addAttributesToConfig(documentName, attributesToAdd)
                createDocument(documentName, documentText)
            except:
                corpusfailed = True
    if corpusfailed == True:
        st.write("TEXT NOT CREATED")

def addAttributesToConfig(documentName, attributesToAdd):
    config = "data/imported/config.txt"
    docuName = documentName
    try:
        with open(config, 'a') as outfile:
            outfile.write("\n" + docuName + "\t" + attributesToAdd)
    except:
        pass

def createDocument(documentName, documentText):
    docuName = documentName
    newfile = docuName
    filepath = "data/imported/"
    f = open(filepath + newfile, "w+")
    data = documentText
    data = re.sub("\n\t*\n", "\n", data)
    f.write(data)
