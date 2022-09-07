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
      st.image("https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1575660327927x644858521477206700%2Fhttp_%25252F%25252Fcdn.cnn.com%25252Fcnnnext%25252Fdam%25252Fassets%25252F180518162730-edward-burtynsky-lagos.jpg?w=2048&h=941&auto=compress&dpr=1&fit=max")
   with text_col:
      st.markdown("**Trans African Transportation Networks**")
      st.write('''
         "I have seen and heard quite a number of media sources talk about trans African 
         highways and railway lines. The voice in my head cannot help but mutter that these 
         are most likely myth than reality.  These types of projects are far from trivial. 
         They require tight coordination across multiple stake holders, and this is even 
         moreso when multinational interests are at stake.

         Integrating the African continent with a trans-continental highway or railway network would 
         require a colossal effort so immense only a top-down  command/control style of administration 
         and financing is conceivable for such massive projects to be achieved. It would require a body 
         with continent wide clout & reach like the AU on steroids to fund it(or at least to administer 
         via a common fund) and oversee every phase of the projects while superseding national 
         jurisdictional rights or interests during the design/build phase of the projects. In the 
         improbable likelihood that such a project is pulled off, it would be the largest and most 
         ambitious project ever pulled off by mankind owing to the sheer size of the African continent.

         It is unfortunate that such a project though beneficial to humankind is most unlikely to succeed 
         owing to the fractured nature of the constituent nations on the continent, their disparate interests 
         and the vastness in the degree of unalignment that would exist among the pertinent stakeholders.  
         Financing would most likely remain the largest boulder to overcome as the complexities of an 
         emergent multipolar geopolitical world start to play out over the short and long terms. It is 
         conceivable that financiers from opposing geopolitical poles find reason to acknowledge common 
         interests in funding Africa's bedrock infrastructure. A long shot? Maybe, only time will tell.''')
