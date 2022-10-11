import mysql.connector
import time
import sys
from Functions.ascii import *

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
                     'Serbia   ', 'Sweden   ', 'Germany  ', 'Denmark  ', 'Estonia  ', 'Spain    '],
                    ['France     ', 'Ukraine    ', 'Guernsey   ', 'Gibraltar  ', 'Greece     ', 'Croatia    ',
                     'Hungary    ', 'Ireland    ', 'Monaco     ', 'Iceland    ', 'Italy      ', 'Jersey     ',
                     'Russia     '], ['Latvia      ', 'Isle of Man ', 'Moldova     ', 'Montenegro  ', 'Kosovo      ',
                     'Malta       ', 'Netherlands ', 'Norway      ', 'Poland      ', 'Portugal    ',
                     'Finland     ', 'Switzerland  ', 'Liechtenstein  '], ['Bosnia and Herzegovina  ', 'San Marino  ',
                     'United Kingdom  ', 'Vatican City  ', 'North Macedonia  ', 'Romania  ', 'Luxembourg ',
                     'Czech Republic  ', 'Lithuania  ', 'Slovenia  ', 'Faroe Islands  ', '', '', '', '']]
    print("\nCHEAT SHEET, MAKE SURE TEACHER DOESN'T SEE YOU!!!")
    for x, y, z, q in zip(*country_list):
        print(x, y, z, q)


def cheat_cheet_continent():
    country_list = [['Europe     ', '', 'Finland   ', 'Poland  ', 'Italy     '], ['Asia     ', '', 'India        ',
                    'Bangladesh   ', 'Turkey      '], ['North-America     ', '', 'Canada           ',
                    'Costa Rica         ', 'Guatemala         '], ['South-America     ', '', 'Argentina       ',
                    'Venezuela         ', 'Colombia         '], ['Oceania      ', '', 'Australia     ', 'Nauru      ',
                    'Tuvalu       '], ['Africa      ', '', 'Ghana      ', 'Ethiopia    ', 'Egypt      '], ['Antarctica',
                    '', ' Antarctica', 'South Georgia and the South Sandwich Isl', 'French Southern Territories']]
    print("\nCHEAT SHEET, MAKE SURE TEACHER DOESN'T SEE YOU!!!")
    for x, y, z, q, t, r, p in zip(*country_list):
        print(x, y, z, q, t, r, p)



def credits_text():
    ascii_text(6)
    credits = "Designed and developed by Group 2\nKarin Domagalska\nJoona Rantala\nCan Erman\nNadim Ahmed"
    typewriter(credits)
    print("\n")
    time.sleep(1)
    print("\n")


def easter_egg():
    print("There's nothing to do here.")
    while True:
        egg = input("Do you want to exit\nYes or No: ")
        if egg == "yes" or egg == "Yes":
            egg = input("Wait! Are you sure?\nYes or No:: ")
            if egg == "yes" or egg == "Yes":
                egg = input("Think again!\nYes or No:: ")
                if egg == "yes" or egg == "Yes":
                    egg = input("Are you sure sure?\nYes or No: ")
                    if egg == "yes" or egg == "Yes":
                        print(f"\n\n\n\U0001F49A\U0001F49APlease grade us 5/5\U0001F49A\U0001F49A\n\n\n")
                        time.sleep(1)
                        break
                    elif egg == "no" or egg == "No":
                        print("Wrrrrrong answerrrrrr.")
                elif egg == "no" or egg == "No":
                    print("Ooops! Wrong answer")
            elif egg == "no" or egg == "No":
                print("Wrong answer hehe.")
        elif egg == "no" or egg == "No":
            print("Hmmm.. think again.")


def logo():
    ascii_pictures(6)
    ascii_text(8)
    ascii_pictures(6)
