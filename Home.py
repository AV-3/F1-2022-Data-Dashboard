import streamlit as st
import pandas as pd

#Sets page layout/allows the columns and graphs to use 100% width of the screen
st.set_page_config(page_title= "Home • F1 Dashboard", layout="centered", page_icon=":checkered_flag:")

#Import CSS
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


#Landing page
st.title("Welcome to the F1 2022 Dashboard")
st.image("images/F1 pit.jpg", caption="Scuderia Ferrari F1 Team 2020 - Image from unsplash.com")
st.title("Background:")
st.markdown(
    """
    Formula One (F1) is the highest class of single-seater auto racing sanctioned by the Fédération Internationale de l'Automobile (FIA).
    The championship consists of a series of races, known as Grands Prix, which are held on purpose-built circuits and public roads. 
    The drivers and constructors compete for the World Drivers' Championship and the World Constructors' Championship, respectively. 
    Points are awarded to the top ten finishers in each race, with the first-place finisher receiving 25 points, the second-place finisher receiving 18 points, and so on.

    The 2022 Formula One season consisted of 22 races or "Grands Prix." The first race was held in Bahrain on March 20, and the 
    last race was held in Abu Dhabi on November 20. There were 20 drivers and 10 teams competing in the 2022 season.

    Here are some additional details about F1:
    - Formula One cars are the fastest regulated road-course racing cars in the world, owing to very high cornering speeds achieved through generating large amounts of aerodynamic downforce.
    - The word "formula" in the name refers to a set of rules to which all participants' cars must conform. 
    The rules cover a wide range of aspects of the car, including the engine, chassis, and aerodynamics.
    - The Formula One World Championship is one of the most popular sporting events in the world, and it is broadcast in over 200 countries. The championship is also one of the most lucrative sports in the world, with the top teams earning hundreds of millions of dollars each year.




    """)

st.title("About the Project:")
st.markdown("""
This data visualization dashboard provides an overview of the 2022 season of Formula One 
racing with interactive visualizations that make it easy to compare drivers and teams to each other, analyze race results, and identify trends in the race data.

""")
st.write("Check out the [GitHub repository](https://github.com/AV-3/F1-2022-Data-Dashboard) for more information.")

#Sidebar
st.sidebar.title("F1 2022 Dash")
st.sidebar.markdown("Created by Alan Velez")
st.sidebar.markdown("[GitHub](https://github.com/AV-3)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/alan-velez-615401220/)")
