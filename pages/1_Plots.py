chosen = st.radio(
      'Executive action',
      ("Nuclear protocol", "High Alert", "Nuclear code"))
   st.write(f"Trump will activate the {chosen} sequence!")

st.subheader("With a simple block of code, much can be achieved")
st.code("const Map = () => {const origin = useSelector(selectOrigin)}; ")
