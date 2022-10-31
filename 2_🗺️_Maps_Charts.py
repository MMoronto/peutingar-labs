import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import leafmap.foliumap as leafmap 
from urllib.error import URLError


st.header("PEUTINGAR Labs")
st.subheader("Datasets for Africa's Transportation Infrastructure")
st.write("Peutingar's mission is to help institutions develop the capacity to build infrastructure projects easily, cheaply and efficiently. We do this by enabling effective and real-time decision making through cloud-enabled software and geo-spatial artificial intelligence.")
st.sidebar.radio('SEGMENTS', ['1', '2', '3', '4', '5', 'All'])

st.sidebar.radio('POINTS', ['1', '2', '3', '4', '5', 'All'])

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [6.46, 3.406],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Is the road paved or not?',
     df['first column'])

'You selected: ', option

add_selectbox = st.selectbox(
   'Which type of Lagos neighborhoods are at risk of flooding?',
   ("Upper class i.e. bananna Is. V.I., Ikoyi", 
      "Upper Mid class i.e. Lekki Ph. 1 & 2", 
      "Lower Mid class i.e. Mainland, Ikeja", 
      "Lower class i.e. Surulere", "Slums i.e. Makoko, Ajegunle")
   )
add_slider = st.slider(
   'Select a range of values',
   0.0, 100.0, (25.0, 75.0)
   )

left_column, middle_column, right_column = st.columns(3)
# You can use a column just like st.sidebar:
left_column.button('Trunk A Major Artery')
middle_column.button('State Motorway')
right_column.button('Local Thoroughfare')

with right_column:
   chosen = st.radio(
      'Inspection Status',
      ("Quarterly", "Annual", "Bi-annual"))
   st.write(f"Generate the {chosen} Inspection Report")

st.subheader("With a simple block of code, much can be achieved")
# st.code("const Map = () => {const origin = useSelector(selectOrigin)}; ")

st.caption("With the right timely data, Roads can be maitained with ease.'")


map_data = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [7.01, 3.310],
    columns=['lat', 'lon'])

st.map(map_data)

st.write("Peutingar's mission is to help institutions develop the capacity to build infrastructure projects easily, cheaply and efficiently. We do this by enabling effective and real-time decision making through cloud-enabled software and geo-spatial artificial intelligence.")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[6.52, 3.316], zoom=4)
        cities = './GRID3_Nigeria_-_Factories_and_Industrial_SitesA.csv'
        regions = './GRID3_Nigeria_-_Factories_and_Industrial_SitesA.geojson'

        m.add_geojson(regions, layer_name='Nig Industrial Sites')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            # color_column='state_name',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=600)
