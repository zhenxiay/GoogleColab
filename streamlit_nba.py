import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Definition of the function to get data
def get_team_list():

    df = pd.read_html('https://www.basketball-reference.com')
    df_west = df[1]
    df_west = df_west.rename(columns={"West": "teams"})
    df_west['teams'] = df_west['teams'].str[:3]
    teams = df_west['teams']
    #df_east = df[0]
    #df_east = df_east.rename(columns={"East": "teams"})
    #df_teams = pd.concat([df_west, df_east],ignore_index=True)
    #df_teams['teams'] = df_teams['teams'].str[:3]
    #teams = df_teams['teams']

    return teams.to_list()

@st.cache_data
def read_data(team,year):
    #year = dataset['Year-Wert']
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[3]
    return df_a

#Selection area
team_selected = st.selectbox('Team', get_team_list())

#First part of the web app
st.markdown('## Advanced stats players')

cols = ['Player','Age','G','MP','PER','TS%','OBPM','DBPM','BPM','VORP']

data = read_data(team_selected,2024)[cols]

data = data[data['MP']> 400]

data

st.divider()

st.header("Scatter plot | x- OBPM | y- DBPM")

#Second part of the web app
fig, ax = plt.subplots()
sizes = data['MP']*0.1
max_size = 200

ax.scatter(x=data['OBPM'], 
           y=data['DBPM'],
           s=[size if size <= max_size else max_size for size in sizes],
           alpha=0.5)

for i, label in enumerate(data['Player']):
    ax.annotate(label, (data['OBPM'][i] + 0.1, data['DBPM'][i] + 0.1))

st.pyplot(fig)
