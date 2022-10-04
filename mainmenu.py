from continent_game_function import *
from Functions import *

while True:
    print("Welcome to Green Wash Airlines")
    main_menu = int(input("1. Continent game \n2. Europe game \n3. Credits \n4. Something funny. \n5. Quit\n"))
    if main_menu == 1:
        flight_game_continent()
    elif main_menu == 2:
        while True:
            eu_menu = int(input("\nEU game\n1. Start \n2. Country cheat sheet. \n3. Back \n"))
            if eu_menu == 1:
                print("function here")
            elif eu_menu == 2:
                cheat_sheet()
            elif eu_menu == 3:
                break
    elif main_menu == 3:
        credits_text()
    elif main_menu == 4:
        easter_egg()
    elif main_menu == 5:
        typewriter("Exiting the game.")
        break
