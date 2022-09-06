import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

def app():
    st.title("Search Basemaps")
    st.markdown(
        """
    This app is a demonstration of searching and loading basemaps from [xyzservices](https://github.com/geopandas/xyzservices) and [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices). Selecting from 1000+ basemaps with a few clicks.  
    """
    )

