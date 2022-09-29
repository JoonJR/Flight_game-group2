import mysql.connector
import geopy
from geopy.distance import geodesic
import random
import time
from time import sleep
import sys
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def get_country():
    sql = "SELECT country.name FROM country ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_airport(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result==[]:
        print('This country does not exist, try again.')
        return None
        get_airport2(country)
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


    # else:     #If user enters invalid country, asks to repeat a country until
    #     get_airport(country)


def get_airport2(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_continent(country): #returns continent
    sql = "SELECT country.continent FROM country WHERE country.name ='" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_location(airport): #returns long/lat of an airport
    location = []
    sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.name ='" + airport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(row[1])
            location.append(row[0])
        return location


def check_continents(current_continent): # checks the list with the continents and removes it if the current continent is the same as in the list
    for x in range(len(continents) - 1):
        if current_continent == continents[x]:
            continents.remove(continents[x])


def dice_chance():  # rolling the dice befor each flight(NOT FINISHED)
    number = random.randint(1, 6)
    if number == 1:  # 50% chance of dying
        print("You died.")
    elif number == 2:
        print("double the amount of Co2 consumed.")
        # double the amount of Co2 consumed.
    elif number == 3:
        print("Your planes GPS breaks and you end up at a random destination anywhere in the world.")
        # random country
    elif number == 4:
        print("Your plane had to return to the previous airport. Full amount of Co2 wasted.")
        # Your plane had to return to the previous airport. Full amount of Co2 wasted
    elif number == 5:
        print("50% discount on co2.")
        # 50% discount
    else:
        print("100% discount on co2")
        # 100% discount
    return number


def typewriter(rules):
    for char in rules:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.5)


death_text = ["Your plane got struck by lightning and crashed on a remote island, you survived the crash and promptly died of dehydration. Game Over!",
              "The pilot had one too many the night before and fell asleep at the wheel, nosediving the plane to your inevitable doom. Game Over!",
              "You encountered some unexpected turbulence causing the pilot to lose complete control of the plane which hits the ground and explodes, but not before doing a cool flip. Game Over!",
              "You poorly chose the meal with fish. You made it to your destination before dying of food poisoning in the airport bathroom. Game Over!",
              "Someone's beloved pet cobra somehow escaped from its cage and found its way up your pants. Unfortunately you only realised this after it bit you. You took your last breath 15 minutes later. Game Over!"]


is_alive = True
budget = 4000
continents = ["EU", "AF", "NA", "SA", "OC", "AS", "AN"] # list that stores all the continents
player_name = input("Enter your name: ")

rules = "Hello " + player_name + "! You have been given the mission of travelling to all 7 continents! You will be given a plane and a Co2 budget of 4000 which you cannot exceed. For every 1000km you use 100 Co2.\n\
Your starting location will be random. From that point you can choose to fly to any country, however the airport will be random.\n\
Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
6. You get a full Co2 refund for that particular flight.\n\
5. You get a 50% Co2 refund for that particular flight.\n\
4. Your plane had to return to the previous airport. Full amount of Co2 wasted for that trip.\n\
3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\
2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
1. Worst possible scenario. You have a 50% chance of dying."





#typewriter(rules)
current_country = get_country()
check_continents(get_continent(current_country))
destination = None

while is_alive: #while the game is on and player is alive

    if budget <= 0:
        print("You ran out of Co2 before reaching all the continents. Game Over!")
        break
        is_alive = False # you lost
    if len(continents) == 0:
        print("You won! You made it to all 7 continents without exceeding your budget!")
        is_alive = False # you won! the game is finished



    while budget > 0 and is_alive:
        print(f"You are currently in {current_country} at {get_airport(current_country)} in {get_continent(current_country)}. Your current Co2 budget is {budget}. You have traveled to {7 - len(continents)}/7 continents.")

        destination = input("Enter the country you wish to travel to: ")
        destination_country = get_airport(destination)
        if destination_country == None:
            continue

        number = dice_chance()
        if number == 1:

            print(death_text[random.randint(0, 4)])
            is_alive = False
            break
        if number == 2:


            distance = geodesic(get_location(get_airport(current_country)), get_location(destination_country)).kilometers # calculates the distance
            budget -= int(distance / 10)*2 # calculates Co2
            current_country = destination # updates the current location
            check_continents(get_continent(current_country))
            print(f"Your flight was {distance:.1f} kilometers")

        if number == 3:


            distance = geodesic(get_location(get_airport(current_country)), get_location(destination_country)).kilometers # calculates the distance
            budget -= int(distance / 10) # calculates Co2
            check_continents(get_continent(current_country))
            print(f"Your flight was {distance:.1f} kilometers")
        if number == 4:

            destination_country = get_airport2(destination)
            distance = geodesic(get_location(get_airport(current_country)), get_location(destination_country)).kilometers # calculates the distance
            budget -= int(distance / 10) # calculates Co2

        if number == 5:


            distance = geodesic(get_location(get_airport(current_country)), get_location(destination_country)).kilometers # calculates the distance
            budget -= int(distance / 10) / 2 # calculates Co2
            current_country = destination # updates the current location
            check_continents(get_continent(current_country))
            print(f"Your flight was {distance:.1f} kilometers")
        if number == 6:


            distance = geodesic(get_location(get_airport(current_country)), get_location(destination_country)).kilometers # calculates the distance
            budget -= int(distance / 10) - int(distance / 10) # calculates Co2
            current_country = destination # updates the current location
            check_continents(get_continent(current_country))
            print(f"Your flight was {distance:.1f} kilometers")

        break