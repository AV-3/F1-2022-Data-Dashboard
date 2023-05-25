import streamlit as st
import pandas as pd

#Sets page layout/allows the columns and graphs to use 100% width of the screen
st.set_page_config(page_title= "Grand Prix Results • F1 Dashboard", layout="wide")

#Import CSS
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#Import csv files
df1 = pd.read_csv("csv/drivers.csv")
df2 = pd.read_csv("csv/teams.csv")
df3 = pd.read_csv("csv/races.csv")
df4 = pd.read_csv("csv/GrandPrix_FastestLaps.csv")
df5 = pd.read_csv("csv/GrandPrix_Qualifying.csv")
df6 = pd.read_csv("csv/GrandPrix_RaceData.csv")


#Sidebar functionality
st.sidebar.title("F1 Dashboard")
st.sidebar.title("Filters")

# Add a dropdown to select the race
grandprix_dropdown = st.sidebar.selectbox("Grand Prix", df3["Grand Prix"].unique())

# Add a dropdown to select the team
team_dropdwon = st.sidebar.selectbox("Team", df2["Team"].unique())

# Add a dropdown to select the driver
driver_dropdown = st.sidebar.selectbox("Driver", df1["Driver"].unique())

# Add a checkbox to show only races where the driver finished in the top 5
top_5_checkbox = st.sidebar.checkbox("Show podium results only")

# Create a main page
st.title("F1 2022 Grand Prix Statistics")

# Show the driver's name and team
st.write(f"Grand Prix: {grandprix_dropdown}")
st.write(f"Team: {df1[df1['Driver'] == driver_dropdown]['Driver'].values[0]}")

# Show the driver's statistics
st.table(df1[df1['Driver'] == driver_dropdown].drop(['Nationality','Car', 'PTS'], axis=1))

# If the "Show only races where the driver finished in the top 5" checkbox is checked, only show the races where the driver finished in the top 5
if top_5_checkbox:
    df = df1[df1['Driver'] == driver_dropdown]
    df = df[df['POS'] <= 5]

# Show a table of the driver's race results
st.table(df6[['Pos', 'Driver', 'Car', 'Laps', 'Time/Retired', 'PTS']])