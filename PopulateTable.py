import random as rd
import string
import Tables
letters = string.ascii_uppercase
car_types = ["Abarth", " AC", "Acura", "Alfa Romeo", "Almac", "Alternative Cars", "Amuza", "Anteros", " Buick", " BYD", " Mazzanti", " Ferrari"]
plug_types = ["PT173", "PT1412", "PT229"]
part_types = ["Wheel Q564", "Washer L96", "Door Standard K312", "Door Lux KL311", "Engine LQP55A89b"]
streets = ["Veselaya", "Belorussian", "Tykaya", "Gogola", "Malaya", "Sinya", "Karla Marksa", "Gorkogo"]
colours = ["Red", "Green", "Black", "White", "Yellow", "Blue", "Brown", "Silver"]
provider_name = ["Tinkoff Car Inc", "Yandex Taxi Details", "Musk Tesla Inc", "Google Repair"]
stations = 5
customers = 10
cars = 10
workshops = 3
plate_numbers = ["AN353", "AN642"]

# stations_addresses = ["Veselay, 5", "Malaliskay, 66", "Romanovska, 9", "Tsuinchekovskay, 61"]
# workshops_location = ["Meyora, 91", "Priroda, 8", "Red Square, 1", "Universitetskay, 108"]


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

def populate_workshops(conn, amount):
    for i in range(amount):
        l = create_address()
        open = str(rd.randint(8,11))
        close = str(rd.randint(19,21))
        Tables.insert(conn, Tables.WorkshopsTable.TABLE_NAME,
                      "NULL, '" +l + "', '" + open + "', '" + close+ "'")

def populate_sockets(conn):
    for i in range(1,stations+1):
        for j in range(1, len(plug_types)+1):
            Tables.insert(conn, Tables.SocketsTable.TABLE_NAME,
                          "NULL, '" + str(j) + "', '" + str(i) + "'")

def populate_part_provider(conn):
    for i in range(1,len(part_types)+1):
        for j in range(1, len(provider_name)+1):
            cost = rd.randint(100,1000)
            Tables.insert(conn, Tables.PartProviderTable.TABLE_NAME,
                          "'" + str(i) + "', '" + str(j) + "', '" + str(cost) + "'")
def populate_part_workshop(conn):
    for i in range(1, len(part_types) + 1):
        for j in range(1, workshops + 1):
            cost = rd.randint(1, 20)
            Tables.insert(conn, Tables.PartWorkshopTable.TABLE_NAME,
                          "'" + str(i) + "', '" + str(j) + "', '" + str(cost) + "'")
def populate_provider_workshop(conn):
    for i in range(1, len(provider_name) + 1):
        for j in range(1, workshops + 1):
            Tables.insert(conn, Tables.ProviderWorkshopTable.TABLE_NAME,
                          "'" + str(i) + "', '" + str(j) + "'")



conn = Tables.create_connection()
# populate_car_types(conn)
# populate_part_types(conn)
# populate_plug_types(conn)
# populate_charging_stations(conn, stations)
# populate_customers(conn, customers)
# populate_cars(conn, cars)
# populate_providers(conn)
# populate_workshops(conn,workshops)
# populate_sockets(conn)
# populate_part_provider(conn)
# populate_part_workshop(conn)
# populate_provider_workshop(conn)