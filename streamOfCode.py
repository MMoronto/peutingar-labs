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

with st.container():
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image("https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1575660327927x644858521477206700%2Fhttp_%25252F%25252Fcdn.cnn.com%25252Fcnnnext%25252Fdam%25252Fassets%25252F180518162730-edward-burtynsky-lagos.jpg?w=2048&h=941&auto=compress&dpr=1&fit=max")
   with text_col:
      st.markdown("**Eagle-eye view approach to maintenance**")
      st.write('''
         "If you want to build a wealthy economy, you must first start by building roads". 
         I don't recall exactly when I first heard this quote. It is an old Chinese saying, but then again, I can't be so sure. 
         This quote resonates when you consider the nations that have grown the fastest in the last century. 
         Much of their accomplishments were possible due to effective transportation infrastructure. 
         Road and rail networks are essential for opening up a country's interior. 
         This is even more so if such regions were hitherto, inaccessible. 
         Roads foster cohesion across regions thereby facilitating trade and commerce amongst neighbors. 
         Roads are accelerants for developing manufacturing and industrial capacity in a region.''')

with st.container():
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image("https://www.researchgate.net/profile/Sergio-Oliete-Josa/publication/322258475/figure/fig1/AS:593694713458689@1518559258802/PIDAs-transport-network-plan-PIDA-2012-TAH-Trans-African-Highway.png")
   with text_col:
      st.markdown("**Trans African Transportation Networks**")
      st.write('''
         Lately, some media sources have been talking about trans-African highways and railway lines. The voice in my 
         head cannot help but mutter that these talks are most likely myths than reality. These types of projects are 
         far from trivial. They need tight coordination across many stakeholders. This is more so when multinational 
         interests are at stake.

         It would take a colossal effort to integrate the African continent through transport networks. Top-down, 
         command-control administration will be necessary to complete complex projects at such scale. A body with 
         continent-wide clout & reach like the AU(African Union), on steroids, to fund and oversee every phase of 
         the projects. National jurisdictional rights during the project's design/build phase will  belong to the body. 
         If such an ambitious project succeeds, it would be the most daring one ever pulled off by mankind owing to the 
         sheer size of the African continent alone.

         Unfortunately, such a project regardless of its benefits to humankind is improbable. The fractured nature of 
         the continent's constituent nations is a big disadvantage. Disparate and unaligned interests amongst pertinent 
         stakeholders complicate this scenario further.
         Of all the headwinds this proposition faces, Financial risk is the most prominent. Whereas Project Financing 
         has been manageable in the last decade, change is in the air. I suspect financing poses unique challenges as 
         the complexities of an emergent multipolar geopolitical world start to play out over the short and long terms. 
         It is conceivable that financiers from opposing geopolitical poles find a reason to acknowledge common interests 
         in funding Africa's bedrock infrastructure. A long shot? Only time will tell.
         ''')
