#!/bin/bash

# Weather scrapper script for cron
# @sonbyj01

# sources the virtual environment needed to run the program
source /home/helen/projects/weather_scrapping/venv/bin/activate

# turns to executable
chmod +x /home/helen/projects/weather_scrapping/scrapper.py

# runs the program
/home/helen/projects/weather_scrapping/scrapper.py

# deactivates the virtual environment
deactivate