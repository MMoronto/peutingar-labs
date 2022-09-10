import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

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


@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Annual Expenditure on Transport Infrastructure ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
