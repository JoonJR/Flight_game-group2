import mysql.connector
import time
import sys
connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )


def typewriter(rules):
    for char in rules:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(1)


def cheat_sheet():
    country_list = [['Andorra  ', 'Albania  ', 'Austria  ', 'Belgium  ', 'Slovakia ', 'Bulgaria ', 'Belarus  ',
                    'Serbia   ', 'Sweden   ', 'Germany  ', 'Denmark  ', 'Estonia  ', 'Spain    ', 'Finland  ',
                    'Romania  '], ['France     ', 'Ukraine    ', 'Guernsey   ', 'Gibraltar  ', 'Greece     ',
                    'Croatia    ', 'Hungary    ', 'Ireland    ', 'Monaco     ', 'Iceland    ', 'Italy      ',
                    'Jersey     ', 'Russia     ', 'Lithuania  ', 'Luxembourg '], ['Latvia      ', 'Isle of Man ',
                    'Moldova     ', 'Montenegro  ', 'Kosovo      ', 'Malta  ', 'Netherlands  ', 'Norway  ', 'Poland  ',
                    'Portugal  ', 'Faroe Islands  ', 'Switzerland  ', 'Liechtenstein  ', 'Czech Republic  ',
                    'Slovenia  '], ['Bosnia and Herzegovina  ', 'San Marino  ', 'United Kingdom  ', 'Vatican City  ',
                    'North Macedonia  ', '', '', '', '', '', '', '', '', '', '']]
    print("\nCHEAT SHEET, MAKE SURE TEACHER DOESN'T SEE YOU!!!")
    for x, y, z, q in zip(*country_list):
        print(x, y, z, q)


def credits_text():
    credits = "Designed and developed by Group 2\nKarin Domagalska\nJoona Rantala\nCan Erman\nNadim Ahmed"
    typewriter(credits)
    print("\n")


def easter_egg():
    while True:
        egg = input("1. To exit.\nyes or no: ")
        if egg == "yes":
            egg = input("1. To exit.\nyes or no: ")
            if egg == "yes":
                egg = input("1. To exit.\nyes or no: ")
                if egg == "yes":
                    egg = input("1. To exit.\nyes or no: ")
                    if egg == "yes":
                        print(f"\n\n\n\U0001F49A\U0001F49APlease grade us 5/5\U0001F49A\U0001F49A\n\n\n")
                        break
                    elif egg == '1':
                        print("\n")
                        break
                    elif egg == "no":
                        print("Wrong answer.")
                elif egg == '1':
                    print("\n")
                    break
                elif egg == "no":
                    print("Wrong answer.")
            elif egg == '1':
                print("\n")
                break
            elif egg == "no":
                print("Wrong answer.")
        elif egg == '1':
            print("\n")
            break
        elif egg == "no":
            print("Wrong answer.")


