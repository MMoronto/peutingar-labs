import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import st_folium
import folium
from branca.element import Figure


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
    m = folium.Map(location=[6.45363, 3.39803], tiles="cartodbpositron",zoom_start=13.5)
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

fig1=Figure(height=525,width=725)
m=folium.Map(location=[6.45363, 3.39803], tiles="cartodbpositron",zoom_start=13.5)
fig1.add_child(m)
with col2:
    coord_1=[[3.39469,6.547502],[3.394657,6.547417],[3.394657,6.547331],
    [3.394631,6.547238],[3.394598,6.547153],[3.394572,6.54707],[3.394569,6.546985],
    [3.394555,6.546894],[3.394542,6.546806],[3.394513,6.546716], 
    [3.394486,6.54663],[3.394462,6.546548],[3.394435,6.546457],
    [3.3944,6.54638],[3.394378,6.546292],[3.394341,6.546209],
    [3.394306,6.546122],[3.394279,6.546042],[3.394223,6.545967],
    [3.394191,6.545882],[3.394153,6.545807],[3.394099,6.545727],
    [3.394073,6.545642],[3.39403,6.545567],[3.393992,6.545482],
    [3.393971,6.545397],[3.393928,6.545317],[3.393912,6.545231],
    [3.39389,6.545141],[3.393874,6.54505],[3.393863,6.544965],
    [3.393853,6.544874],[3.393831,6.544784],[3.393826,6.544699],
    [3.393821,6.544608],[3.393799,6.544517],[3.393821,6.544427],
    [3.393815,6.544341],[3.393821,6.544251],[3.393815,6.544166],
    [3.393826,6.544075],[3.393821,6.543984],[3.393826,6.543894],
    [3.393826,6.543803],[3.393799,6.543713],[3.393799,6.543627],
    [3.393772,6.543542],[3.393751,6.543457],[3.393745,6.543361],
    [3.393721,6.543276],[3.393694,6.543188],[3.393673,6.543108],
    [3.393638,6.543022],[3.393617,6.542934],[3.393582,6.542847],
    [3.393574,6.542761],[3.393539,6.542676],[3.393485,6.542601],
    [3.39345,6.542524],[3.393416,6.542439],[3.393378,6.542359],
    [3.393335,6.542279],[3.393292,6.542199],[3.393257,6.542119],
    [3.393212,6.542039],[3.393182,6.541954],[3.393145,6.541874],
    [3.39312,6.541786],[3.393086,6.541706],[3.393061,6.541613],
    [3.393037,6.541528],[3.393008,6.541445],[3.392984,6.541354],
    [3.392951,6.541272],[3.392946,6.541184]]

    fig1=Figure()
    m=folium.Map([6.45363, 3.39803],tiles="Stamen Toner",zoom_start=13.5)
    fig1.add_to(m)

    f1=folium.FeatureGroup("Vehicle 1")

    line1=folium.vector_layers.PolyLine(coord_1,tooltip='resurfaced 2018',color='green',weight=10).add_to(f1)

    f1.add_to(m)
    folium.LayerControl().add_to(m)
    m
    # st_data = st_folium(m, width = 725)








