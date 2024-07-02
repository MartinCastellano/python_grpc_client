# Project

## Prerequisites

This project requires Python 3.9 and pip to function correctly.

## Install Requirements

### To install the requirements, run the following command in the root folder

pip install -r ./requirements.txt

## Run Program

### Run the following command in the root folder. (This way the program should be run manually from the browser)

locust -f locustfile.py --master-host vacancies.cyrextech.net --master-port 7823 --users 3 --spawn-rate 30 --run-time 5m

### To start the program automatically, run the following command in the root folder

locust -f locustfile.py --master-host vacancies.cyrextech.net --master-port 7823 --users 3 --spawn-rate 30 --run-time 5m --autostart

## Result

### the result could be showed in <http://0.0.0.0:8089>
