import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plots", page_icon="📈")

st.markdown("# Trade Estimates for the Road Networks Converging into Cities ")
st.sidebar.header("Plots")
st.write(""""If you want to build a wealthy economy, you must first start by building roads". """)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

chosen = st.radio(
      'Network overview',
      ("Primary networks", "Secondary networks", "Intermediate routes")
      )
st.write(f"Trade estimates for {chosen} converging into cities")
st.image('''./image5.png''')

st.subheader("With a simple block of code, much can be achieved")
st.code("const Map = () => {const origin = useSelector(selectOrigin)}; ")
