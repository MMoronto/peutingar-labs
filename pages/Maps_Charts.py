# st.header("PEUTINGAR Labs")
st.subheader("Datasets for Africa's Transportation Infrastructure")
st.write("Peutingar's mission is to help institutions develop the capacity to build infrastructure projects easily, cheaply and efficiently. We do this by enabling effective and real-time decision making through cloud-enabled software and geo-spatial artificial intelligence.")


with st.container():
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''https://mcusercontent.com/9af560008b578528e07445390/images/706e1762-4543-a736-76ec-12e92faa3a5f.jpg''')
   with text_col:
      st.markdown("**Paradigm shift in infrastructure maintenance management**")
      st.write('''
         The burden of maintenance can be alleviated in countries that often 
         lack financial resources to conduct routine work on existing infrastructure 
         by enabling the monitoring of certain infrastructure at scale with minimum 
         deployment of ground teams. This way troubled spots are targeted and 
         prioritized thus saving man hours and budget.''')
with st.container():
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image("https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1575660327927x644858521477206700%2Fhttp_%25252F%25252Fcdn.cnn.com%25252Fcnnnext%25252Fdam%25252Fassets%25252F180518162730-edward-burtynsky-lagos.jpg?w=2048&h=941&auto=compress&dpr=1&fit=max")
   with text_col:
      st.markdown("**Eagle-eye view approach to maintenance**")
      st.write('''
         "If you want to build a wealthy economy, you must first start by building roads". 
         I don't recall exactly when I first heard this quote. It is an old Chinese saying, but then again, I can't be so sure. 
         This quote resonates when you consider fast-growing nations in the last century. 
         Much of their accomplishments were possible due to effective transportation infrastructure. 
         Road and rail networks are essential for opening up a country's interior. 
         This is even more so if such regions were hitherto, inaccessible. 
         Roads foster cohesion across regions thereby facilitating trade and commerce amongst neighbors. 
         Roads are accelerants for developing manufacturing and industrial capacity in a region.''')

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
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# add_selectbox = st.sidebar.selectbox(
#    'Which type of Lagos neighborhoods should we investigate?',
#    ("Upper class i.e. bananna Is. V.I., Ikoyi", 
#       "Upper Mid class i.e. Lekki Ph. 1 & 2", 
#       "Lower Mid class i.e. Mainland, Ikeja", 
#       "Lower class i.e. Surulere", "Slums i.e. Makoko, Ajegunle")
#    )
# add_slider = st.sidebar.slider(
#    'Select a range of values',
#    0.0, 100.0, (25.0, 75.0)
#    )

left_column, middle_column, right_column = st.columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')
middle_column.button('Unpress me!!')
right_column.button('Nuclear option!!!')

with right_column:
   chosen = st.radio(
      'Executive action',
      ("Nuclear protocol", "High Alert", "Nuclear code"))
   st.write(f"Trump will activate the {chosen} sequence!")

st.subheader("With a simple block of code, much can be achieved")
st.code("const Map = () => {const origin = useSelector(selectOrigin)}; ")

st.caption("On the third day, the Lord said'Let there be code.'")

st.code('''
   const Map = () => {
    const origin = useSelector(selectOrigin);

    return (
    <MapView
        style={tw`flex-1`}
        mapType="mutedStandard"
        initialRegion={{
            latitude: origin.location.lat,
            longitude: origin.location.lng,
            latitudeDelta: 0.005,
            longitudeDelta: 0.005,
        }}
    >
        {origin?.location && (
            <Marker 
                coordinate={{
                    latitude: origin.location.lat,
                    longitude: origin.location.lng,
                }}
                title="Origin"
                description={origin.description}
                identifier="origin"
            />
        )}    
    </MapView>
  );
};''')

