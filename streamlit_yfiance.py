
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

#First part of the web app
data

st.divider()

st.header(f"Timeline | x- {stock_name} | y- {start_date}")

#Second part of the web app
fig = px.line(data, 
              x=data.index, 
              y='Adj Close', 
              title=f'{stock_name} Stock Price')

st.plotly_chart(fig)