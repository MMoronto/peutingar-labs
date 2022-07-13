import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(
#     page_title="Aborigani!",
#     page_icon="👋",
# )

st.title("PEUTINGAR Labs")
st.sidebar.success("Navigate to page links above.")




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
