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
"""""
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
        sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%heliport' ORDER BY RAND() LIMIT 1"
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
"""""


def get_country2():
    sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_heliport2(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%heliport' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        print('This country does not exist, try again.')
        return None

    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_heliport3(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' and airport.type like '%heliport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def get_location(heliport):  # returns long/lat of an airport
    location = []
    sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.name ='" + heliport + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(int(row[1]))
            location.append(int(row[0]))
        return location


country= get_country2()
country_d= get_heliport2(country)
def get_continent(country):  # returns continent
    sql = "SELECT country.continent FROM country WHERE country.name ='" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]

def check_countries(current_country):
    for x in range(len(country_list)-1):
        if current_country==country_list[x]:
            country_list.remove(country_list[x])
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

neardeath_text = ["You tripped while leaving the plane and proceeded to fall down the stairs, you thought it was all over\n before the real Tom of Finland grabbed your arm, saving your life.",
                  "Some strong turbulence managed to open a loose baggage compartment. Someones weights fell out and almost hit you on the head.\nThankfully they hit the person next to you.",
                  "You were offered a meal choice of either fish or meat, you were about to choose fish before remembering the golden rule. That was a close one.",
                  "You somehow managed to flush the toilet without realising a part of your clothing was in there.\nYou got pulled back into the toilet but thankfully you had your second breakfast that morning.",
                  "Your plane was about to take off and then you quickly remembered you didnt change your phones mode to flight mode.\nYou frantically make the change before takeoff saving the lives of many. A true hero.",
                  "A bump in the sky during mealtime caused a swedish meatball to go down the wrong pipe. Thankfully a vet was nearby to help."]

randomcountry_text = ["The pilot forgot to Never Eat Soggy Waffles and ended up going in the opposite direction.",
                      "Your pilot partied a bit too much the night before and didn't realise a change of schedule.",
                      "Your plane got hijacked by honeymooners who could not afford the flights for their dream trip",
                      "You accidentally got onto the wrong plane without anyone noticing"]

fullrefund_text = ["You found an old coupon for a free flight on the floor of a public toilet. All expenses paid.",
                   "Some rich guy ahead of you was feeling generous and paid for your flight. No Co2 spent.",
                   "You forgot to buy the ticket and managed to sneak on the plane without getting caught. You even bumped yourself up to first class. No Co2 spent.",
                   "You spoke to the pilot on your way onto the plane and it turns out hes your sisters cousins uncles brother. He let you on for free. No Co2 spent.",
                   "You spoke to the pilot on your way onto the plane and it turns out hes your uncles sisters aunts nephew. He let you on for free. No Co2 spent."]

# list that stores all the continents
player_name = input("Enter your name: ")

rules = "Hello " + player_name + "! You have been given the mission of travelling to all 49 continents! You will be given a plane and a Co2 budget of 4000 which you cannot exceed. For every 1000km you use 100 Co2.\n\
Your starting location will be random. From that point you can choose to fly to any country, however the airport will be random. \nYou have 3 rounds/lives, you collect 100 points for each continent per round. \n\
Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
6. You get a full Co2 refund for that particular flight.\n\
5. You get a 50% Co2 refund for that particular flight.\n\
4. Your plane had to return to the previous airport. Full amount of Co2 wasted for that trip.\n\
3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\
2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
1. Worst possible scenario. You have a 50% chance of dying.\nGood luck!\nps if there are errors its your fault :p\n"

#typewriter(rules)

rounds = 1
score = 0
score1 = 0
score2 = 0

while rounds != 4:
    is_alive = True
    budget = 4000
    current_country =get_country2()
    country_list = [["Albania","Andorra","Austria","Belarus","Belgium","Bosnia and Herzegovina","Bulgaria","Croatia","Czech Republic","Denmark","Estonia","Faroe Islands","Finland","France","Germany","Gibraltar","Greece","Guernsey","Hungary","Iceland","Ireland",
                    "Isle of Man","Italy","Kosovo","Latvia","Liechtenstein","Lithuania","Luxembourg","Malta","Moldova","Monaco","Montenegro","Netherlands","North Macedonia","Norway","Poland","Portugal","Romania","Russia","San Marino","Serbia","Slovakia","Slovenia",
                    "Spain","Sweden","Switzerland","Ukraine","United Kingdom","Vatican City"]]
    destination = None
    current_heliport = None
    recent_heliport = ""

    while is_alive:  # while the game is on and player is alive

        if budget <= 0:
            print("You ran out of Co2 before reaching all the continents. Game Over!")
            is_alive = False  # you lost
            break
        if len(country_list) == 0:
            print("You won! You made it to all 49 continents without exceeding your budget!")
            is_alive = False  # you won! the game is finished

        while budget > 0 and is_alive:

            recent_country = current_country

            if recent_heliport != "":

                print(
                    f"You are currently in {recent_country} at {recent_heliport} . Your current Co2 budget is {budget}. You have traveled to {49 - len(country_list)}/49 country.\n")
                score = ((49 - len(country_list)) * 100)
                recent_airport = ""
                destination = input("\nEnter the country you wish to travel to: ")
                destination_helipport = get_heliport2(destination)

                while destination_heliport is None:

                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_heliport = get_heliport2(destination)

                else:

                    number = random.randint(1, 6)
                    if number == 1:  # 1. Worst possible scenario. You have a 50% chance of dying.
                        possible_death = random.randint(1, 2)
                        if possible_death == 1:
                            death = death_text[random.randint(0, 4)]
                            typewriter(death)
                            is_alive = False
                            break
                        else:
                            distance = geodesic(get_location(get_heliport2(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 10)  # calculates Co2
                            current_country = destination  # updates the current location
                            check_countries(current_country)
                            typewriter(neardeath_text[random.randint(0, 5)])
                            print(
                                f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 2:  # 2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        check_countries(current_country)
                        print("Your plane had to take an unexpected detour, doubling the cost of Co2.")
                        print(
                            f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10) * 2:.1f} Co2")

                    if number == 3:  # 3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\

                        current_country = get_country2()
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10)  # calculates Co2
                        check_countries()
                        typewriter(randomcountry_text[random.randint(0, 3)])
                        print(
                            f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 4:  # 4. Your plane had to return to the previous airport. Full amount of Co2 wasted

                        recent_airport += current_heliport
                        destination_heliport = get_heliport2(destination)
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10)
                        print("Your plane had to return to the previous airport. Full amount of Co2 had to be paid.")
                        print(f"Your flight was {0} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) / 2
                        current_country = destination
                        check_countries(current_country)
                        print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        print(
                            f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10) / 2:.1f} Co2")

                    if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) - int(distance / 10)
                        current_country = destination
                        check_countries(current_country)
                        print(fullrefund_text[random.randint(0, 4)])
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")

            else:

                current_heliport = get_heliport2(current_country)
                print(
                    f"\nYou are currently in {current_country} at {current_heliport} in {get_continent(current_country)}. Your current Co2 budget is {budget}. You have traveled to {49 - len(country_list)}/49 continents.")

                destination = input("\nEnter the country you wish to travel to: ")
                destination_heliport = get_heliport2(destination)

                while destination_heliport is None:

                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_heliport = get_heliport2(destination)

                else:
                    number = random.randint(1, 6)
                    if number == 1:  # 1. Worst possible scenario. You have a 50% chance of dying.
                        possible_death = random.randint(1, 2)
                        if possible_death == 1:
                            death = death_text[random.randint(0, 4)]
                            typewriter(death)
                            is_alive = False
                            break
                        else:
                            distance = geodesic(get_location(get_heliport2(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 10)  # calculates Co2
                            current_country = destination  # updates the current location
                            check_countries(current_country)
                            typewriter(neardeath_text[random.randint(0, 5)])
                            print(
                                f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 2:  # 2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        check_countries(current_country)
                        print("Your plane had to take an unexpected detour, doubling the cost of Co2.")
                        print(
                            f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10) * 2:.1f} Co2")

                    if number == 3:  # 3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\

                        current_country = get_country2()
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10)  # calculates Co2
                        check_countries(current_country)
                        typewriter(randomcountry_text[random.randint(0, 3)])
                        print(
                            f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 4:  # 4. Your plane had to return to the previous airport. Full amount of Co2 wasted

                        recent_heliport += current_heliport
                        destination_heliport = get_heliport2(destination)
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10)
                        print("Your plane had to return to the previous airport. Full amount of Co2 had to be paid.")
                        print(f"Your flight was {0} kilometers and you had to pay {(distance / 10):.1f} Co2")

                    if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) / 2
                        current_country = destination
                        check_countries(current_country)
                        print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        print(
                            f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10) / 2:.1f} Co2")

                    if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                        distance = geodesic(get_location(get_heliport2(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 10) - int(distance / 10)
                        current_country = destination
                        check_countries(get_continent(current_country))
                        print(fullrefund_text[random.randint(0, 4)])
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")
    rounds += 1
    if rounds == 2:
        score1 = ((49 - len(country_list)) * 100)
        typewriter("\n\nGet ready for second round!\n\n")
    if rounds == 3:
        score2 = ((49 - len(country_list)) * 100)
        typewriter("\n\nGet ready for third and last round!\n\n")
else:
    typewriter(f"\n3 rounds played. Game over.\n Your score was: {(score1 + score2 + score)}")
