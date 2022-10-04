import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
import folium


st.header("Lagos")
st.subheader("View road report analyses")
st.write("Review transportation network assets.")

col1, col2 = st.columns([1, 2])

with col2:
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [6.46, 3.406],
        columns=['lat', 'lon'])

    st.map(map_data)

with col1:
    st.image('''./distressedRoad.png''')

with col1:
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])

        chart_data

    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
        })



with col2:
    m = folium.Map(location=[6.45363, 3.39803], tiles="Stamen Toner",zoom_start=12.5)
    folium.Marker(
        location=[6.45363, 3.39803],
        popup="Eyo Masquerade Statue",
        icon=folium.Icon(color="green", icon="cloud"),
        tooltip="Eyo Masquerade Statue"
        ).add_to(m)

    folium.Marker(
        [6.45464, 3.39219],
        popup="Tinubu Square",
        icon=folium.Icon(color="green", icon="cloud"),
        tooltip="Tinubu Square"
        ).add_to(m)

    st_data = st_folium(m, width = 725)






