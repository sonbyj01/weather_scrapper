#!/bin/bash

# Weather scrapper script for cron
# @sonbyj01

# add script to crontab to run every 15 minutes:
# $ crontab -e
# */15 * * * * helen /home/helen/projects/weather_scrapper/script.sh

# sources the virtual environment needed to run the program
source /home/helen/projects/weather_scrapper/venv/bin/activate

# turns to executable
chmod +x /home/helen/projects/weather_scrapper/scrapper.py

# runs the program
/home/helen/projects/weather_scrapper/scrapper.py

# deactivates the virtual environment
deactivate
