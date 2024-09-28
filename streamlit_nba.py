import streamlit as st
import pandas as pd
import numpy as np

def read_data(team,year):
    #year = dataset['Year-Wert']
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[3]
    return df_a

cols = ['Player','Age','G','MP','PER','TS%','OBPM','DBPM','BPM','VORP']

df_main = read_data('HOU',2024)[cols]

df_main

st.header("Scatter plot | x- PER | y- TS%")
st.divider()
st.scatter_chart(
    df_main,
    x="PER",
    y="TS%",
    size="BPM",
)
