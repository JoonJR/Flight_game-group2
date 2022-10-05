import mysql.connector
import geopy
from geopy.distance import geodesic
import random
import time
from time import sleep
import sys
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='136133136',
         autocommit=True
         )

def get_country():
    sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_airport(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%airport' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        print('This country does not exist, try again.')
        return None
country=get_country()
print(get_country())
print(get_airport(country))