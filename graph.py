#!/usr/bin/env python3

import plotly.graph_objects as go
import pandas as pd

old_data = pd.read_pickle('./weather_data.pickle')

# create CSV file for readability
old_data.to_csv('./weather_data.csv', encoding='utf-8')

# generate plotly graph
date_time = []
temperature = []

for index, row in old_data.iterrows():
    date_time.append('{} {}, {}-{}:{}'.format(row['Month'],
                                              row['Day'],
                                              row['Year'],
                                              row['Hour'],
                                              row['Minute']))
    temperature.append(row['Temperature'])

fig = go.Figure()
fig.add_trace(go.Scatter(x=date_time, y=temperature, name='Temperature',
                         line=dict(color='royalblue', width=2)))
fig.update_layout(title='Recorded Weather Data',
                  xaxis_title='[Month] [Day], [Year]-[Hour]:[Minute]',
                  yaxis_title='Temperature (F)')
fig.show()
