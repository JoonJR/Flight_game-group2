import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

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


area_code1 = input("Enter area code of the first airport: ")
area_code2 = input("Enter area code of the first airport: ")
print(f"The distance between the two airports is {geodesic(get_location(area_code1), get_location(area_code2)).kilometers:.6} km")