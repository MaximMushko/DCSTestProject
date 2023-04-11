# DCSTestProject
Technical Assessment for DCS

This is the siple sprint-boot app with the following endpoints

1. <code>POST /wether</code>
To create a weather for a city using the following schema
<code>
{
cityName: string,
weather: string,
date: date
}
</code>

2. <code>GET /weather/{cityName}</code>
To get all available weather entries for a patrucular city

3. <code>GET /weather/date/{date}</code>
To get all available weather entries for a particular date

4. <code>GET /error</code>
To throw 500 Internal Server Error

5. <code>GET /hello</code>
To print Hello, world!


To run the appilcation execute the command

<code>mvn package spring-boot:repackage</code>
<code>docker compose up</code>

Docker compose run 2 containers for Redis Cache and for the Application

To run the Python tests execute the command

<code>pip install api_test/requirement.txt
  PYTHONPATH=. pytest api_tests/tests/apitest.py
</code>

Expected that 2 tests will fail:
One because of the known issue with lowercase for a cityName from <code>GET /weather/{cityName}</code>
Second becuase of the 500 from <code>GET /error</code> endpoint
