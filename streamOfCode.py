import streamlit as st
import pandas as pd
import numpy as np

# st.set_page_config(
#     page_title="Aborigani!",
#     page_icon="👋",
# )

st.title("PEUTINGAR Labs")
# st.sidebar.success("Navigate to page links above.")




# st.header("PEUTINGAR Labs")
st.subheader("Datasets for Africa's Transportation Infrastructure")
st.write('Morakinyo Moronto')
st.write("Peutingar's mission is to help the Africa's fastest growing cities pave every dirt road and maintain all paved roads in the cheapest and most efficient way possible by providing access to relevant, frequently updated and affordable data at scale.")


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
st.write('*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *')

with st.container():
   st.subheader("**Eagle-eye view approach to maintenance**")
   st.write('Morakinyo Moronto')
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
         Much of their accomplishments were possible due to the implementation of effective transportation infrastructure. 
         Road and rail networks are essential for opening up a country's interior. 
         This is even more so if such regions were hitherto, inaccessible. 
         Roads foster cohesion across regions thereby facilitating trade and commerce amongst neighbors. 
         Roads are accelerants for developing manufacturing and industrial capacity in a region.''')
st.write('*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *')

with st.container():
   st.subheader("**Trans African Transportation Networks**")
   st.write('Morakinyo Moronto')

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
st.write('*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *')
with st.container():
   st.subheader("**Prioritizing the Discipline of Maintenance**")
   st.write('Morakinyo Moronto')
   st.image("./image_6.png")
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''./image_7.png''')
      st.image('''./image8.png''')
   with text_col:
      # st.markdown("**Eagle-eye view approach to maintenance**")
      st.write('''
         As infrastructure projects keep cropping up across the African sub-continent one has to wonder what frameworks are being put 
         in place to cultivate the discipline of maintenance and nurture the idea of maintenance into a fully ingrained maintenance 
         culture. On a more tactical level, the relevant questions about the performance of maintenance must be addressed. These 
         questions must be answered coherently. Who will do the maintenance? When will it be done? How frequently? What tools and 
         resources will be necessary to get it done? What happens if these resources are not available? How much will it cost? 
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
st.write('*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *')
with st.container():
   st.subheader("**The Burden of Maintaining Sub-Saharan Africa's Roads**")
   st.write('Morakinyo Moronto')
   st.image("./image8.png")
   image_col, text_col = st.columns((1,2))
   with image_col:
      st.image('''./image_7.png''')
      st.image('''./image_6.png''')
   with text_col:
      # st.markdown("**Eagle-eye view approach to maintenance**")
      st.write('''
It is hardly  news that the entire region of sub-Saharan Africa has less municipal and civil infrastructure than some individual states in the continental USA. In my previous posts, i attempted to frame the most obvious issues which stymie the development of robust municipal infrastructure on the sub continent. I showcased obvious and some not so obvious situations that continue to hobble the maintenance of its existing infrastructure and impede the expansion of its vital transportation networks. one of the more obvious conclusions was that roads are expensive to build and even more expensive and operationally demanding to maintain.  With this in mind, we'll explore the nature of these challenges and propose viable and practical options for resolving each challenge.

**costs and budget constraints**
A healthy road network requires routine maintenance for its full benefits to be realized. The typical asphalt road is designed to last a decade. This life span is easily extended for another five to six years if routine maintenance is carried out diligently and at the appropriate points in its life cycle.   A failure to conduct well timed routine maintenance reduces the roads lifespan to under the ten year mark and costs much more as rehabilitation or complete reconstruction of the road will eventually be required. Unfortunately many developing countries are forced to defer routine road maintenance, or completely neglect roads due to constrained finances. As budgetary constraints are often the norm in these nations, road maintenance is routinely de-prioritized in light of other pressing issues.  

**Ineffective policy dilemmas**
A lack of institutional capacity and adequate expertise in municipal and civil infrastructure planning and policy making often lead to poorly thought-out policies and ad-hoc decisions that lack a centralized vision and strategy. This naturally leads to a mismatch between stakeholder needs and what gets built or maintained. A typical example is the scenario where countries overspend on over-engineered roads and spend additional funds on rehabbing or completely rebuilding under-engineered road sections. The incoherence in strategies due to ill informed policies or a lack of data ultimately lead to waste. 

**Opaque contractual arrangements with contractors and vendors**
it is not uncommon in some parts of a developing nation to have multiple contracts  awarded for the same project and to subsequently have nothing built. ditches are dug, dirt gets pushed around but the road never gets built. In many instances, the road is simply rendered worse off than before the contract was awarded.  The lack of transparency in the processes of contracting municipal work to contractors encourage an atmosphere bereft of accountability. In such an environment, it is easy for contractors to under-perform or to fail at delivering projects as agreed upon. 

**Material costs**
A lack of data and incoherent policies for developing municipal infrastructure most assuredly lead to waste. This is untenable in cash strapped societies for obvious reasons. Yet it is common to see inefficiencies in construction methods and means regularly adopted. Every means of reducing construction costs must be considered when executing road projects in these places. One of the more obvious areas where savings can be made is in material costs. Construction materials should be sourced locally so as to reduce transportation costs. Designs that consider location from a perspective of cost savings can better balance long term durability against short term cost savings. Critical questions that challenge engineering norms have to be asked. For instance, do roads in an area full of granite deposits and a large mass of under-employed, able-bodied youths need to be built with imported asphalt and bitumen? Can the minor roads in such an area  be manually paved in local stone?  These type of considerations ought to be carefully considered.

**Transportation costs**
This piggy-backs off the previous point. Source building materials locally to reduce the cost of transporting standard road building materials. Use local transportation contractors to minimize cost. Building local capacity where none exists will create opportunities for jobs as small plants and quarries will operate in perpetuity as long as the roads exist and require maintenance. 

         ''')
st.write('*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *')