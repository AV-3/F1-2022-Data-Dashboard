import streamlit as st
import pandas as pd
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


#Landing page
st.title("Welcome to the F1 2022 Dashboard")
st.image("images/F1 pit.jpg", caption="Scuderia Ferrari F1 Team 2020 - Image from unsplash.com")
st.title("Background:")
st.markdown(
    """Formula One (F1) is the highest class of single-seater 
auto racing sanctioned by the Fédération Internationale de l'Automobile (FIA). 
Formula One cars are the fastest regulated road-course racing cars in the world, owing to very high 
cornering speeds achieved through generating large amounts of aerodynamic downforce.


The word "formula" in the name refers to a set of rules to which all participants' cars must conform. The rules cover a wide range of aspects of the car, including the engine, chassis, and aerodynamics. 

The 2022 Formula One season consisted of 22 races or "Grands Prix."
The first race was held in Bahrain on March 20, and the last race was held in Abu Dhabi on November 20.
There were 20 drivers and 10 teams competing in the 2022 season.
""")

st.title("About the Project:")
st.markdown("""
This statistics dashboard provides an overview of the 2022 season of Formula One 
racing with interactive visualizations that make it easy to compare drivers and teams to each other, analyze race results, and identify trends in the race data.

""")
st.write("Check out the [GitHub repository](https://github.com/AV-3/F1-2022-Data-Dashboard) for more information.")
