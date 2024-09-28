import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(team,year):
    #year = dataset['Year-Wert']
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[3]
    return df_a

cols = ['Player','Age','G','MP','PER','TS%','OBPM','DBPM','BPM','VORP']

data = read_data('HOU',2024)[cols]

data

st.header("Scatter plot | x- PER | y- TS%")
st.divider()

fig, ax = plt.subplots()
ax.scatter(data['OBPM'], data['DBPM'])

for i, label in enumerate(data['Player']):
    ax.annotate(label, (data['OBPM'][i], data['DBPM'][i]))

st.pyplot(fig)
