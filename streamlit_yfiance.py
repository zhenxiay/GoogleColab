
import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.express as px

#Definition of the function to get data
def read_data(name,start_date):
   df_asset = yf.download(name, start=start_date)
   df_asset['pct_change'] = df_asset['Adj Close'].pct_change(1)
   
   def to_percentage(x):
         return f"{x*100:.2f}%"
   df_asset['pct_change'] = df_asset['pct_change'].apply(to_percentage)
   
   return df_asset

#design the interface in the web app
stock_selected = st.selectbox(
   "Choose stock",
        ('BRK-B',
          'TWTR',
          '^NDX',
          'BNTX',
          'SQ',
          'AIR.PA',
          'MSFT',
          'GOOGL',
          'FB',
          'TSLA',
          'DM.V',
          '3CP.MU',
          'FRA.DE',
          'TTD',
          'LYMS.DE',
          'ZSRI.DE',
          'EUNN.DE',
          'DDD',
          '1COV.DE',
          'BAS.DE',
          'HDD.DE',
          'HPHA.DE',
          'AG1.F',
          'SAP.DE',
           'PYPL'
          ),
     )

#header
stock_name = stock_selected
start_date = '2024-01-01'

st.header(f"Timeline | Stock- {stock_name} | Start- {start_date}")

#First part of the web app
data = read_data(stock_name,start_date)

fig = px.line(data, 
              x=data.index, 
              y='Adj Close', 
              title=f'{stock_name} Stock Price')

fig.update_yaxes(range=[min(data['Adj Close'])*0.8, 
                        max(data['Adj Close'])*1.2])

st.plotly_chart(fig)

st.divider()

#Second part of the web app

st.markdown("## Last 10 days' detail")
data[-10:]