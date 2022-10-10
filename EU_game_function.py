import mysql.connector
import ascii
from geopy.distance import geodesic
import random
import time
import sys
import os
from Functions import *
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def eugame():
    def get_country():
        sql = "SELECT country.name FROM  country WHERE continent = 'EU' order by RAND() LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                return row[0]


    def get_heliport_code(country):
        sql = "SELECT airport.ident FROM airport, country  WHERE country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country +"' AND airport.type = 'heliport' OR country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country +"' and airport.type = 'small_airport' OR country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country +"' and airport.type = 'medium_airport' order by (case when airport.type = 'heliport' then 1 else 2 END) LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if not result:
            print("This country does not exists or is not located in continent EU, try again.")
            return None

        if cursor.rowcount > 0:
            for row in result:
                return row[0]

    def get_heliport_name(code):
        sql = "SELECT airport.name FROM airport WHERE airport.ident ='" + code + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                return row[0]


    def get_location(code):  # returns long/lat of an airport
        location = []
        sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.ident ='" + code + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                location.append(int(row[1]))
                location.append(int(row[0]))
            return location


    def typewriter(rules):
        for char in rules:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(0.02)
            else:
                time.sleep(0.5)


    death_text = ["Your helicopter got struck by lightning and crashed on a remote island, you survived the crash and promptly died of dehydration. Game Over!",
                  "The pilot had one too many the night before and fell asleep at the wheel, nosediving the helicopter to your inevitable doom. Game Over!",
                  "You encountered some unexpected turbulence causing the pilot to lose complete control of the helicopter which hits the ground and explodes, but not before doing a cool flip. Game Over!",
                  "You poorly chose the meal with fish. You made it to your destination before dying of food poisoning in the airport bathroom. Game Over!",
                  "Someone's beloved pet cobra somehow escaped from its cage and found its way up your pants. Unfortunately you only realised this after it bit you. You took your last breath 15 minutes later. Game Over!"]

    neardeath_text = ["You tripped while leaving the helicopter and proceeded to fall down the stairs, you thought it was all over\n before the real Tom of Finland grabbed your arm, saving your life.",
                      "Some strong turbulence managed to open a loose baggage compartment. Someones weights fell out and almost hit you on the head.\nThankfully they hit the person next to you.",
                      "You were offered a meal choice of either fish or meat, you were about to choose fish before remembering the golden rule. That was a close one.",
                      "You somehow managed to flush the toilet without realising a part of your clothing was in there.\nYou got pulled back into the toilet but thankfully you had your second breakfast that morning.",
                      "Your helicopter was about to take off and then you quickly remembered you didnt change your phones mode to flight mode.\nYou frantically make the change before takeoff saving the lives of many. A true hero.",
                      "A bump in the sky during mealtime caused a swedish meatball to go down the wrong pipe. Thankfully a vet was nearby to help."]

    randomcountry_text = ["The pilot forgot to Never Eat Soggy Waffles and ended up going in the opposite direction.",
                          "Your pilot partied a bit too much the night before and didn't realise a change of schedule.",
                          "Your helicopter got hijacked by honeymooners who could not afford the flights for their dream trip",
                          "You accidentally got onto the wrong helicopter without anyone noticing"]

    fullrefund_text = ["You found an old coupon for a free flight on the floor of a public toilet. All expenses paid.",
                       "Some rich guy ahead of you was feeling generous and paid for your flight. No Co2 spent.",
                       "You forgot to buy the ticket and managed to sneak on the helicopter without getting caught. You even bumped yourself up to first class. No Co2 spent.",
                       "You spoke to the pilot on your way onto the helicopter and it turns out hes your sisters cousins uncles brother. He let you on for free. No Co2 spent.",
                       "You spoke to the pilot on your way onto the helicopter and it turns out hes your uncles sisters aunts nephew. He let you on for free. No Co2 spent."]


    player_name = input("\nEnter your name: ")

    rules = f"Hello " + player_name + "! You have been given the mission of travelling to all 50 EU-countries! You will be" \
    " given a fancy helicopter with a pilot and a Co2 budget of 10000 which you cannot exceed. For every 1000km you use 300 Co2.\n\
    Your starting location will be random. From that point you can choose to fly to any country, however the heliports will be random. \n\
    Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
    6. You get a full Co2 refund for that particular flight.\n\
    5. You get a 50% Co2 refund for that particular flight.\n\
    4. Your helicopter had to return to the previous heliport. Full amount of Co2 wasted for that trip.\n\
    3. Your helicopter flies through teleportal and you end up at a random destination anywhere in the world.\n\
    2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
    1. Worst possible scenario. You have a 50% chance of dying.\nGood luck!\nps if there are errors its your fault :p\n"

    #typewriter(rules)
    is_alive = True
    budget = 10000
    countries = []
    current_country = get_country()
    countries.append(current_country)
    destination = None
    current_heliport = None
    recent_heliport = ""

    while is_alive:

        if budget <= 0:
            print("You ran out of Co2 before reaching all the continents. Game Over!")
            is_alive = False  # you lost
            break

        while budget > 0 and is_alive:

            if len(countries) == 50:
                print("You won! You made it to all 50 countries without exceeding your budget!")
                is_alive = False  # you won! the game is finished
            recent_country = current_country

            if recent_heliport != "":
                print(f"You are currently in {recent_country} at {get_heliport_name(recent_heliport)}. Your current Co2 budget is {budget}. "
                      f"You have travelled to {len(countries)}/50 countries.\n")
                recent_heliport = ""
                destination = input("\nEnter the country you wish to travel to: ")
                destination_heliport = get_heliport_code(destination)

                while destination_heliport is None:
                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_heliport = get_heliport_code(destination)

                else:

                    number = random.randint(1, 6)
                    if number == 1:
                        possible_death = random.randint(1, 2)
                        if possible_death == 1:
                            death = death_text[random.randint(0, 4)]
                            typewriter(death)
                            is_alive = False
                            break
                        else:
                            distance = geodesic(get_location(get_heliport_code(current_country)),
                                                get_location(destination_heliport)).kilometers

                            budget -= int(distance / 3.3)  # calculates Co2
                            current_country = destination  # updates the current location
                            if current_country not in countries:
                                countries.append(current_country)  # appends country to the list
                            typewriter(neardeath_text[random.randint(0, 5)])
                            print(
                                f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 2:

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) * 2:.1f} Co2")

                    if number == 3:

                        current_country = get_country()
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)  # calculates Co2
                        typewriter(randomcountry_text[random.randint(0, 3)])
                        print(
                            f"\nYou ended up in {current_country}, {current_heliport}. Your flight was {distance:.1f}"
                            f" kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 4:

                        recent_heliport += current_heliport
                        destination_heliport = get_heliport_code(destination)
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)
                        print("Your helicopter had to return to the previous heliport. Full amount of Co2 had to be paid.")
                        print(f"Your flight was {0} kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 5:

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) / 2
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) / 2:.1f} Co2")

                    if number == 6:
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) - int(distance / 3.3)
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print(fullrefund_text[random.randint(0, 4)])
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")
            else:

                current_heliport = get_heliport_code(current_country)
                current_heliport_name = get_heliport_name(current_heliport)
                print(f"\nYou are currently in {current_country} at {current_heliport_name}. Your current Co2 budget is {budget}."
                      f" You have traveled to {len(countries)}/50 countries.")

                destination = input("\nEnter the country you wish to travel to: ")
                destination_heliport = get_heliport_code(destination)


                while destination_heliport is None:

                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_heliport = get_heliport_code(destination)

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
                            distance = geodesic(get_location(get_heliport_code(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 3.3)  # calculates Co2
                            current_country = destination  # updates the current location
                            if current_country not in countries:
                                countries.append(current_country)  # appends country to the list
                            typewriter(neardeath_text[random.randint(0, 5)])
                            print(
                                f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 2:  # 2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) * 2:.1f} Co2")

                    if number == 3:

                        current_country = get_country()
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)  # calculates Co2
                        typewriter(randomcountry_text[random.randint(0, 3)])
                        print(
                            f"\nYou ended up in {current_country}, {current_heliport}. Your flight was {distance:.1f}"
                            f" kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 4:

                        recent_heliport += current_heliport
                        destination_heliport = get_heliport_code(destination)
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)
                        print("Your helicopter had to return to the previous heliport. Full amount of Co2 had to be paid.")
                        print(f"Your flight was {0} kilometers and you had to pay {(distance / 3.3):.1f} Co2")

                    if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) / 2
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) / 2:.1f} Co2")

                    if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) - int(distance / 3.3)
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        print(fullrefund_text[random.randint(0, 4)])
                        print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")


    else:
        typewriter(f"\nYour score was: {len(countries) * 100}")

    while True:
        decision = input("\nWould you like to play again?(Y/N) ")
        if decision == "Y" or decision == 'y':
            os.system('cls')
            eugame()
        if decision == "N" or decision == 'n':
            typewriter("Flying back to the main menu. Please fasten your seatbelt...")
            time.sleep(1)
            os.system('cls') # opens main menu in a new page (clears everything before that) but doesnt work in pycharm only if its open as a .py file
            logo()
            return None
        else:
            typewriter("Invalid input!")