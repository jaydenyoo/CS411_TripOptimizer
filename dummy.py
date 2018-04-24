import json
from dbsql import *


def createUserDummy(cur, conn):
    try:
        createTable_User(cur)
    except Exception:
        dropTable_User(cur)
        createTable_User(cur)

    print("User Table Created")

    users = json.load(open('users.json'))

    for entry in users:
        addUser(cur, entry["email"], entry["name"],
                entry["age"], entry["birthDate"], entry["address"])

    print("User Dummy Created\n")


def createPlaceDummy(cur, conn):
    try:
        createTable_Place(cur)
    except Exception:
        dropTable_Place(cur)
        createTable_Place(cur)

    print("Place Table Created")

    pid = 0

    places = json.load(open("merged_data.json"))

    for item in places:
        hours = item["hours"].upper().split('-')
        addPlace(cur, item["title"],
                 item["addr"], item['city'].split(',')[0], item['category'], hours[0].strip(), hours[-1].strip(), item['lat'], item['lon'], float(item["yelp_rating"]), float(item["trip_rating"]), pid)
        pid += 1


    print("Place Dummy Created\n")


def createTripDummy(cur, conn):
    try:
        createTable_Trip(cur)
    except Exception:
        dropTable_Trip(cur)
        createTable_Trip(cur)

    print("Trip Table Created")


def createContainDummy(cur, conn):
    try:
        createTable_Contain(cur)
    except Exception:
        dropTable_Contain(cur)
        createTable_Contain(cur)

    print("Contain Table Created")
