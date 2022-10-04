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
            time.sleep(0.5)

def cheat_sheet():
    countrylist = [['Andorra  ', 'Albania  ', 'Austria  ', 'Belgium  ', 'Slovakia ', 'Bulgaria ', 'Belarus  ',
                    'Serbia   ', 'Sweden   ', 'Germany  ', 'Denmark  ', 'Estonia  ', 'Spain    ', 'Finland  ',
                    'Romania  '], ['France     ', 'Ukraine    ', 'Guernsey   ', 'Gibraltar  ', 'Greece     ', 'Croatia    ',
                    'Hungary    ', 'Ireland    ', 'Monaco     ', 'Iceland    ', 'Italy      ', 'Jersey     ', 'Russia     ', 'Lithuania  ',
                    'Luxembourg '], ['Latvia      ', 'Isle of Man ', 'Moldova     ', 'Montenegro  ', 'Kosovo      ', 'Malta  ',
                    'Netherlands  ', 'Norway  ', 'Poland  ', 'Portugal  ', 'Faroe Islands  ', 'Switzerland  ', 'Liechtenstein  ', 'Czech Republic  ',
                    'Slovenia  '],['Bosnia and Herzegovina  ', 'San Marino  ', 'United Kingdom  ', 'Vatican City  ', 'North Macedonia  ', '', '', '', '', '', '', '', '', '', '']]
    print("CHEAT SHEET, MAKE SURE TEACHER DOESN'T SEE YOU!!!")
    for x, y, z, q in zip(*countrylist):
        print(x, y, z, q)

