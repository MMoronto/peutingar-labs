import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
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
right_column.button('Local Thoroghfare')

with right_column:
   chosen = st.radio(
      'Inspection Status',
      ("Quarterly", "Annual", "Bi-annual"))
   st.write(f"Generate the {chosen} Inspection Report")

st.subheader("With a simple block of code, much can be achieved")
# st.code("const Map = () => {const origin = useSelector(selectOrigin)}; ")

st.caption("With the right timely data, Roads can be maitained with ease.'")


st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)

@st.experimental_memo
def from_data_file(filename):
    url = (
        "http://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


try:
    ALL_LAYERS = {
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[0, 0, 0, 200],
            get_size=15,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )

