from Functions.Functions import *

def get_country():
    sql = "SELECT country.name FROM  country WHERE continent = 'EU' order by RAND() LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_heliport_code(country):
    sql = "SELECT airport.ident FROM airport, country  WHERE country.continent = 'EU' and country.iso_country =" \
          " airport.iso_country and country.name ='" + country + "' AND airport.type = 'heliport' OR" \
          " country.continent = 'EU' and country.iso_country = airport.iso_country and country.name ='" + country + "'"\
          " and airport.type = 'small_airport' OR country.continent = 'EU' and country.iso_country = " \
          "airport.iso_country and country.name ='" + country + "' and airport.type = 'medium_airport'" \
          " order by (case when airport.type = 'heliport' then 1 else 2 END) LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if not result:
        print("\nThis country does not exists or is not located in continent EU, try again.")
        return None

    if cursor.rowcount > 0:
        for row in result:
            return row[0]


def get_heliport_name(code):
    sql = "SELECT airport.name FROM airport WHERE airport.ident ='" + code + "'"
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


def typewriter(rules):
    for char in rules:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char != "\n":
            time.sleep(0.02)
        else:
            time.sleep(0.5)


death_text = ["For some reason the helicopter’s carriage started spinning instead of the rotor which caused everyone on board to die of dizziness.",
              "A loose bolt holding the helicopter together became loose. This caused the rotor to become unattached to the rest of the helicopter,\nwhile the helicopter was falling to the ground the rotor crashed into it.",
              "A stray frisbee thrown by a local kid flew into the helicopter bonking the pilot on the head knocking him out. Without a pilot the helicopter crashed.",
              "The pilot flew into a spaceship masquerading as a cloud causing the helicopter to explode"]


neardeath_text = ["The inexperienced pilot forgot that the controls for the helicopter are inverted. Thankfully he remembered in time.",
"The pilot didn’t get much sleep the night before because his newborn was crying and screaming.\nThankfully your crying and screaming also woke him up.",
"The pilot looked at you with a smirk and told you to watch him do a flip. You pleaded for him not to, but he wasn’t listening.\nHe proceeded to do a flip.....it was awesome.",
"The helicopter stalled midflight causing the engine to stop. The pilot struggled to restart the engine and thankfully got it running in time."]

randomcountry_text = ["The pilot flew into a cloud causing him to fly the wrong direction and get lost.",
                    "The pilot was listening to his favourite song on repeat for the entire flight and forgot where he was supposed to go. ",
                    "The scared pilot flew to avoid a flock of flying geese, the flock was so large he ended up lost."
]

fullrefund_text = ["You found an old coupon for a free flight on the floor of a public toilet. All expenses paid.",
                   "You forgot to buy the ticket and managed to sneak on the helicopter without getting caught.No Co2 spent",
                   "You spoke to the pilot on your way onto the helicopter and it turns out hes your sisters cousins uncles brother. He let you on for free. No Co2 spent.",
                   "You spoke to the pilot on your way onto the helicopter and it turns out hes your uncles sisters aunts nephew. He let you on for free. No Co2 spent."]