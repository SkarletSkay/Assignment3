import random as rd
import Tables

car_types = ["Abarth", " AC", "Acura", "Alfa Romeo", "Almac", "Alternative Cars", "Amuza", "Anteros", " Buick", " BYD", " Mazzanti", " Ferrari"]
plug_types = ["PT173", "PT1412", "PT229"]
stations = 5
# stations_addresses = ["Veselay, 5", "Malaliskay, 66", "Romanovska, 9", "Tsuinchekovskay, 61"]
colours = ["Red", "Green", "Black", "White", "Yellow", "Blue", "Brown", "Silver"]
plate_numbers = ["AN353", "AN642"]
part_types = ["Wheel Q564", "Washer L96", "Door Standard K312", "Door Lux KL311", "Engine LQP55A89b"]
workshops_location = ["Meyora, 91", "Priroda, 8", "Red Square, 1", "Universitetskay, 108"]
provider_name = ["Tinkoff Car Inc", "Yandex Taxi Details", "Musk Tesla Inc", "Google Repair"]
streets = ["Veselaya", "Belorussian", "Tykaya", "Gogola", "Malaya", "Sinya", "Karla Marksa", "Gorkogo"]
city = ["Misnk"]
name = ["Bob", "Anna"]


def create_address():
    a = rd.randint(0, len(streets)-1)
    b = rd.randint(1,100)
    address = streets[a]+", "+str(b)
    return address

def create_phone():
    number = "8"
    for i in range(10):
        a = rd.randint(0,9)
        number+=str(a)

    print(number)
    return number

def populate_car_types(conn):
    for i in range(len(car_types)):
        Tables.insert( conn, Tables.CarTypesTable.TABLE_NAME, "NULL, '" + car_types[i] + "'")
def populate_part_types(conn):
    for i in range(len(part_types)):
        Tables.insert( conn, Tables.PartTypesTable.TABLE_NAME, "NULL, '" + part_types[i] + "'")
def populate_plug_types(conn):
    for i in range(len(plug_types)):
        Tables.insert(conn, Tables.PlugTypesTable.TABLE_NAME, "NULL, '" + plug_types[i] + "'")
def populate_charging_stations(conn, amount):
    for i in range(amount):
        address = create_address()
        Tables.insert(conn, Tables.ChargingStationsTable.TABLE_NAME, "NULL, '" + address + "'")


conn = Tables.create_connection()
populate_car_types(conn)
populate_part_types(conn)
populate_plug_types(conn)
populate_charging_stations(conn, stations)