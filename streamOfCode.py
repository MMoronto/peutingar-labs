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
# st.write("Peutingar's mission is to help institutions develop the capacity to build infrastructure projects easily, cheaply and efficiently. We do this by enabling effective and real-time decision making through cloud-enabled software and geo-spatial artificial intelligence.")
st.write("Peutingar's mission is to help the world's fastest growing cities pave every dirt road and maintain all paved roads in the cheapest and most efficient way possible by providing access to relevant, frequently updated and affordable data at scale.")


with st.container():
   st.image('''./image3-.png''')
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''https://mcusercontent.com/9af560008b578528e07445390/images/706e1762-4543-a736-76ec-12e92faa3a5f.jpg''')
   with text_col:
      st.markdown("**Paradigm shift in infrastructure maintenance management**")
      st.write('''
         The burden of maintenance can be alleviated in countries that lack
         financial resources to conduct routine work on existing infrastructure 
         by enabling the monitoring of critical infrastructure at scale with minimum 
         deployment of ground teams. This way troubled spots are targeted and 
         prioritized thus saving man hours and stretching limited budgets.''')

with st.container():
   st.subheader("**Eagle-eye view approach to maintenance**")
   st.image("https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1575660327927x644858521477206700%2Fhttp_%25252F%25252Fcdn.cnn.com%25252Fcnnnext%25252Fdam%25252Fassets%25252F180518162730-edward-burtynsky-lagos.jpg?w=2048&h=941&auto=compress&dpr=1&fit=max")
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''./image1-.png''')
      st.image('''./image4-.png''')
   with text_col:
      # st.markdown("**Eagle-eye view approach to maintenance**")
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
   st.subheader("**Trans African Transportation Networks**")
   st.write()
   st.image('''./image2-.png''')
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image("https://www.researchgate.net/profile/Sergio-Oliete-Josa/publication/322258475/figure/fig1/AS:593694713458689@1518559258802/PIDAs-transport-network-plan-PIDA-2012-TAH-Trans-African-Highway.png")
      map_data = pd.DataFrame(
          np.random.randn(100, 2) / [50, 50] + [6.46, 3.406],
          columns=['lat', 'lon'])

      st.map(map_data)

      x = st.slider('x')  # 👈 this is a widget

      if st.checkbox('Show dataframe'):
          chart_data = pd.DataFrame(
             np.random.randn(20, 3),
             columns=['a', 'b', 'c'])

          chart_data

      df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
          })
   with text_col:
      # st.markdown("**Trans African Transportation Networks**")
      st.write('''
         Lately, there have been discussions in various media outlets about trans-African highways and railways as a means of 
         integrating the continent. The voice in my head cannot help but mutter that these talks are more likely myths than reality. 
          These types of projects are far from trivial. It would take tight coordination across many stakeholders to achieve success. 
          This is even more so when multinational interests are at stake.

         It would take a colossal effort to integrate the African continent through transport networks. Top-down, 
         command-control administration will be necessary to complete complex projects at such scale. A body with 
         continent-wide clout & reach like the AU(African Union), on steroids, must fund and oversee every phase of the 
         project. National jurisdictional rights during the project's design/build phase will  belong to the body. 
         If such an ambitious project succeeds, it would be the most daring one ever pulled off by mankind owing to the 
         sheer size of the African continent alone.

         Unfortunately, such a project regardless of its benefits to humankind is most improbable. The fractured nature 
         of the continent's constituent nations is a big disadvantage. Disparate and unaligned interests amongst pertinent 
         stakeholders complicate this scenario further.
         Of all the headwinds this proposition faces, Financial risk is the most prominent. Whereas Project Financing has been 
         manageable in the last decade, change is in the air. I suspect that financing will pose unique challenges in the immediate 
         future. This becomes more evident as the complexities of an emergent multipolar geopolitical world order start to play out 
         in the short term and over the long term. It is conceivable that financiers from opposing geopolitical poles find a reason 
         to acknowledge common interests in funding Africa's bedrock infrastructure. A long shot? Time will tell.
         ''')
with st.container():
   st.subheader("**Prioritizing the Discipline of Maintenance**")
   st.image("https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1575660327927x644858521477206700%2Fhttp_%25252F%25252Fcdn.cnn.com%25252Fcnnnext%25252Fdam%25252Fassets%25252F180518162730-edward-burtynsky-lagos.jpg?w=2048&h=941&auto=compress&dpr=1&fit=max")
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''./image1-.png''')
      st.image('''./image4-.png''')
   with text_col:
      # st.markdown("**Eagle-eye view approach to maintenance**")
      st.write('''
         As infrastructure projects keep cropping up across the African sub-continent one has to wonder what frameworks are being put 
         in place to cultivate the discipline of maintenance and nurture the idea of maintenance into a fully ingrained maintenance 
         culture. On a more tactical level, the relevant questions about the performance of maintenance must be addressed. These 
         questions must be answered coherently. Who will do the maintenance? When will it be done? How frequently? What tools and 
         resources will be necessary to get it done? What happens if these resources are not unavailable? How much will it cost? 
         Where does the money come from? What contingencies are there for funding  when economic downturns occur?

         In what way can earth observation and geospatial datascience help create a culture of maintenance? I imagine a world where 
         periodic and consistent monitoring of transport infrastructure is possible because of the availability of affordable satellite 
         imagery. A world where processing of relevant data  is automated, actionable insights are extracted with ease, and seamlessly 
         delivered at scale. This naturally eliminates several costly steps in the customary long and drawn out inspection process. 
         These periodic inspection processes are indispensable when identifying the health of road networks. 

         How would one go about sowing the seeds of a movement that pushes the adoption of infrastructure maintenance so much so 
         that it becomes a culture. What initiatives must be enacted to emphasize the importance of maintaining built infrastructure? 
         How does one convince stakeholders to prioritize maintenance as an essential practice amongst other essentials that vie 
         constantly for the top slot on a region's hierarchy of needs? it appears to be a hard sell at first blush. But what if, 
         just what if the same mechanisms that have allowed for the behavior changes required to embrace new technologies can be 
         harnessed for more practical societal benefits?
         ''')

