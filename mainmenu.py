import mysql.connector
import geopy
from geopy.distance import geodesic
import random
import time
from time import sleep
import sys
from continent_game_function import *
from Functions import *
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )
print("Welcome to Green Wash Airlines")
mainmenu = int(input("1. Continent game \n2. Europe game \n3. Quit \n"))
if mainmenu == 1:
    flight_game_continent()
elif mainmenu == 2:
    print("EU game")
elif mainmenu == 3:
    typewriter("Exiting the game.")

