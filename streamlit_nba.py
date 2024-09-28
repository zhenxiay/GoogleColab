import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Definition of the function to get data
def read_data(team,year):
    #year = dataset['Year-Wert']
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[3]
    return df_a

cols = ['Player','Age','G','MP','PER','TS%','OBPM','DBPM','BPM','VORP']

data = read_data('HOU',2024)[cols]

#First part of the web app
data

st.divider()

st.header("Scatter plot | x- OBPM | y- DBPM")

#Second part of the web app
fig, ax = plt.subplots()
sizes = data['MP']*0.001
max_size = max(sizes)

ax.scatter(x=data['OBPM'], 
           y=data['DBPM'],
           s=[size if size <= max_size else max_size for size in sizes],
           alpha=0.5)

for i, label in enumerate(data['Player']):
    ax.annotate(label, (data['OBPM'][i] + 0.1, data['DBPM'][i] + 0.1))

st.pyplot(fig)
