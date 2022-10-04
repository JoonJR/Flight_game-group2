from continent_game_function import *
from Functions import *

print("Welcome to Green Wash Airlines")
main_menu = int(input("1. Continent game \n2. Europe game \n3. Quit \n"))
if main_menu == 1:
    flight_game_continent()
elif main_menu == 2:
    eu_menu = int(input("\nEU game\n1. Start \n2. Country cheat sheet. \n3. Quit \n"))
    if eu_menu == 1:
        print("function here")
    elif eu_menu == 2:
        print(cheat_sheet())
    elif eu_menu == 3:
        typewriter("lol")
elif main_menu == 3:
    typewriter("Exiting the game.")


