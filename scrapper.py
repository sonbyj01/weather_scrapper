#!/usr/bin/env python3

# Weather Scrapper program from wunderground
# @sonbyj01

from datetime import datetime
from bs4 import BeautifulSoup
import sqlalchemy
import requests
import pandas as pd
import pymongo

# URL of specific location where data will be pulled from
URL = "https://www.wunderground.com/weather/us/ny/manhasset/11030"

# "database_dialect://user:password@host/database"
MONGODB_URL = 'mongodb://{{IP ADDRESS || HOST NAME}}:{{PORT}}/'
MONGODB_DATABASE = 'weather_scrapping'
MONGODB_COLLECTION = 'data'
POSTGRES_URL = 'postgresql://{{USERNAME}}:{{PASSWORD}}!@{{IP ADDRESS || HOST NAME}}:{{PORT}/{{DATABASE}}'
POSTGRES_TABLE = 'data'

# specify storing method based on individual case
STORING_METHOD = {
    'Pickle': False,
    'MongoDB': True,
    'Postgres': False
}


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
# https://www.datasciencelearner.com/insert-pandas-dataframe-into-mongodb/
def _to_mongodb(df):
    client = pymongo.MongoClient(MONGODB_URL)
    db = client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION]

    df_dict = df.to_dict('records')
    collection.insert_one(df_dict[0])


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html
# http://www.jan-langfellner.de/storing-a-pandas-dataframe-in-a-postgresql-database/
def _to_postgres(df):
    engine = sqlalchemy.create_engine(POSTGRES_URL)
    con = engine.connect()
    df.to_sql(POSTGRES_TABLE, con, if_exists='append')
    con.close()
    return


def _to_pickle_file(df):
    # first checks if there's existing pickle file
    try:
        old_data = pd.read_pickle('./weather_data.pickle')
    except FileNotFoundError as fnf:
        old_data = pd.DataFrame()

    # sees if there's previous data and append, otherwise move on
    if old_data.empty:
        old_data = df
    else:
        old_data = old_data.append(df, ignore_index=True)

    # stores into pickle file
    old_data.to_pickle('./weather_data.pickle')
    return


def store_information(df):
    if STORING_METHOD.get('Pickle'):
        _to_pickle_file(df)
    if STORING_METHOD.get('MongoDB'):
        _to_mongodb(df)
    if STORING_METHOD.get('Postgres'):
        _to_postgres(df)
    return


def gather_information():
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

    # converts data into data frame
    store_information(pd.DataFrame(data))
    return


def main():
    gather_information()


if __name__ == "__main__":
    main()
