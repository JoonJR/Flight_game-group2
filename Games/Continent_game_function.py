from geopy.distance import geodesic
import random
from Functions.Functions import *
import os
from Functions.Continent_game_functions import *


def flight_game_continent():

    def check_continents(current_continent):  # checks the list with the continents and appends it if the current continent is not in the list
        if current_continent not in continents:
            continents.append(current_continent)

    ascii_text(3)
    player_name = input("Enter your name: ")
    ascii_pictures(7)
    rules = "Hello " + player_name + "! You have been given the mission of travelling to all 7 continents! You will be given a plane and a Co2 budget of 4000 which you cannot exceed. For every 1000km you use 100 Co2.\n\
Your starting location will be random. From that point you can choose to fly to any country, however the airport will be random.\nYou have 3 rounds/lives, you collect 100 points for each continent per round. \n\
Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
    6. You get a full Co2 refund for that particular flight.\n\
    5. You get a 50% Co2 refund for that particular flight.\n\
    4. Your plane had to return to the previous airport. Full amount of Co2 wasted for that trip.\n\
    3. Your planes GPS breaks and you end up at a random destination anywhere in the world.\n\
    2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
    1. Worst possible scenario. You have a 50% chance of dying.\nGood luck!\nps if there are errors its your fault :p\n"
    typewriter(rules)
    ascii_pictures(7)

    rounds = 1
    score = 0
    score1 = 0
    score2 = 0

    while rounds != 4:

        is_alive = True
        budget = 4000
        continents = []  # list that stores all the continents
        current_country = get_country()  # a random starting point
        current_continent = (get_continent(current_country))
        continents.append(current_continent)
        #destination = None  to be deleted perhaps
        current_airport = None
        recent_airport = ""  # used only if you roll 4 -> the plane returns to the same airport

        while is_alive:  # while the game is on and player is alive

            if budget <= 0: #the game ends if you run out of the budget
                print("You ran out of Co2 before reaching all the continents.")
                is_alive = False  # you lost
                break

            while budget > 0 and is_alive:

                if len(continents) == 7: # if all 7 continents are collected
                    ascii_pictures(9)
                    typewriter("\nYou won! You made it to all 7 continents without exceeding your budget!\n\n")
                    ascii_pictures(8)
                    is_alive = False  # you won! the game is finished
                    break

                recent_country = current_country  # only for roll 4

                if recent_airport != "":  # this whole thing is only used if you roll 4

                    typewriter(f"\nYou are currently in {recent_country} at {get_airport_name(recent_airport)} in {get_continent(recent_country)}. Your current Co2 budget is {budget}. You have traveled to {len(continents)}/7 continents.")
                    score = ((len(continents)) * 100)
                    recent_airport = ""
                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_airport = get_airport_code(destination) # gets a random airport ICAO of the country you wish to fly to

                    while destination_airport is None:  # if entered country is invalid

                        destination = input("\nEnter the country you wish to travel to: ")
                        destination_airport = get_airport_code(destination)

                    else:

                        number = random.randint(1, 6)
                        if number == 1:  # You have a 50% chance of dying.
                            possible_death = random.randint(1, 2)
                            if possible_death == 1: # you died
                                death_pic = random.randint(0, 4)
                                death = death_text[death_pic]
                                ascii_pictures(death_pic) # prints a picture that corresponds to the death text
                                typewriter(death)
                                is_alive = False
                                break
                            else:  # you survived
                                distance = geodesic(get_location(get_airport_code(current_country)), get_location(destination_airport)).kilometers
                                budget -= int(distance / 10)  # calculates Co2
                                current_country = destination # your previous destination becomes your current country
                                check_continents(get_continent(current_country))
                                typewriter(neardeath_text[random.randint(0, 5)])
                                typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                        if number == 2:  # You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10)  # calculates Co2
                            current_country = destination
                            check_continents(get_continent(current_country))
                            typewriter("Your plane had to take an unexpected detour, doubling the cost of Co2.")
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10) * 2:.1f} Co2")

                        if number == 3:  # you end up at a random destination anywhere in the world.

                            random_country = get_country()  # the new random country
                            new_destination = get_airport_code(random_country)  # the location of the airport in a new random country
                            distance = geodesic(get_location(current_airport), get_location(new_destination)).kilometers
                            current_country = random_country  # updates the current country so the text will be correct
                            budget -= int(distance / 10)  # calculates Co2
                            check_continents(get_continent(current_country))
                            typewriter(randomcountry_text[random.randint(0, 3)])
                            typewriter(f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2")

                        if number == 4:  # Your plane had to return to the previous airport. Full amount of Co2 wasted

                            recent_airport += current_airport  # changes the value of the current airport to the recent
                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers #calculates the distance for the planned flight
                            budget -= int(distance / 10)
                            typewriter("Your plane had to return to the previous airport. Full amount of Co2 had to be paid.")
                            typewriter(f"\nYour flight was {0} kilometers and you had to pay {(distance / 10):.1f} Co2")

                        if number == 5:  # You get a 50% Co2 refund for that particular flight.

                            distance = geodesic(get_location(get_airport_code(current_country)), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10) / 2
                            current_country = destination
                            check_continents(get_continent(current_country))
                            typewriter("You got a good discount and only had to pay 50% of the original Co2 cost.")
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10) / 2:.1f} Co2")

                        if number == 6:   # You get a full Co2 refund for that particular flight.
                            distance = geodesic(get_location(get_airport_code(current_country)), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10) - int(distance / 10)
                            current_country = destination
                            check_continents(get_continent(current_country))
                            typewriter(fullrefund_text[random.randint(0, 4)])
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {0} Co2")

                else:

                    current_airport = get_airport_code(current_country)
                    current_airport_name = get_airport_name(current_airport)
                    typewriter(f"\nYou are currently in {current_country} at {current_airport_name} in {get_continent(current_country)}. Your current Co2 budget is {budget}. You have traveled to {len(continents)}/7 continents.")

                    destination = input("\nEnter the country you wish to travel to: ")
                    destination_airport = get_airport_code(destination)

                    while destination_airport is None:

                        destination = input("\nEnter the country you wish to travel to: ")
                        destination_airport = get_airport_code(destination)

                    else:
                        number = random.randint(1, 6)
                        if number == 1:  # You have a 50% chance of dying.
                            possible_death = random.randint(1, 2)
                            if possible_death == 1:
                                deathpict = random.randint(0, 4)
                                death = death_text[deathpict]
                                typewriter(death)
                                ascii_pictures(deathpict)
                                is_alive = False
                                break
                            else:
                                distance = geodesic(get_location(current_airport),
                                                    get_location(destination_airport)).kilometers
                                budget -= int(distance / 10)  # calculates Co2
                                current_country = destination  # updates the current location
                                check_continents(get_continent(current_country))
                                typewriter(neardeath_text[random.randint(0, 5)])
                                typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2\n")

                        if number == 2:  #You had to take an unexpected detour. Double the amount of Co2 consumed.\n\

                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10) * 2  # calculates Co2
                            current_country = destination  # updates the current location
                            check_continents(get_continent(current_country))
                            typewriter("Your plane had to take an unexpected detour, doubling the cost of Co2.")
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10) * 2:.1f} Co2\n")

                        if number == 3:  #you end up at a random destination anywhere in the world.\n\

                            random_country = get_country()  # the new random country
                            new_destination = get_airport_code(random_country)  # the location of the airport in a new random country
                            distance = geodesic(get_location(current_airport), get_location(new_destination)).kilometers
                            current_country = random_country #updates the current country
                            budget -= int(distance / 10)  # calculates Co2
                            check_continents(get_continent(current_country))
                            typewriter(randomcountry_text[random.randint(0, 3)])
                            typewriter(f"\nYou ended up in {current_country} in {get_continent(current_country)}. Your flight was {distance:.1f} kilometers and you had to pay {(distance / 10):.1f} Co2\n")

                        if number == 4:  # Your plane had to return to the previous airport. Full amount of Co2 wasted

                            recent_airport += current_airport # changes the value of the current airport to the recent
                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10)
                            typewriter("Your plane had to return to the previous airport. Full amount of Co2 had to be paid.")
                            typewriter(f"\nYour flight was {0} kilometers and you had to pay {(distance / 10):.1f} Co2\n")

                        if number == 5:  # You get a 50% Co2 refund for that particular flight.

                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10) / 2
                            current_country = destination
                            check_continents(get_continent(current_country))
                            typewriter("You got a good discount and only had to pay 50% of the original Co2 cost.")
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 10) / 2:.1f} Co2\n")

                        if number == 6:  # You get a full Co2 refund for that particular flight.
                            distance = geodesic(get_location(current_airport), get_location(destination_airport)).kilometers
                            budget -= int(distance / 10) - int(distance / 10)
                            current_country = destination
                            check_continents(get_continent(current_country))
                            typewriter(fullrefund_text[random.randint(0, 4)])
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {0} Co2\n")
        rounds += 1
        if rounds == 2:
            score1 = ((len(continents)) * 100)
            typewriter("\n\n✧✧✧✧✧✧✧✧✧✧✧✧✧✧Get ready for second round!✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧\n\n")

        if rounds == 3:
            score2 = ((len(continents)) * 100)
            typewriter("\n\n✧✧✧✧✧✧✧✧✧✧✧✧Get ready for third and last round!✧✧✧✧✧✧✧✧✧✧✧✧\n\n")
    else:
        ascii_text(4)
        final_score = score1 + score2 + score  # total 2100
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
            os.system('cls')
            logo()
            return
        else:
            typewriter("Invalid input!")
