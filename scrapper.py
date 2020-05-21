#!/usr/bin/env python3

# Weather Scrapper program from wunderground
# @sonbyj01

from datetime import datetime
import requests
# import time
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.wunderground.com/weather/us/ny/manhasset/11030"


def gather_information():
    # first checks if there's existing pickle file
    try:
        old_data = pd.read_pickle('./weather_data.pickle')
    except FileNotFoundError as fnf:
        old_data = pd.DataFrame()

    # requests for the web page
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}

    # gets current date and time
    now = datetime.now()
    data['Day'] = [now.strftime('%d')]
    data['Month'] = [now.strftime('%m')]
    data['Year'] = [now.strftime('%Y')]
    data['Hour'] = [now.strftime('%H')]
    data['Minute'] = [now.strftime('%M')]

    # retrieve temperature
    temperature_results = soup.find('span', class_="wu-value wu-value-to")
    temperature = str(temperature_results.contents[0])
    data['Temperature'] = [temperature]
    # print('{}: {}'.format('Temperature', temp))

    # retrieve additional information
    additional_information = {'Pressure': 'test-false wu-unit wu-unit-pressure ng-star-inserted',
                              'Visibility': 'test-false wu-unit wu-unit-distance ng-star-inserted',
                              'Dew Point': 'test-false wu-unit wu-unit-temperature ng-star-inserted',
                              'Humidity': 'test-false wu-unit wu-unit-humidity ng-star-inserted',
                              'Rainfall': 'test-false wu-unit wu-unit-rain ng-star-inserted',
                              'Snow Depth': 'test-false wu-unit wu-unit-snow ng-star-inserted'}
    for info in additional_information.keys():
        temp_results = soup.find('span', class_=additional_information[info])
        temp = str(temp_results.contents[3].contents[0])
        data[info] = [temp]
        # print(data)
        # print('{}: {}'.format(info, temp))

    # converts data into data frame
    df = pd.DataFrame(data)
    print(df)

    # sees if there's previous data and append, otherwise move on
    if old_data.empty:
        old_data = df
        print('empty')
    else:
        old_data = old_data.append(df, ignore_index=True)
        print('not empty')

    # stores into pickle file
    print(old_data)
    old_data.to_pickle('./weather_data.pickle')


def main():
    gather_information()
    # while True:
    #     gather_information()
    #     time.sleep(900)         # 15 minutes


if __name__ == "__main__":
    main()
