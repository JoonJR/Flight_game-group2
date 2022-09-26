import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

nickname=input("Please enter your nickname")
print(f"Hello {nickname}! Your task is to travel as many continents as possible! "
      f"You have 4000 C02. For every 1000 km you use 100 CO2.`\n Your starting point is a random airport in"
      f"a random country. Later you can chose any country, but the airport will be random."
      f"\nBefore you fly, roll the dice. If you roll:"
      f"\n6: no CO2 was used"
      f"\n5: You use 50% of your CO2"
      f"\n4: The plane had to come back and you wasted your CO2."
      f"\n3: You end up in a random destination."
      f"\n2: You use double the amount of your CO2"
      f"\n1: Your plane crashes. The round is over."
      f"\nYou have 3 rounds.")
con= input("Press y/n to continue:")
def GetCountry():
    sql = "SELECT country.name FROM country ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row[0])
        return row[0]



def GetAirport(country):
    sql = "SELECT airport.name FROM airport, country WHERE airport.iso_country = country.iso_country and country.name ='" + country + "' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row[0])
        return


country = GetCountry()
GetAirport(country)
country = input("Enter the country you want to travel: ")

GetAirport(country)

import geopy
from geopy.distance import geodesic
def get_location (area_code):
    location = []
    sql = "SELECT longitude_deg, latitude_deg  FROM airport"
    sql += " WHERE ident='" + area_code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(row[1])
            location.append(row[0])
        return location


CO2_km = 0.1
count = 0
co2 = 0
while count <3:
    area_code1 = input("Enter area code of the first airport: ")
    area_code2 = input("Enter area code of the second airport: ")
    print(f"The distance between the two airports is {geodesic(get_location(area_code1), get_location(area_code2)).kilometers:.6} km"
          f"\n and CO2 consumed {geodesic(get_location(area_code1), get_location(area_code2))*CO2_km} ")
    count += 1
