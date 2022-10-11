from Functions.Functions import *


def get_country():  # returns a random country from the database
    sql = "SELECT country.name FROM country, airport WHERE airport.iso_country = country.iso_country and airport.type like '%airport' ORDER BY RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_airport_code(country):  # returns a random airport's ICAO of a country
    sql = "SELECT airport.ident FROM airport, country  WHERE country.iso_country = airport.iso_country and" \
          " country.name ='" + country + "' AND airport.type = 'medium_airport' OR country.iso_country = " \
          "airport.iso_country and country.name ='" + country + "' and airport.type = 'large_airport' OR" \
          " country.iso_country = airport.iso_country and country.name ='" + country + "' and airport.type" \
          " = 'small_airport' order by (case when airport.type = 'medium_airport' then 1 ELSE 2 END), RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:  # if the country doesn't exist in the database it will print an error message
        print('\nThis country does not exist, try again.')
        return None

    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_airport_name(code):  # returns an airport name from the ICAO
    sql = "SELECT airport.name FROM airport WHERE airport.ident ='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_continent(country):  # returns a continent
    sql = "SELECT country.continent FROM country WHERE country.name ='" + country + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_location(code):  # returns long/lat of an airport
    location = []
    sql = "SELECT longitude_deg, latitude_deg FROM airport WHERE airport.ident ='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            location.append(int(row[1]))
            location.append(int(row[0]))
        return location


def typewriter(rules):  # text animation
    for char in rules:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.0005)


death_text = [
    "Your plane got struck by lightning and crashed on a remote island, you survived the crash and promptly died of dehydration.",
    "The pilot had one too many the night before and fell asleep at the wheel, nosediving the plane to your inevitable doom.",
    "You encountered some unexpected turbulence causing the pilot to lose complete control of the plane which hits the ground and explodes, but not before doing a cool flip.!",
    "You poorly chose the meal with fish. You made it to your destination before dying of food poisoning in the airport bathroom.!",
    "Someone's beloved pet cobra somehow escaped from its cage and found its way up your pants. Unfortunately you only realised this after it bit you. You took your last breath 15 minutes later."]

neardeath_text = [
    "Some strong turbulence managed to open a loose baggage compartment. Someones weights fell out and almost hit you on the head.\nThankfully they hit the person next to you.",
    "You were offered a meal choice of either fish or meat, you were about to choose fish before remembering the golden rule. That was a close one.",
    "You somehow managed to flush the toilet without realising a part of your clothing was in there.\nYou got pulled back into the toilet but thankfully you had your second breakfast that morning.",
    "Your plane was about to take off and then you quickly remembered you didnt change your phones mode to flight mode.\nYou frantically make the change before takeoff saving the lives of many. A true hero.",
    "A bump in the sky during mealtime caused a swedish meatball to go down the wrong pipe. Thankfully a vet was nearby to help.",
    "The pilot didn't get much sleep the night before because his newborn was crying and screaming.\nThankfully the crying and screaming of you and the other passengers also woke him up."]

randomcountry_text = ["The pilot forgot to Never Eat Soggy Waffles and ended up going in the opposite direction.",
                      "Your pilot partied a bit too much the night before and didn't realise a change of schedule.",
                      "Your plane got hijacked by honeymooners who could not afford the flights for their dream trip",
                      "You accidentally got onto the wrong plane without anyone noticing"]

fullrefund_text = ["You found an old coupon for a free flight on the floor of a public toilet. All expenses paid.",
                   "Some rich guy ahead of you was feeling generous and paid for your flight. No Co2 spent.",
                   "You forgot to buy the ticket and managed to sneak on the plane without getting caught. You even bumped yourself up to first class. No Co2 spent.",
                   "You spoke to the pilot on your way onto the plane and it turns out hes your sisters cousins uncles brother. He let you on for free. No Co2 spent.",
                   "You spoke to the pilot on your way onto the plane and it turns out hes your uncles sisters aunts nephew. He let you on for free. No Co2 spent."]
