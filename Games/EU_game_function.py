from geopy.distance import geodesic
import random
import os
from Functions.EU_game_functions import *
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )


def eugame():
    ascii_text(7)
    player_name = input("\nEnter your name: ")

    rules = f"Hello " + player_name + "! You have been given the mission of travelling to all 50 countries in continent Europe! You will be" \
    " given a fancy helicopter with a pilot and a Co2 budget of 10000 which you cannot exceed.\nFor every 1000km you use 300 Co2. Your starting location will be random. From that point you can choose to fly to any country, however the heliports will be random.\n" \
    "Every time before you fly a dice of destiny will be rolled. The outcomes of the rolls are as follows:\n\
    6. You get a full Co2 refund for that particular flight.\n\
    5. You get a 50% Co2 refund for that particular flight.\n\
    4. Your helicopter had to return to the previous heliport. Full amount of Co2 wasted for that trip.\n\
    3. Your helicopter flies through teleportal and you end up at a random destination anywhere in the world.\n\
    2. You had to take an unexpected detour. Double the amount of Co2 consumed.\n\
    1. Worst possible scenario. You have a 50% chance of dying.\nGood luck!\nps if there are errors its your fault :p\n" \
                                      "(Type X if you want to exit the game)"

    #typewriter(rules)
    is_alive = True
    budget = 10000
    countries = []
    current_country = get_country()
    countries.append(current_country)
    current_heliport = None
    recent_heliport = ""

    while is_alive:

        if budget <= 0:
            print("\nYou ran out of Co2 before reaching all the continents. Game Over!")
            break

        while budget > 0 and is_alive:

            if len(countries) == 50:
                ascii_pictures(9)
                typewriter("\nYou won! You made it to all 50 countries without exceeding your budget!\n\n")
                ascii_pictures(8)
                is_alive = False  # you won! the game is finished
                break
            recent_country = current_country


            if recent_heliport != "":
                print(f"\nYou are currently in {recent_country} at {get_heliport_name(recent_heliport)}. Your current Co2 budget is {budget}. "
                      f"You have travelled to {len(countries)}/50 countries.")
                recent_heliport = ""
                destination = input("Enter the country you wish to travel to: ")
                if destination == "Russia" or destination == "russia":
                    while destination == "Russia" or destination == "russia":
                        print("It's currently too dangerous to travel to Russia. Choose another destination")
                        destination = input("Enter the country you wish to travel to: ")
                destination_heliport = get_heliport_code(destination)

                if destination == "X" or destination == "x":  # to exit the game
                    os.system("cls")
                    return

                while destination_heliport is None:
                    destination = input("Enter the country you wish to travel to: ")
                    while destination == "Russia" or destination == "russia":
                        print("It's currently too dangerous to travel to Russia. Choose another destination")
                        destination = input("Enter the country you wish to travel to: ")
                    destination_heliport = get_heliport_code(destination)

                    if destination == "X" or destination == "x":  # to exit the game
                        os.system("cls")
                        return

                else:

                    number = random.randint(1, 6)
                    if number == 1:
                        possible_death = random.randint(1, 2)
                        if possible_death == 1:
                            death = death_text[random.randint(0, 3)]
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
                            typewriter(neardeath_text[random.randint(0, 3)])
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 2:

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) * 2:.1f} Co2\n")

                    if number == 3:

                        current_country = get_country()
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)  # calculates Co2
                        typewriter(randomcountry_text[random.randint(0, 2)])
                        typewriter(f"\n You ended up in {current_country}, {current_heliport}.\nYour flight was {distance:.1f}"
                                   f"kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 4:

                        recent_heliport += current_heliport
                        destination_heliport = get_heliport_code(destination)
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)
                        typewriter("Your helicopter had to return to the previous heliport. Full amount of Co2 had to be paid.")
                        typewriter(f"\nYour flight was {0} kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 5:

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) / 2
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) / 2:.1f} Co2\n")

                    if number == 6:
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) - int(distance / 3.3)
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter(fullrefund_text[random.randint(0, 3)])
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {0} Co2")
            else:

                current_heliport = get_heliport_code(current_country)
                current_heliport_name = get_heliport_name(current_heliport)
                typewriter(f"\nYou are currently in {current_country} at {current_heliport_name}. Your current Co2 budget is {budget}. "
                           f"You have traveled to {len(countries)}/50 countries.")

                destination = input("\nEnter the country you wish to travel to: ")
                if destination == "Russia" or destination == "russia":
                    while destination == "Russia" or destination == "russia":
                        print("It's currently too dangerous to travel to Russia. Choose another destination")
                        destination = input("Enter the country you wish to travel to: ")
                destination_heliport = get_heliport_code(destination)

                if destination == "X" or destination == "x":
                    os.system("cls")
                    return



                while destination_heliport is None:

                    destination = input("Enter the country you wish to travel to: ")
                    if destination == "Russia" or destination == "russia":
                        while destination == "Russia" or destination == "russia":
                            print("It's currently too dangerous to travel to Russia. Choose another destination")
                            destination = input("Enter the country you wish to travel to: ")
                    destination_heliport = get_heliport_code(destination)

                    if destination == "X" or destination == "x":
                        os.system("cls")
                        return

                else:
                    number = random.randint(1, 6)
                    number = 1
                    if number == 1:  # You have a 50% chance of dying.
                        possible_death = random.randint(1, 2)
                        if possible_death == 1:
                            death = death_text[random.randint(0, 3)]
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
                            typewriter(neardeath_text[random.randint(0, 3)])
                            typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 2:  # You had to take an unexpected detour. Double the amount of Co2 consumed.

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) * 2  # calculates Co2
                        current_country = destination  # updates the current location
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter("Your helicopter had to take an unexpected detour, doubling the cost of Co2.")
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) * 2:.1f} Co2\n")

                    if number == 3:

                        current_country = get_country()
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)  # calculates Co2
                        typewriter(randomcountry_text[random.randint(0, 2)])
                        typewriter(f"You ended up in {current_country}, {current_heliport}. \nYour flight was {distance:.1f}"
                                   f" kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 4:

                        recent_heliport += current_heliport
                        destination_heliport = get_heliport_code(destination)
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3)
                        typewriter("Your helicopter had to return to the previous heliport. Full amount of Co2 had to be paid.")
                        typewriter(f"\nYour flight was {0} kilometers and you had to pay {(distance / 3.3):.1f} Co2\n")

                    if number == 5:  # 5. You get a 50% Co2 refund for that particular flight.\n\

                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) / 2
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter("You got a good discount and only had to pay 50% of the original Co2 cost.")
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {(distance / 3.3) / 2:.1f} Co2\n")

                    if number == 6:  # 6. You get a full Co2 refund for that particular flight.\n\
                        distance = geodesic(get_location(get_heliport_code(current_country)),
                                            get_location(destination_heliport)).kilometers
                        budget -= int(distance / 3.3) - int(distance / 3.3)
                        current_country = destination
                        if current_country not in countries:
                            countries.append(current_country)  # appends country to the list
                        typewriter(fullrefund_text[random.randint(0, 3)])
                        typewriter(f"\nYour flight was {distance:.1f} kilometers and you had to pay {0} Co2\n")


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
            os.system('cls')  # opens main menu in a new page (clears everything before that) but doesn't work in pycharm
            logo()
            return
        else:
            typewriter("Invalid input!")

eugame()