import streamlit as st
import pandas as pd
import numpy as np


st.header("Lagos")
st.subheader("View road report analyses")
st.write("The state of transportation network assets.")

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






