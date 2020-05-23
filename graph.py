#!/usr/bin/env python3

import plotly.graph_objects as go
import plotly
import pandas as pd

old_data = pd.read_pickle('./weather_data.pickle')

# create CSV file for readability
old_data.to_csv('./weather_data.csv', encoding='utf-8')

# generate plotly graph
date_time = []
temperature = []
dew_point = []
humidity = []
rainfall = []

for index, row in old_data.iterrows():
    date_time.append('{} {}, {}-{}:{}'.format(row['Month'],
                                              row['Day'],
                                              row['Year'],
                                              row['Hour'],
                                              row['Minute']))
    temperature.append(row['Temperature'])
    dew_point.append(row['Dew Point'])
    humidity.append(row['Humidity'])
    rainfall.append(row['Rainfall'])

fig = go.Figure()

fig.add_trace(
    go.Scatter(x=date_time, y=temperature, name='Temperature',
               line=dict(color='royalblue', width=2))
)
fig.add_trace(
    go.Scatter(x=date_time, y=dew_point, name='Dew Point',
               line=dict(color='firebrick', width=2))
)
fig.add_trace(
    go.Scatter(x=date_time, y=humidity, name='Humidity',
               line=dict(color='royalblue', width=2, dash='dot'))
)
fig.add_trace(
    go.Scatter(x=date_time, y=rainfall, name='Rainfall',
               line=dict(color='firebrick', width=2, dash='dot'))
)

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label='Weather Data',
                     method='update',
                     args=[{'visible': [True, True, True, True]},
                           {'title': 'Weather Data'}]),
                dict(label='Temperature',
                     method='update',
                     args=[{'visible': [True, False, False, False]},
                           {'title': 'Temperature'}]),
                dict(label='Dew Point',
                     method='update',
                     args=[{'visible': [False, True, False, False]},
                           {'title': 'Dew Point'}]),
                dict(label='Humidity',
                     method='update',
                     args=[{'visible': [False, False, True, False]},
                           {'title': 'Humidity'}]),
                dict(label='Rainfall',
                     method='update',
                     args=[{'visible': [False, False, False, True]},
                           {'title': 'Rainfall'}]),
                dict(label='Temperature and Dew Point',
                     method='update',
                     args=[{'visible': [True, True, False, False]},
                           {'title': 'Rainfall'}]),
                dict(label='Humidity and Rainfall',
                     method='update',
                     args=[{'visible': [False, False, True, True]},
                           {'title': 'Humidity and Rainfall'}]),
            ])
        )
    ]
)

fig.show()

# ---------------------------------------------

# data = [go.Scatter(x=date_time, y=temperature, name='Temperature',
#                    line=dict(color='royalblue', width=2)),
#         go.Scatter(x=date_time, y=dew_point, name='Dew Point',
#                    line=dict(color='firebrick', width=2)),
#         go.Scatter(x=date_time, y=humidity, name='Humidity',
#                    line=dict(color='royalblue', width=2, dash='dot')),
#         go.Scatter(x=date_time, y=rainfall, name='Rainfall',
#                    line=dict(color='firebrick', width=2, dash='dot')),
#         ]
#
# update_menus = list(
#     [dict(active=-1,
#           buttons=list([
#               dict(label='Weather Data',
#                    method='update',
#                    args=[{'visible': [True, True, True, True]},
#                          {'title': 'Weather Data'}]),
#               dict(label='Temperature',
#                    method='update',
#                    args=[{'visible': [True, False, False, False]},
#                          {'title': 'Temperature'}]),
#               dict(label='Dew Point',
#                    method='update',
#                    args=[{'visible': [False, True, False, False]},
#                          {'title': 'Dew Point'}]),
#               dict(label='Humidity',
#                    method='update',
#                    args=[{'visible': [False, False, True, False]},
#                          {'title': 'Humidity'}]),
#               dict(label='Rainfall',
#                    method='update',
#                    args=[{'visible': [False, False, False, True]},
#                          {'title': 'Rainfall'}]),
#           ]),
#           )
#      ]
# )
#
# layout = dict(title='Weather Data', showlegend=True,
#               updatemenus=update_menus)
#
# fig = dict(data=data, layout=layout)
#
# plotly.offline.plot(fig, auto_open=True, show_link=False)

# ---------------------------------------------

# fig.add_trace(go.Scatter(x=date_time, y=temperature, name='Temperature',
#                          line=dict(color='royalblue', width=2)))
# fig.update_layout(title='Recorded Weather Data',
#                   xaxis_title='[Month] [Day], [Year]-[Hour]:[Minute]',
#                   yaxis_title='Temperature (F)')
# fig.show()
