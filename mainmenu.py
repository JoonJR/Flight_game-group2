from continent_game_function import *
from Functions import *
import os
# from ascii import *

logo()

typewriter("\nWelcome to Sus-PLANE-ability\n")
#main_menu = input("1. Continent game \n2. Europe game \n3. Credits \n4. Something funny. \n5. Quit\n>>> ")
while True:
    main_menu = input("1. Continent game \n2. Europe game \n3. Credits \n4. Quit\n>>> ")
    if main_menu == "1":
        typewriter("Flying to the Continent Game. Please fasten your seatbelt...\n\n\n")
        os.system('cls') # opens game in a new page (clears everything before that) but doesnt work in pycharm only if its open as a .exe file
        flight_game_continent()
    elif main_menu == "2":
        while True:
            eu_menu = int(input("\nEU game\n1. Start \n2. Country cheat sheet. \n3. Back \n>>>"))
            if eu_menu == "1":
                print("function here")
            elif eu_menu == "2":
                cheat_sheet()
            elif eu_menu == "3":
                continue
    elif main_menu == "3":
        os.system('cls')
        credits_text()
        while True:
            choice = input("Would you like to go back to the main menu? (Y/N):")
            if choice == "Y" or choice == "y":
                os.system('cls')
                logo()
                typewriter("\nWelcome to Sus-PLANE-ability\n")
                break
            elif choice == "N" or choice == "n":
                easter_egg()
                input("Press ENTER to continue")
                os.system('cls')
                logo()
                typewriter("\nWelcome to Sus-PLANE-ability\n")
                break
            else:
                print("Enter a valid input")
    # elif main_menu == "4":
    #     easter_egg()
    elif main_menu == "4":
        typewriter("Exiting the game.")
        break
    else:
        typewriter('Enter a valid input\n')