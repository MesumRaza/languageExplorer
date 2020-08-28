# Import the wrapper function from your package
import streamlit as st
import textManager
import textViewer


def main():
    page = st.sidebar.radio("Page", options=["Text Manager", "Text Viewer"], index=1)
    if page == "Text Manager":
        textManager.textManager()
    elif page == "Text Viewer":
        textViewer.textViewer()


main()
