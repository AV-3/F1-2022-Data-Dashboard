import streamlit as st
import pandas as pd
import altair as alt
import plost

#Sets page layout/allows the columns and graphs to use 100% width of the screen
st.set_page_config(page_title= "Overall Results • F1 Dashboard", layout="wide", page_icon=":checkered_flag:")

#Sets color variables
primary_color = "#f2023e"

#Sidebar
st.sidebar.title("F1 2022 Dash")
st.sidebar.markdown("Created by Alan Velez")
st.sidebar.markdown("[GitHub](https://github.com/AV-3)")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/alan-velez-615401220/)")

#Import CSS
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#Import csv files
df1 = pd.read_csv("clean_csv/clean_drivers.csv")
df2 = pd.read_csv("clean_csv/clean_teams.csv")

#Page title
st.title("F1 2022 Season Overview")

#Makes tabs for each page
tab1, tab2 = st.tabs(["Drivers", "Constructors"])

#Driver Stats Tab
with tab1:
    #Row A/Podium metrics
    st.subheader("Podium(Top 3 Drivers)")
    col1, col2, col3 = st.columns(3)
    col1.metric("MAX VERSTAPPEN (Red Bull #1)", "1st", "454 pts")
    col2.metric("CHARLES LECLERC (Ferrari #16)", "2nd", "308 pts")
    col3.metric("SERGIO PEREZ (Red Bull #11)", "3rd","305 pts")
    
    #Row B/Standings bar chart
    st.subheader("Drivers Standings")
    plost.bar_chart(
    data=df1,
    bar='Driver',
    value='Points',
    color=primary_color,
    direction='horizontal',
    )

    #Row C/Wins and podium donut charts
    col4, col5, = st.columns(2)
    with col4:
        st.subheader("Wins")
        plost.donut_chart(
        data=df1,
        theta='Wins',
        color='Driver',
        legend='left',
        use_container_width= True
        )
    
    with col5:
        st.subheader("Podiums")
        plost.donut_chart(
        data=df1,
        theta='Podiums',
        color='Driver',
        legend='left',
        use_container_width= True
        )
    
    #Row D/Raw Data
    with st.expander("Click to see raw data"):
        st.subheader("Raw Dataframe")
        df1_new = pd.read_csv("raw_csv/drivers.csv")
        df1_new.columns=["Rank","Driver","Nationality","Team","Points","Wins","Podiums"]
        df1_new.index.names = ['ID']
        st.dataframe(df1_new, width=33, height=800, use_container_width= True)
    
#Constructor Stats Tab
with tab2:
    #Row A
    st.subheader("Podium(Top 3 Constructors)")
    col1, col2, col3 = st.columns(3)
    col1.metric("RED BULL", "1st", "759 pts")
    col2.metric("FERRARI", "2nd", "554 pts")
    col3.metric("MERCEDES", "3rd","515 pts")

    #Row B/Standings bar chart
    st.subheader("Constructors Standings")
    plost.bar_chart(
    data=df2,
    bar='Team',
    value='Points',
    color=primary_color,
    direction='horizontal',
    )

    #Row C/Wins and podium donut charts
    col4, col5, = st.columns(2)
    with col4:
        st.subheader("Wins")
        plost.donut_chart(
        data=df2,
        theta='Wins',
        color='Team',
        legend='left',
        use_container_width= True
        )
    
    with col5:
        st.subheader("Podiums")
        plost.donut_chart(
        data=df2,
        theta='Podiums',
        color='Team',
        legend='left',
        use_container_width= True
        )
    
    #Row D/Raw Data
    with st.expander("Click to see raw data"):
        st.subheader("Raw Dataframe")
        df2_new = pd.read_csv("raw_csv/teams.csv")
        df2_new.columns=["Rank","Team","Points"]
        df2_new.index.names = ['ID']
        st.dataframe(df2_new, width=33, height=380, use_container_width= True)