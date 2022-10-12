from Games.Continent_game_function import *
from Games.EU_game_function import *
import os

logo()
typewriter("\nWelcome to SUS(PLANE)ABILITY\n")
while True:
    main_menu = input("1. Continent game \n2. Europe game \n3. Credits \n4. Quit\n>>> ")
    if main_menu == "1":
        os.system('cls')
        while True:
            ascii_text(3)
            continent_menu = input("\n1. Start \n2. Country cheat sheet \n3. Back \n>>>")
            if continent_menu == "1":
                typewriter("Flying to the Continent Game. Please fasten your seatbelt...")
                time.sleep(1)  # suspends execution for 1 second
                os.system('cls')  # opens game on a new page (clears everything before that)
                flight_game_continent()  # opens the continent game
            elif continent_menu == "2":
                cheat_cheet_continent()
                back = input("\n\n\nPress ENTER to go back")  # returns to the eu game menu
                os.system('cls')
            elif continent_menu == "3":  # returns to the main menu
                os.system('cls')
                logo()
                typewriter("\nWelcome to SUS(PLANE)ABILITY\n")
                break
            else:
                print("Enter a valid input")
    elif main_menu == "2":  # EU game menu
        os.system('cls')
        while True:
            ascii_text(7)
            eu_menu = input("\n1. Start \n2. Country cheat sheet \n3. Back \n>>>")
            if eu_menu == "1":
                typewriter("Flying to the EU Game. Please fasten your seatbelt...")
                time.sleep(1)
                os.system('cls')
                eugame()  # opens EU game on a new page
            elif eu_menu == "2":
                cheat_sheet()  # opens countries' list on a new page
                back = input("\n\n\nPress ENTER to go back")  # returns to the eu game menu
                os.system('cls')
            elif eu_menu == "3":  # returns to the main menu
                os.system('cls')
                logo()
                typewriter("\nWelcome to SUS(PLANE)ABILITY\n")
                break
            else:
                print("Enter a valid input")
    elif main_menu == "3":
        os.system('cls')
        credits_text()  # opens credits on a new page
        while True:
            choice = input("Would you like to go back to the main menu? (Y/N):")  # option to exit
            if choice == "Y" or choice == "y":
                os.system('cls')
                logo()
                typewriter("\nWelcome to SUS(PLANE)ABILITY\n")
                break
            elif choice == "N" or choice == "n":
                easter_egg()
                input("Press ENTER to continue")  # exits to the main menu
                os.system('cls')
                logo()
                typewriter("\nWelcome to SUS(PLANE)ABILITY\n")
                break
            else:
                print("Enter a valid input")
    elif main_menu == "4":
        typewriter("Exiting the game.")
        time.sleep(1)
        break
    else:
        typewriter('Enter a valid input\n')
