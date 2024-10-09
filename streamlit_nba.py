import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.express as px

#Definition of the function to get data
@st.cache_data
def get_team_list():

    df = pd.read_html('https://www.basketball-reference.com')
    df_west = df[1]
    df_west = df_west.rename(columns={"West": "teams"})
    df_west['teams'] = df_west['teams'].str[:3]
    #teams = df_west['teams']
    df_east = df[0]
    df_east = df_east.rename(columns={"East": "teams"})
    df_teams = pd.concat([df_west, df_east],ignore_index=True)
    df_teams['teams'] = df_teams['teams'].str[:3]
    teams = df_teams['teams']

    return teams.to_list()
    
def read_data(team,year):
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[1]
    return df_a

def read_adv_data(team,year):
    url = f'https://www.basketball-reference.com/teams/{team}/{year}.html'
    data = pd.read_html(url)
    df_a = data[3]
    return df_a
    
def scatter_plotly(df,team,year):
	fig = px.scatter(df,
                 x="OBPM",
                 y="DBPM",
                 size="MP")

	line_x = {'type': 'line',
			'x0': df['OBPM'].min(),
			'x1': df['OBPM'].max(),
			'y0': 0,
			'y1': 0,
			'line': {'color': 'red', 'width': 2}}
	
	line_y = {'type': 'line',
			'x0': 0,
			'x1': 0,
			'y0': df['DBPM'].min(),
			'y1': df['DBPM'].max(),
			'line': {'color': 'red', 'width': 2}}
 
                  
	fig.update_layout(shapes=[line_x, line_y])

	for i in range(len(df)):
		fig.add_annotation(x=df['OBPM'].iloc[i]+0.02, 
        					y=df['DBPM'].iloc[i]+0.02, 
                            text=df['Player'].iloc[i])    
	return fig

def scatter_matplotlib(df,team,year):        
	fig, ax = plt.subplots()
	sizes = data['MP']*0.1
	max_size = 200

	ax.scatter(x=df['OBPM'], 
          	   y=df['DBPM'],
           	   s=[size if size <= max_size else max_size for size in sizes],
           	   alpha=0.5)
    
	for i, label in enumerate(data['Player']):
		ax.annotate(label, 
					(data['OBPM'][i] + 0.1, 
                    data['DBPM'][i] + 0.1)
                    )

	return fig, ax

#Selection area
with st.sidebar:
	team_selected = st.selectbox('Team', get_team_list())
	plot_type = st.selectbox('Plot_method',('plotly','matplotlib'))
	year_selected = st.text_input('Season','2024')

#First part of the web app
st.markdown('## Stats per game players')

data_per_game = read_data(team_selected,year_selected)

data_per_game

st.divider()

#Second part of the web app
st.markdown('## Advanced stats players')

cols = ['Player','Age','G','MP','PER','TS%','OBPM','DBPM','BPM','VORP']

data = read_adv_data(team_selected,year_selected)[cols]

data = data[data['MP']> 400]

data

st.divider()

st.header("Scatter plot | x- OBPM | y- DBPM")

#Third part of the web app
if plot_type == 'matplotlib':
	fig,ax = scatter_matplotlib(df=data,
                                team=team_selected,
                                year=year_selected)
	st.pyplot(fig)
elif plot_type == 'plotly':
    fig = scatter_plotly(df=data,
                                team=team_selected,
                                year=year_selected)
    st.plotly_chart(fig)
