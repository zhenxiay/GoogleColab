
import streamlit as st
import datetime
import pandas as pd
import yfinance as yf
import numpy as np
import plotly.express as px
#from abstract_stock_data import StockData
from abc import ABC, abstractmethod
import cufflinks as cf
from plotly.offline import iplot
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

#Abstract class definition
class StockDataStructure(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def create_fig(self):
        pass
    
#Define class for getting and displaying stock data
class StockData(StockDataStructure):
    
	def __init__(self, name, start_date):
		self.name = name
		self.start_date = start_date
    
	def read_data(self):
		df_asset = yf.download(self.name, start=self.start_date)
		df_asset['pct_delta_1_day'] = df_asset['Adj Close'].pct_change(1)
		df_asset['pct_delta_7_day'] = df_asset['Adj Close'].pct_change(7)
     
		def to_percentage(x):
			return f"{x*100:.2f}%"
    
		for col in ('pct_delta_1_day', 'pct_delta_7_day'):
			df_asset[col] = df_asset[col].apply(to_percentage)
           
		return df_asset
  
	def create_fig(self):
		data = self.read_data()

		fig = px.line(data, 
                      x=data.index, 
                      y='Adj Close', 
                      title=f'{self.name} Stock Price')
		return fig
      
	def create_cf_fig(self):
		data = self.read_data()
    
		qf = cf.QuantFig(data, 
        				title=f'Stock Dashboard - {self.name}', 
        				legend = 'right', 
                        name = f'{self.name}')
		qf.iplot()             
		return qf
        
#design the interface in the web app

col1, col2 = st.columns(2)

with col1:

    date_selected = st.date_input("Select start date", 
                           datetime.date(2024, 1, 1)
                              )
    
with col2:

    stock_selected = st.selectbox(
            "Choose stock",
            (
            'LYMS.DE',
            'ZSRI.DE',
            'EUNN.DE',
            'BRK-B',
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
st.header(f"Timeline | Stock- {stock_selected} | Start- {date_selected}")

#First part of the web app
stock_data = StockData(stock_selected, date_selected)
data = stock_data.read_data()

fig = stock_data.create_fig()

fig.update_yaxes(range=[min(data['Adj Close'])*0.8, 
                        max(data['Adj Close'])*1.2])

st.plotly_chart(fig)

st.divider()
#Second part of the web app
#fig_qf = stock_data.create_cf_fig()

#fig_qf.iplot()

#st.plotly_chart(fig_qf)

#st.divider()

#Third part of the web app

st.markdown("## Last 10 days' detail")
data[-10:]