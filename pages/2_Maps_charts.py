
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [6.46, 3.406],
    columns=['lat', 'lon'])

st.map(map_data)

