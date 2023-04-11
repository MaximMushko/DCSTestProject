import os
from pathlib import Path

import jsonschema
import configparser
import pytest

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

from api_tests.client.weatherClient import *

user = config["TEST_USER"]["wronguser"]
password = config["TEST_USER"]["wrongpass"]

@pytest.fixture(scope="session", autouse=True)
def create_test_city_fixture():
    create_city_weather("test", "Cloudly", "2023-04-08")

def test_get_not_authorised():
    response = get_weather_by_city("test", user, password)
    assert response.status_code == 401


def test_get_status_code():
    response = get_weather_by_city("test")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


def test_get_response_schema():
    response = get_weather_by_city("test")
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "cityName": {"type": "string"},
                "weather": {"type": "string"},
                "date": {"type": "string", "format": "date"}
            }
        },
        "required": ["id", "cityName", "weather", "date"]
    }
    jsonschema.validate(response.json(), schema)


def test_get_weather_by_city():
    response = get_weather_by_city("test")
    body = response.json()
    assert len(body) > 0
    assert body[0]["cityName"] == "test"
    assert body[0]["weather"] == "Cloudly"
    assert body[0]["date"] == "2023-04-08"


def test_get_weather_wrong_city():
    response = get_weather_by_city("nocity")
    body = response.json()
    assert len(body) == 0


def test_get_weather_by_date_not_authorised():
    response = get_weather_by_date("2023-04-08", user, password)
    assert response.status_code == 401


def test_get_weather_by_date_schema():
    response = get_weather_by_date("2023-04-08")
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "cityName": {"type": "string"},
                "weather": {"type": "string"},
                "date": {"type": "string", "format": "date"}
            }
        },
        "required": ["id", "cityName", "weather", "date"]
    }
    jsonschema.validate(response.json(), schema)


def test_get_weather_by_date_status_code():
    response = get_weather_by_date("2023-01-01")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


def test_get_weather_by_date():
    response = get_weather_by_date("2023-04-08")
    body = response.json()
    assert len(body) > 0
    assert body[0]["date"] == "2023-04-08"


def test_get_weather_wrong_date():
    response = get_weather_by_date("2024-04-08")
    body = response.json()
    assert len(body) == 0


def test_post_weather_not_authorised():
    response = create_city_weather("MyTestCity", "Sunny", "2023-04-10", user, password)
    assert response.status_code == 401


def test_post_weather_status_code():
    response = create_city_weather("MyTestCity", "Sunny", "2023-04-10")
    assert response.status_code == 200


def test_post_weather():
    create_city_weather("MyTestCity", "Sunny", "2023-04-10")
    response = get_weather_by_city("MyTestCity")
    body = response.json()
    assert body[0]["cityName"] == "MyTestCity"
    assert body[0]["weather"] == "Sunny"
    assert body[0]["date"] == "2023-04-10"


def test_error_endpoint():
    response = getError()
    assert response.status_code == 500


def test_hello_endpoint():
    response = getHelloWorld()
    assert response.status_code == 200
    assert response.text == "Hello, world!"