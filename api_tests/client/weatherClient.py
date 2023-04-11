import os
from pathlib import Path

import requests
import configparser

path = Path(__file__)
ROOT_DIR = path.parent.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

host = os.environ.get('HOST')
if host:
    config.set('TEST_APP', 'base_url', host)
    print(host)

user = config['TEST_USER']['username']
password = config['TEST_USER']['password']
url = config["TEST_APP"]["base_url"]

def get_weather_by_city(city, user=user, password=password):
    response = requests.get(url + "/weather/" + str.lower(city), auth=requests.auth.HTTPBasicAuth(user, password))
    return response


def get_weather_by_date(date, user=user, password=password):
    response = requests.get(url + "/weather/date/" + date, auth=requests.auth.HTTPBasicAuth(user, password))
    return response


def create_city_weather(city, weather, date, user=user, password=password):
    data = {
        "cityName": city,
        "weather": weather,
        "date": date
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url + "/weather", auth=requests.auth.HTTPBasicAuth(user, password), json=data,
                             headers=headers)
    return response


def getError(user=user, password=password):
    response = requests.get(url + "/error", auth=requests.auth.HTTPBasicAuth(user, password))
    return response


def getHelloWorld(user=user, password=password):
    response = requests.get(url + "/hello", auth=requests.auth.HTTPBasicAuth(user, password))
    return response
