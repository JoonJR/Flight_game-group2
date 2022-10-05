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
         password='root',
         autocommit=True
         )

round = 0
country_list = set()
airport_list =set()
while round != 45:
    def get_country_1():
        sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                return row[0]

    def get_airport_1(country):
        sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%airport' ORDER BY RAND() LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if not result:
            print('This country does not exist, try again.')
            return None

        if cursor.rowcount > 0:
            for row in result:
                return row[0]


    country = get_country_1()
    country_list.add(get_country_1())
    airport_list.add(get_airport_1(country))
    round+=1


print(country_list)
print(airport_list)



def get_country2():
    sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_airport2(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%airport' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        print('This country does not exist, try again.')
        return None

    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_airport3(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_location(airport):  # returns long/lat of an airport
    location = []
    sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.name ='" + airport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(int(row[1]))
            location.append(int(row[0]))
        return location


player_name = input("Enter your name: ")


rounds = 1
score = 0
score1 = 0
score2 = 0

while rounds != 4:
    is_alive = True
    budget = 4000
    current_country =get_country1()
    destination = None
    current_airport = None
    recent_airport = ""

    while is_alive:
        if budget <= 0:
            print("You ran out of Co2 before reaching all countrys. Game Over!")
            is_alive = False
            break
        if len(country_list)==0:
            print("you won! You made it to all 7 continents without exceeding your budget!")
            is_alive = False
        while budget > 0 and is_alive:
            recent_country = current_country
            if recent_airport != "":
                print(
                    f"You are currently in {recent_country} at {recent_airport} in EU . Your current Co2 budget is {budget}. You have traveled to {7 - len(continents)}/7 continents.\n")

