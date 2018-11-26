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

fav_location = ["Veselay, 5", "Malaliskay, 66", "Romanovska, 9", "Tsuinchekovskay, 61", "Meyora, 91", "Priroda, 8",
                "Red Square, 1", "Universitetskay, 108"]


cities = ["Kazan", "Moscow"]
names = ["Bob", "Anna", "Gretta", "Julia", "Elena", "Eliza"]
surnames = ["Smith", "Black", "Stone", "White", "Brown", "Perry"]


def create_time(start, end):
    hh = rd.randint(start, end-1)
    mm = rd.randint(0, 59)
    ss = rd.randint(0, 59)
    result = ""
    for item in (hh, mm, ss):
        if item > 9:
            result += str(item)+":"
        else:
            result += "0"+str(item)+":"
    return result[:len(result)-1]


def create_address():
    a = rd.randint(0, len(streets)-1)
    b = rd.randint(1, 150)
    address = streets[a] + ", " + str(b)
    return address


def create_phone():
    number = "8"
    for i in range(10):
        a = rd.randint(0, 9)
        number += str(a)
    return number


def create_name():
    a = rd.randint(0, len(names) - 1)
    b = rd.randint(0, len(surnames) - 1)
    return names[a] + " " + surnames[b]


def create_username(name):
    return name[0] + name[1] + name[2] + str(rd.randint(1, 256))


def populate_car_types(conn):
    for i in range(len(car_types)):
        Tables.CarTypesTable.add_new_car_type(conn, car_types[i])


def populate_part_types(conn):
    for i in range(len(part_types)):
        Tables.PartTypesTable.add_new_part_type(conn, part_types[i])


def populate_plug_types(conn):
    for i in range(len(plug_types)):
        Tables.PlugTypesTable.add_new_plug_type(conn, plug_types[i])


def populate_charging_stations(conn, amount):
    for i in range(amount):
        address = create_address()
        Tables.ChargingStationsTable.add_new_station(conn, address)


def populate_customers(conn, amount):
    for i in range(amount):
        name = create_name()
        Tables.CustomersTable.add_new_customer(conn, name, create_username(name),  "@email.com",
                                               "Russia", cities[rd.randint(0, len(cities)-1)],
                                               rd.randint(400000, 499999), create_phone())


def populate_cars(conn, amount):
    for i in range(amount):

        colour = colours[rd.randint(0, len(colours)-1)]
        num = rd.choice(letters) + rd.choice(letters) + str(rd.randint(100, 999))
        plug = rd.randint(1, len(plug_types))
        car_type = rd.randint(1, len(car_types))
        Tables.CarsTable.add_new_car(conn, plug, car_type, colour, num)

    for i in range(2):
        colour = colours[0]
        num = "AN" + str(rd.randint(100, 999))
        plug = rd.randint(1, len(plug_types))
        car_type = rd.randint(1, len(car_types))
        Tables.CarsTable.add_new_car(conn, plug, car_type, colour, num)


def populate_providers(conn):
    for i in range(len(provider_name)):
        Tables.ProvidersTable.add_new_provider(conn, provider_name[i], create_address(), create_phone())


def populate_workshops(conn, amount):
    for i in range(amount):
        Tables.WorkshopsTable.add_new_workshop(conn, create_address(), rd.randint(8, 11), rd.randint(19, 23))


def populate_sockets(conn):
    for i in range(1, stations+1):
        for j in range(1, len(plug_types)+1):
            Tables.SocketsTable.add_new_socket(conn, j, i)


def populate_part_provider(conn):
    for i in range(1, len(part_types)+1):
        for j in range(1, len(provider_name)+1):
            cost = rd.randint(100, 1000)
            Tables.PartProviderTable.add_new_part_provider(conn, i, j, cost)


def populate_part_workshop(conn):
    for i in range(1, len(part_types)):
        for j in range(1, Tables.get_number_of_rows(conn, Tables.WorkshopsTable.TABLE_NAME)):
            cost = rd.randint(1, 20)
            Tables.insert(conn, Tables.PartWorkshopTable.TABLE_NAME,
                          "'" + str(i) + "', '" + str(j) + "', '" + str(cost) + "'")


def populate_provider_workshop(conn):
    for i in range(1, len(provider_name) + 1):
        for j in range(1,  Tables.get_number_of_rows(conn, Tables.WorkshopsTable.TABLE_NAME) + 1):
            Tables.ProviderWorkshopTable.add_new_provider_workshop(conn, i, j)


def populate_car_parts(conn):
    for i in range(1, Tables.get_number_of_rows(conn, Tables.CarsTable.TABLE_NAME) + 1):
        for j in range(1,  Tables.get_number_of_rows(conn, Tables.PartTypesTable.TABLE_NAME) + 1):
            Tables.PartCarTable.add_new_part_car(conn, j, i)


