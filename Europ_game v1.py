from geopy.distance import geodesic
import random
from Functions import *
import os
# import mysql.connector
# import time
# import sys
# from ascii import *
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def flight_game_continent():
    def get_country():
        sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and country.continent like '%EU%' ORDER BY RAND() LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                return row[0]

    def get_heliport(country):
        sql = "SELECT airport.name FROM airport, country  WHERE country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country + "' AND airport.type = 'heliport' OR country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country + "' and airport.type = 'small_airport' OR country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country + "' and airport.type = 'medium_airport' order by (case when airport.type = 'heliport' then 1 else 2 END) LIMIT 1"
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

    country = get_country()
    country_d = get_heliport(country)

    def get_continent(country):  # returns continent
        sql = "SELECT country.continent FROM country WHERE country.name ='" + country + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if cursor.rowcount > 0:
            for row in result:
                return row[0]

    def check_countries(current_country):
        for x in range(len(country_list) - 1):
            if current_country == country_list[x]:
                country_list.remove(country_list[x])

    def typewriter(rules):
        for char in rules:
            sys.stdout.write(char)
            sys.stdout.flush()

            if char != "\n":
                time.sleep(0.02)
            else:
                time.sleep(0.5)

    death_text = [
        "Your helicopter got struck by lightning and crashed on a remote island, you survived the crash and promptly died of dehydration. Game Over!",
        "The pilot had one too many the night before and fell asleep at the wheel, nosediving the helicopter to your inevitable doom. Game Over!",
        "You encountered some unexpected turbulence causing the pilot to lose complete control of the helicopter which hits the ground and explodes, but not before doing a cool flip. Game Over!",
        "Helicopter hit a building at night! Game over!",
        "Some birds hit the propellers and pilot lost control! Game over!"]

    neardeath_text = [
        "You were drunk and high and tripped while leaving the helicopter and proceeded to fall down the stairs like a rockstar, you thought it was all over\n before the real Liam Gallagher grabbed your arm, saving your life.",
        "Your helicopter was about to take off and then you quickly remembered you didnt change your phones mode to flight mode.\nYou frantically make the change before takeoff saving the lives of many. A true hero.",
        "You forgot to close the door while helicopter takes off! Where is your mind!"]

    randomcountry_text = ["The pilot forgot to Never Eat Soggy Waffles and ended up going in the opposite direction.",
                          "Your pilot partied a bit too much the night before and didn't realise a change of schedule.",
                          "Your helicopter got hijacked by your crazy mate wants to hit it to World Trade Center",
                          "You accidentally got onto the wrong helicopter without anyone noticing"]

    fullrefund_text = ["You found an old coupon for a free flight on the floor of a public toilet. All expenses paid.",
                       "Some rich guy ahead of you was feeling generous and paid for your flight. No Co2 spent.",
                       "You forgot to buy the ticket and managed to sneak on the helicopter without getting caught. No Co2 spent.",
                       "You spoke to the pilot on your way onto the helicopter and it turns out hes your sisters cousins uncles brother. He let you on for free. No Co2 spent.",
                       "You spoke to the pilot on your way onto the helicopter and it turns out hes your uncles sisters aunts nephew. He let you on for free. No Co2 spent."]

    ascii_pictures(5)
    ascii_text(3)
    ascii_pictures(5)
    player_name = input("Enter your name: ")
    ascii_pictures(7)

    rules = "Hello " + player_name + "! You have been given the mission of travelling to as many as heliports in Europe! You will be given a helicopter and a Co2 budget of 10.000 which you cannot exceed. For every 1000km you use 200 Co2.\n\
    Your starting location will be random. From that point you can choose to fly to any country, however the heliport will be random. \nYou have 3 rounds/lives, you collect 100 points for each continent per round. \n\
    Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
    6. You get a full Co2 refund for that particular flight.\n\
    5. You get a 50% Co2 refund for that particular flight.\n\
    4. Your plane had to return to the previous heliport. Full amount of Co2 wasted for that trip.\n\
    3. Your helicopter's GPS breaks and you end up at a random destination anywhere in the world.\n\
    2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
    1. Worst possible scenario. You have a 50% chance of dying.\nGood luck!\nps if there are errors its your fault :p\n"

    typewriter(rules)

    rounds = 1
    score = 0
    score1 = 0
    score2 = 0

    while rounds != 4:
        is_alive = True
        budget = 10000
        current_country = get_country()
        country_list = ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria",
                        "Croatia", "Czech Republic", "Denmark", "Estonia", "Faroe Islands", "Finland", "France",
                        "Germany", "Gibraltar", "Greece", "Guernsey", "Hungary", "Iceland", "Ireland",
                        "Isle of Man", "Italy", "Kosovo", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta",
                        "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland",
                        "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia",
                        "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"]
        destination = None
        current_heliport = None
        recent_heliport = ""

        while is_alive:  # while the game is on and player is alive

            if budget <= 0:
                print("You ran out of Co2 before reaching all the continents. Game Over!")
                is_alive = False  # you lost
                break
            if len(country_list) == 0:
                ascii_pictures(9)
                print("You won! You made it to all 49 continents without exceeding your budget!")
                ascii_pictures(8)
                is_alive = False  # you won! the game is finished

            while budget > 0 and is_alive:

                recent_country = current_country

                if recent_heliport != "":

                    print(
                        f"You are currently in {recent_country} at {recent_heliport} . Your current Co2 budget is {budget}. You have traveled to {49 - len(country_list)}/49 country.\n")
                    score = ((49 - len(country_list)) * 100)
                    recent_airport = ""
                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_helipport = get_heliport(destination)

                    while destination_heliport is None:

                        destination = input("\nEnter the country you wish to travel to: ")
                        destination_heliport = get_heliport(destination)

                    else:

                        number = random.randint(1, 6)
                        print(f"Print-2  {number}")
                        if number == 1:  # 1. Worst possible scenario. You have a 50% chance of dying.
                            possible_death = random.randint(1, 2)
                            if possible_death == 1:
                                death_pic = death_text(0, 4)
                                death = death_text[death_pic]
                                ascii_pictures(death_pic)
                                typewriter(death)
                                is_alive = False
                                break
                            else:
                                distance = geodesic(get_location(get_heliport(current_country)),
                                                    get_location(destination_heliport)).kilometers
                                budget -= int(distance / 5)  # calculates Co2
                                current_country = destination  # updates the current location
                                check_countries(current_country)
                                typewriter(neardeath_text[random.randint(0, 5)])
                                print(
                                    f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 2:  # 2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                            distance = geodesic(get_location(get_heliport(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) * 2  # calculates Co2
                            current_country = destination  # updates the current location
                            check_countries(current_country)
                            print("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                            print(
                                f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5) * 2:.1f} Co2")

                        if number == 3:  # 3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\

                            random_country = get_country()
                            new_destination = get_heliport(random_country)
                            distance = geodesic(get_location(current_heliport),
                                                get_location(new_destination)).kilometers
                            budget -= int(distance / 5)  # calculates Co2
                            check_countries(current_country)
                            typewriter(randomcountry_text[random.randint(0, 3)])
                            print(
                                f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 4:  # 4. Your plane had to return to the previous airport. Full amount of Co2 wasted

                            recent_airport += current_heliport
                            distance = geodesic(get_location(get_location(current_heliport)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5)
                            print(
                                "Your helicopter had to return to the previous airport. Full amount of Co2 had to be paid.")
                            print(f"Your flight was {0} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                            distance = geodesic(get_location(get_heliport(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) / 2
                            current_country = destination
                            check_countries(current_country)
                            print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                            print(
                                f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5) / 2:.1f} Co2")

                        if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                            distance = geodesic(get_location(get_heliport(current_country)),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) - int(distance / 5)
                            current_country = destination
                            check_countries(current_country)
                            print(fullrefund_text[random.randint(0, 4)])
                            print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")

                else:

                    current_heliport = get_heliport(current_country)
                    print(
                        f"\nYou are currently in {current_country} at {current_heliport} in {get_continent(current_country)}. Your current Co2 budget is {budget}. You have traveled to {49 - len(country_list)}/49 countries.")

                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_heliport = get_heliport(destination)

                    while destination_heliport is None:

                        destination = input("\nEnter the country you wish to travel to: ")
                        destination_heliport = get_heliport(destination)

                    else:
                        number = random.randint(1, 6)
                        print(f"Print-1  {number}")
                        if number == 1:  # 1. Worst possible scenario. You have a 50% chance of dying.
                            possible_death = random.randint(1, 2)
                            if possible_death == 1:
                                deathpict = random.randint(0, 4)
                                death = death_text[deathpict]
                                typewriter(death)
                                ascii_pictures(deathpict)
                                is_alive = False
                                break
                            else:
                                distance = geodesic(get_location(current_heliport),
                                                    get_location(destination_heliport)).kilometers
                                budget -= int(distance / 5)  # calculates Co2
                                current_country = destination  # updates the current location
                                check_countries(current_country)
                                typewriter(neardeath_text[random.randint(0, 5)])
                                print(
                                    f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 2:  # 2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                            distance = geodesic(get_location(current_heliport),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) * 2  # calculates Co2
                            current_country = destination  # updates the current location
                            check_countries(current_country)
                            print("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                            print(
                                f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5) * 2:.1f} Co2")

                        if number == 3:  # 3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\

                            random_country = get_country()
                            new_destination = get_heliport(random_country)
                            distance = geodesic(get_location(current_heliport),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5)  # calculates Co2
                            check_countries(current_country)
                            typewriter(randomcountry_text[random.randint(0, 3)])
                            print(
                                f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 4:  # 4. Your plane had to return to the previous airport. Full amount of Co2 wasted

                            recent_heliport += current_heliport
                            distance = geodesic(get_location(current_heliport),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5)
                            print(
                                "Your helicopter had to return to the previous airport. Full amount of Co2 had to be paid.")
                            print(f"Your flight was {0} kilometers and you had to pay {(distance / 5):.1f} Co2")

                        if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                            distance = geodesic(get_location(current_heliport),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) / 2
                            current_country = destination
                            check_countries(current_country)
                            print("You got a good discount and only had to pay 50% of the original Co2 cost.")
                            print(
                                f"Your flight was {distance:.1f} kilometers and you had to pay {(distance / 5) / 2:.1f} Co2")

                        if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                            distance = geodesic(get_location(current_heliport),
                                                get_location(destination_heliport)).kilometers
                            budget -= int(distance / 5) - int(distance / 5)
                            current_country = destination
                            check_countries(current_country)
                            print(fullrefund_text[random.randint(0, 4)])
                            print(f"Your flight was {distance:.1f} kilometers and you had to pay {0} Co2")
        rounds += 1
        if rounds == 2:
            score1 = ((49 - len(country_list)) * 100)
            typewriter("\n\n✧✧✧✧✧✧✧✧✧✧✧✧✧✧Get ready for second round!✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧\n\n")
        if rounds == 3:
            score2 = ((49 - len(country_list)) * 100)
            typewriter("\n\n✧✧✧✧✧✧✧✧✧✧✧✧Get ready for third and last round!✧✧✧✧✧✧✧✧✧✧✧✧\n\n")

    else:
        ascii_text(4)
        final_score = score1 + score2 + score  # total max 2100
        typewriter(f"\n3 rounds played.\nYour score was: {final_score}")
        if final_score == 2100:
            print("\nGreat job! You collected all the continents!")
        elif 2100 > final_score >= 1000:
            print("\nGood job!")
        elif 1000 > final_score >= 300:
            print("\nYou can do better next time!")
        elif final_score < 300:
            print("\nDid you even try..?")

    while True:
        decision = input("\nWould you like to play again?(Y/N) ")
        if decision == "Y" or decision == 'y':
            flight_game_continent()
        if decision == "N" or decision == 'n':
            typewriter("Flying back to the main menu. Please fasten your seatbelt...")
            time.sleep(1)
            os.system(
                'cls')  # opens main menu in a new page (clears everything before that) but doesnt work in pycharm only if its open as a .py file
            logo()
            return None
        else:
            typewriter("Invalid input!")

