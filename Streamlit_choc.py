#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import altair as alt
from datetime import datetime
from datetime import timedelta
import plotly.express as px
link="https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
hackathon = pd.read_csv(link)
hackathon2 =hackathon.copy()


# In[4]:


# variable qui contient uniquement les valeurs aggrégées de WORLD
worldstat = hackathon2.loc[hackathon2["country"]=="World"]

worldstat.rename(columns={"coal_co2": "Charbon","oil_co2": "Pétrole","gas_co2": "Gaz","cement_co2": "Ciment",
                     "flaring_co2": "Torchage","other_industry_co2": "Autres industries"}, inplace=True)
# table pivot pour avoir les valeur par année 
co2consumption = pd.pivot_table(worldstat, values='co2', index='year')
co2consumption.reset_index(inplace=True)


# In[5]:


st.set_page_config(
     page_title="Yolo",
     page_icon=":sunny:",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
        'Get Help':  None,
         'Report a bug': None,
         'About': "# Bienvenue ! # \n"
         "Xavier, Charles et Périnne vous présentent leur analyse sur les emissions de CO2 au niveau mondial \n"
         "Nous nous sommes interessés aux habitudes que les humains raffolent et regarder dans quelle mesure\n"
         "la suppression de cette habitude impactait les emissions par rapport aux objectifs fixés en 2030.\n"
         "Have Fun! \n"
         "Etudiants et étudiantes à la Wild Code School de Nantes \n"
     }
 )

#titre de notre page
st.title("Joyeuse analyse des émissions de CO2 dans le monde")
st.write("                                                   ")
st.subheader(" Bilan à 2020 des émissions de CO2 généré par le secteur de l'énergie")


# In[14]:


co2consumption["year"]=co2consumption["year"].apply(lambda x : str(x))


# In[13]:


line_chart = alt.Chart(co2consumption).mark_line().encode(
    x=alt.X("year:T",title='Années'), 
    y=alt.Y('co2', title='Emission de CO2 en millions de tonnes'),
    color=alt.value("#FF27D0"),
)
objective=alt.Chart(co2consumption).mark_rule().encode(y=alt.datum(15000))

st.altair_chart(objective + line_chart, use_container_width=True)

with st.container():
    col1, col2= st.columns(2)

    col1.write("L'objectif de baisse de CO2 en 2030 est d'environ **15000 millions\n"
              "de tonnes par an**, comme vous pouvez le constater nous sommes\n"
              "légèrement au-dessus rien de bien inquiètant  :sunglasses: , **franchement ça passe !** \n"
              "\n"
               "Le fait majeur de ce graphique est **l'augmentation de l'émission de CO2** au fil des années\n"
                ",on imagine d'ici votre surprise avec cette information.\n"
                "Regardons maintenant le poids des différents types d'énergie sur les émissions\n"
               "de CO2 dans le monde, une grande surprise est également prévue.\n"
              )
    col2.image(
            "https://media.giphy.com/media/l3vR5UgInxQW8wK6k/giphy.gif",
            use_column_width="auto")


# In[151]:


st.write("                                                   ")
st.subheader("Proportion des différentes industries dans l'émission de CO2 en fonction du temps")
st.write("                                                   ")
fig =px.area(data_frame =worldstat, x='year',y=['Charbon','Pétrole','Gaz','Ciment','Torchage','Autres industries'],
             color_discrete_sequence= px.colors.diverging.PiYG, 
#              labels={"coal_co2": "Charbon","oil_co2": "Pétrole","gas_co2": "Gaz","cement_co2": "Ciment",
#                      "flaring_co2": "Torchage","other_industry_co2": "Autres industries"}
            )

fig.update_layout(
    font_family="IBM Plex Sans",
    xaxis_title="Années",
    yaxis_title="Émission de CO2 en mt/an",
    legend_title="Industries",
)

st.plotly_chart(fig, use_container_width=True)
with st.container():
    col1, col2= st.columns(2)

    col2.write("Premier constat, **il reste des corons** ! Et oui, le charbon \n"
              "est la première source d'émission de CO2. Elle reste très utilisée\n"
              "par de nombreux pays pour se chauffe, **franchement, pas ouf!** \n"
              "\n"
               "Vous constaterez que l'augmentation fut exponentielle, depuis l'arrivée des **boomers** :clap: ! \n"
               "Oui, mesdames et messieurs, les boomers ont pris le pouvoir et l'energie avec ! \n"
               "Depuis les générations ont rien changé, elles les ont exploité \n"
              )
    col1.image(
            "https://media.giphy.com/media/l3vRgggdBsrXJNocg/giphy.gif",
            use_column_width="auto")


# In[15]:


st.write("                                                   ")
st.subheader("Des petits essais pour atteindre l'objectif...")
col1, col2, col3, col4 = st.columns((3,1,1,1))
with col2:
    with st.expander("Suprise"):
        avions=st.slider("Supprimons des avions, bye bye les caraïbes", -100, 100, 0, key="avions")
    with st.expander("Encore plus"):
        streaming=st.slider("Adieu Netflix & Chill, just Chill !", -100, 100, 0, key="streaming")
with col3: 
    with st.expander("Tristitude"):
        alcool = st.slider("Fini les hangover !", -100, 100, 0, key="alcool")
    with st.expander("Adieu vie sociale"):
        smartphone = st.slider("Smart quoi ?", -100, 100, 0, key="smartphone")
with col4:     
    with st.expander("Moyens drastiques"):
        etatsunis = st.slider("On rase les Etats-Unis à combien de % ?", -100, 100, 0, key="usa")
    with st.expander("Moyens désespérés"):
        chine = st.slider("Même combat pour la Chine", -100, 100, 0, key="chine")
    
resultat = (avions*0.0136) + (streaming*0.01) + (alcool*0.007) + (smartphone*0.004) + (etatsunis*0.138) + (chine*0.3138) #stock la valeur additionné de nos reglettes
worldstat2000=worldstat.copy()
worldstat2000['Courbe']= 'Réel'
worldstat2000Dystopie=worldstat2000.copy()
worldstat2000Dystopie['Courbe']= 'Dystopie'
worldstat2000Dystopie["co2"]=worldstat2000Dystopie["co2"].apply(lambda x : x*((100+resultat)/100))
worldstat2000complete = pd.concat([worldstat2000,worldstat2000Dystopie])
worldstat2000complete["year"]=worldstat2000complete["year"].apply(lambda x : str(x))


with col1:
    line_chart_test = alt.Chart(worldstat2000complete).mark_line().encode(
    x=alt.X("year:T",title='Années'), 
    y=alt.Y('co2', title='Emission de CO2 en millions de tonnes'),
    color= alt.Color('Courbe',scale=alt.Scale(range=["plum", "darkorchid"]))
    ).properties(
    height=400)

    objective=alt.Chart(worldstat2000complete).mark_rule().encode(y=alt.datum(15000))
    st.altair_chart(line_chart_test + objective, use_container_width=True)


# In[ ]:




