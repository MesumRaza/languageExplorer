# Import the wrapper function from your package
import streamlit as st
import textManager
import textViewer
from PIL import Image


def main():
    image = Image.open('languageExplorer.png')
    st.sidebar.image(image, width=305)
    page = st.sidebar.radio("Tool", options=["Text Manager", "Text Viewer"], index=1)
    if page == "Text Manager":
        textManager.textManager()
    elif page == "Text Viewer":
        textViewer.textViewer()

main()
