
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.express as px

#Definition of the function to get data
def read_data(name,start_date):
   df_asset = yf.download(name, start=start_date)
   return df_asset

stock_name = 'MSFT'

start_date = '2024-01-01'

data = read_data(stock_name,start_date)

#header
st.header(f"Timeline | Stock- {stock_name} | Start- {start_date}")

#First part of the web app
data

st.divider()

#Second part of the web app
fig = px.line(data, 
              x=data.index, 
              y='Adj Close', 
              title=f'{stock_name} Stock Price')

fig.update_yaxes(range=[min(data['Adj Close'])*0.8, 
                        max(data['Adj Close'])*1.2])

st.plotly_chart(fig)