def populate_orders(conn, amount):
    for i in range(1, amount):
        customer_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.CustomersTable.TABLE_NAME))
        car_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.CarsTable.TABLE_NAME))
        t = rd.randint(1, 21)
        st_time = create_time(0, t)
        end_time = create_time(t+1, 23)
        day = rd.randint(21, 25)
        if day < 10:
            date_day = "0" + str(day)
        else:
            date_day = str(day)
        month = 11
        if month < 10:
            date_month = "0" + str(month)
        else:
            date_month = str(month)
        init_loc = create_address()
        dest = create_address()
        dist = rd.randint(50, 200)

        Tables.OrdersTable.add_new_order(conn, customer_id, car_id, "2018-" + date_month + "-" + date_day,
                                         st_time, end_time, init_loc, dest, dist)


def populate_payments(conn, amount):
    for i in range(1, amount):
        customer_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.CustomersTable.TABLE_NAME))
        order_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.OrdersTable.TABLE_NAME))
        t = rd.randint(1, 21)
        st_time = create_time(0, t)
        end_time = create_time(t + 1, 23)
        day = rd.randint(21, 25)
        if day < 10:
            date_day = "0" + str(day)
        else:
            date_day = str(day)
        month = 11
        if month < 10:
            date_month = "0" + str(month)
        else:
            date_month = str(month)
        cost = rd.randint(200, 1000)

        Tables.PaymentsTable.add_new_payments(conn, customer_id, order_id, "2018-" + date_month + "-" + date_day,
                                              st_time, end_time, cost)


def populate_charges(conn, amount):
    for i in range(1, amount):
        car_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.CarsTable.TABLE_NAME))
        station_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.ChargingStationsTable.TABLE_NAME))
        t = rd.randint(1, 21)
        st_time = create_time(0, t)
        end_time = create_time(t + 1, 23)
        day = rd.randint(21, 25)
        if day < 10:
            date_day = "0" + str(day)
        else:
            date_day = str(day)
        month = 11
        if month < 10:
            date_month = "0" + str(month)
        else:
            date_month = str(month)
        cost = rd.randint(200, 1000)
        Tables.ChargesTable.add_new_charge(conn, car_id, station_id, "2018-" + date_month + "-" + date_day,
                                           st_time, end_time, cost)


def populate_repairs(conn, amount):
    for i in range(1, amount):
        car_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.CarsTable.TABLE_NAME))
        wid = rd.randint(1, Tables.get_number_of_rows(conn, Tables.WorkshopsTable.TABLE_NAME))
        part_type = rd.randint(1, Tables.get_number_of_rows(conn, Tables.PartTypesTable.TABLE_NAME))
        t = rd.randint(1, 21)
        st_time = create_time(0, t)
        end_time = create_time(t + 1, 23)
        day = rd.randint(21, 25)
        if day < 10:
            date_day = "0" + str(day)
        else:
            date_day = str(day)
        month = 11
        if month < 10:
            date_month = "0" + str(month)
        else:
            date_month = str(month)
        cost = rd.randint(200, 1000)
        Tables.RepairsTable.add_new_repair(conn, car_id, wid, part_type, "2018-" + date_month + "-" + date_day,
                                           st_time, end_time, cost)


def populate_order_parts(conn, amount):
    for i in range(1, amount):
        provide_id = rd.randint(1, Tables.get_number_of_rows(conn, Tables.ProvidersTable.TABLE_NAME))
        wid = rd.randint(1, Tables.get_number_of_rows(conn, Tables.WorkshopsTable.TABLE_NAME))
        part_type = rd.randint(1, Tables.get_number_of_rows(conn, Tables.PartTypesTable.TABLE_NAME))
        t = rd.randint(1, 21)
        st_time = create_time(0, t)
        end_time = create_time(t + 1, 23)
        day = rd.randint(21, 25)
        if day < 10:
            date_day = "0" + str(day)
        else:
            date_day = str(day)
        month = 11
        if month < 10:
            date_month = "0" + str(month)
        else:
            date_month = str(month)
        am = rd.randint(1, 100)
        Tables.OrderPartsTable.add_new_order_parts(conn, provide_id, wid, part_type,
                                                   "2018-" + date_month + "-" + date_day, st_time, end_time, am)


connection = Tables.create_connection()

populate_car_types(connection)
populate_part_types(connection)
populate_plug_types(connection)
populate_charging_stations(connection, stations)
populate_customers(connection, customers)
populate_cars(connection, cars)
populate_providers(connection)
populate_workshops(connection, workshops)
populate_sockets(connection)
populate_part_provider(connection)
populate_part_workshop(connection)
populate_provider_workshop(connection)
populate_orders(connection, 50)
populate_car_parts(connection)
populate_payments(connection, 50)
populate_charges(connection, 50)
populate_repairs(connection, 50)
populate_order_parts(connection, 50)
