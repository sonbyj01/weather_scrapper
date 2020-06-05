# Weather Scrapper
[Blog Post](https://blog.hson.dev/projects/2020/05/24/Automate-web-scrapping-weather.html)

- **.gitignore** - don't include certain files/folder that I use for development
- **README.md** - it's what you're reading right now dummy
- **graph.py** - python script that will graph 'weather_data.pickle' using Plotly 
- **requirements.txt** - the required packages in order to run *graph.py* and *scrapper.py*
- **scrapper.py** - python script that will pull data from wunderground and save it to 'weather_data.pickle'
- **script.sh** - bash script that will run your *scrapper.py* automatically if you run this script (meant as crontab task)

## Setting up virtual environment
I recommend that you create and use virtual environments and then installing the requirements into the virtual environment.
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Modifying the programs(s)
**scrapper.py**: 
```python3
URL = "https://www.wunderground.com/weather/us/ny/manhasset/11030" (line 12)
```
Change this to the URL that you want to get data from. 
```python3
MONGODB_URL = 'mongodb://{{IP ADDRESS || HOST NAME}}:{{PORT}}/'
MONGODB_DATABASE = 'weather_scrapping'
MONGODB_COLLECTION = 'data'
POSTGRES_URL = 'postgresql://{{USERNAME}}:{{PASSWORD}}!@{{IP ADDRESS || HOST NAME}}:{{PORT}/{{DATABASE}}'
POSTGRES_TABLE = 'data'
```
Update the MongoDB and/or Postgres urls if you want to save the data to a database.
```python3
STORING_METHOD = {
    'Pickle': False,
    'MongoDB': True,
    'Postgres': False
}
```
Pick which saving method you want to perform.
 
**script.sh**: Change the absolute paths if you want to run this script using crontab. 

## Running the program 
Now the whole purpose of this small project was so you can keep this running 24/7. If you want to run this once just to verify the program works, 
you can either run the program as an executable or python3 script. 
```bash
# As an executable
$ chmod +x scrapper.py
$ ./scrapper.py

# As python3 script
$ python3 scrapper.py
```

You should then see a file produced: weather_data.pickle.

Now you can see this data by running the graph program, by either running it as an executable or python3 script. 
```bash
# As an executable
$ chmod +x graph.py
$ ./graph.py

# As python3 script
$ python3 graph.py
```

I will get around to pulling and graphing data points from databases eventually...