import random as rd
import string
import Tables
letters = string.ascii_uppercase
car_types = ["Abarth", " AC", "Acura", "Alfa Romeo", "Almac", "Alternative Cars", "Amuza", "Anteros", " Buick", " BYD", " Mazzanti", " Ferrari"]
plug_types = ["PT173", "PT1412", "PT229"]
stations = 5
customers = 8
cars = 10
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
def populate_customers(conn, amount):
    for i in range(amount):
        Tables.insert(conn,Tables.CustomersTable.TABLE_NAME, "NULL, '"+"Some guy"+"', '"+"NULL"+"', '"+"NULL"+"', '"+"Russia"+"', '"+"Kazan"+"', '"+"420500"+"', '"+create_phone()+"'")

def populate_cars(conn, amount):
    for i in range(amount):
        if i == 0 or i == 1:
            c = 0;
            pt = plate_numbers[i]
        else:
            c = rd.randint(0,len(colours)-1)
            pt = rd.choice(letters) + rd.choice(letters) + str(rd.randint(100, 999))
        plt = str(rd.randint(1,len(plug_types)))
        ct = str(rd.randint(1,len(car_types)))
        Tables.insert(conn, Tables.CarsTable.TABLE_NAME,
                      "NULL, '" + plt + "', '" + ct + "', '" + colours[c] + "', '" + pt +"'")

def populate_providers(conn):
    for i in range(len(provider_name)):
        l = create_address()
        ph = create_phone()
        Tables.insert(conn, Tables.ProvidersTable.TABLE_NAME,
                      "NULL, '" + provider_name[i] + "', '" + l + "', '" + ph +"'")

conn = Tables.create_connection()
# populate_car_types(conn)
# populate_part_types(conn)
# populate_plug_types(conn)
# populate_charging_stations(conn, stations)
#populate_customers(conn, customers)
# populate_cars(conn, cars)
populate_providers(conn)