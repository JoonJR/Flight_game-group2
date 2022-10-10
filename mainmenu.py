from continent_game_function import *
from Functions import *
from EU_game_function import *
import os

logo()
typewriter("\nWelcome to Sus-PLANE-ability\n")
while True:
    main_menu = input("1. Continent game \n2. Europe game \n3. Credits \n4. Quit\n>>> ")
    if main_menu == "1":
        typewriter("Flying to the Continent Game. Please fasten your seatbelt...")
        time.sleep(1)
        os.system('cls') # opens game in a new page (clears everything before that) but doesnt work in pycharm only if its open as a .exe file
        flight_game_continent()
    elif main_menu == "2":
        os.system('cls')
        ascii_text(7)
        while True:
            eu_menu = input("\nEU game\n1. Start \n2. Country cheat sheet. \n3. Back \n>>>")
            if eu_menu == "1":
                typewriter("Flying to the EU Game. Please fasten your seatbelt...")
                time.sleep(1)
                os.system('cls')
                eugame()
            elif eu_menu == "2":
                cheat_sheet()
            elif eu_menu == "3":
                os.system('cls')
                logo()
                typewriter("\nWelcome to Sus-PLANE-ability\n")
                break
            else:
                print("Enter a valid input")
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
    elif main_menu == "4":
        typewriter("Exiting the game.")
        time.sleep(1)
        break
    else:
        typewriter('Enter a valid input\n')