import sqlite3

DATABASE_NAME = "Database"


def create_connection():
    try:
        connection = sqlite3.connect(DATABASE_NAME + ".db")
        sqlite3.complete_statement("PRAGMA foreign_keys = ON;")
        return connection
    except sqlite3.Error as e:
        print(e)

    return None


def create_table(connection, table_name, columns_of_table):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + columns_of_table + "); ")
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert(connection, table_name, data):
    connection.cursor().execute("INSERT INTO " + table_name + " VALUES (" + data + ")")
    connection.commit()


class CarTypesTable:
    TABLE_NAME = "CarTypes"
    ID_COLUMN = "car_type_id"
    CAR_TYPE_COLUMN = "car_type"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " + self.CAR_TYPE_COLUMN + " TEXT")

    def add_new_car_type(self, connection, car_type):
        insert(connection, self.TABLE_NAME, "NULL, '" + car_type + "'")


class PlugTypesTable:
    TABLE_NAME = "Plug_Types"
    ID_COLUMN = "plug_type_id"
    PLUG_TYPE_COLUMN = "plug_type"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " + self.PLUG_TYPE_COLUMN + " TEXT")

    def add_new_plug_type(self, connection, plug_type):
        insert(connection, self.TABLE_NAME, "NULL, '" + plug_type + "'")


class PartTypesTable:
    TABLE_NAME = "Part_Types"
    ID_COLUMN = "part_type_id"
    PART_TYPE_COLUMN = "part_type"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " + self.PART_TYPE_COLUMN + " TEXT")

    def add_new_part_type(self, connection, part_type):
        insert(connection, self.TABLE_NAME, "NULL, '" + part_type + "'")


class PartCarTable:
    TABLE_NAME = "Part_Car"
    PART_TYPE_ID_COLUMN = "part_type_id"
    CAR_TYPE_ID_COLUMN = "car_type_id"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.PART_TYPE_ID_COLUMN + " INTEGER, " + self.CAR_TYPE_ID_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + self.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.CAR_TYPE_ID_COLUMN +
                     ") REFERENCES " + CarTypesTable.TABLE_NAME + "(" + CarTypesTable.ID_COLUMN + ")," +
                     " UNIQUE(" + self.PART_TYPE_ID_COLUMN + "," + self.CAR_TYPE_ID_COLUMN + ")")

    def add_new_part_car(self, connection, part_type, car_type):
        insert(connection, self.TABLE_NAME, "'" + str(part_type) + "', '" + str(car_type) + "'")


class PartProviderTable:
    TABLE_NAME = "Part_Provider"
    PART_TYPE_ID_COLUMN = "part_type_id"
    PROVIDER_ID_COLUMN = "provider_id"
    COST_COLUMN = "cost"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.PART_TYPE_ID_COLUMN + " INTEGER, " +
                     self.PROVIDER_ID_COLUMN + " INTEGER, " +
                     self.COST_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + self.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " UNIQUE(" + self.PART_TYPE_ID_COLUMN + "," + self.PROVIDER_ID_COLUMN + ")")

    def add_new_part_provider(self, connection, part_type, provider_type, cost):
        insert(connection, self.TABLE_NAME, "NULL, '" + part_type + "', '" + provider_type + "', " + cost)


class PartWorkshopTable:
    TABLE_NAME = "Part_Workshop"
    PART_TYPE_ID_COLUMN = "part_type_id"
    WORKSHOP_ID_COLUMN = "workshop_id"
    QUANTITY_COLUMN = "quantity"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.PART_TYPE_ID_COLUMN + " INTEGER, " +
                     self.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     self.QUANTITY_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + self.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " UNIQUE(" + self.PART_TYPE_ID_COLUMN + "," + self.WORKSHOP_ID_COLUMN + ")")

    def add_new_part_workshop(self, connection, part_type, workshop, quantity):
        insert(connection, self.TABLE_NAME, "NULL, '" + part_type + "', '" + workshop + "', " + quantity)


class ProviderWorkshopTable:
    TABLE_NAME = "Provider_Workshop"
    PROVIDER_ID_COLUMN = "provider_id"
    WORKSHOP_ID_COLUMN = "workshop_id"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.PROVIDER_ID_COLUMN + " INTEGER, " +
                     self.WORKSHOP_ID_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + self.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " UNIQUE(" + self.PROVIDER_ID_COLUMN + "," + self.WORKSHOP_ID_COLUMN + ")")

    def add_new_provider_workshop(self, connection, provider, workshop):
        insert(connection, self.TABLE_NAME, "NULL, '" + provider + "', '" + workshop + "'")


class ChargingStationsTable:
    TABLE_NAME = "Charging_Stations"
    ID_COLUMN = "uid"
    LOCATION_COLUMN = "location"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.LOCATION_COLUMN + " TEXT")

    def add_new_station(self, connection, location):
        insert(connection, self.TABLE_NAME,
               "NULL, '" + location + "'")


class ProvidersTable:
    TABLE_NAME = "Providers"
    ID_COLUMN = "provider_id"
    NAME_COLUMN = "provider_name"
    LOCATION_COLUMN = "location"
    PHONE_COLUMN = "phone_column"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.NAME_COLUMN + " TEXT, " +
                     self.LOCATION_COLUMN + " TEXT, " +
                     self.PHONE_COLUMN + " TEXT")

    def add_new_provider(self, connection, name, location, phone):
        insert(connection, self.TABLE_NAME,
               "NULL, '" + name + "', '" + location + "', '" + phone + "'")


class WorkshopsTable:
    TABLE_NAME = "Workshops"
    ID_COLUMN = "workshop_id"
    LOCATION_COLUMN = "location"
    OPEN_TIME_COLUMN = "open_time_column"
    CLOSE_TIME_COLUMN = "close_time_column"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.LOCATION_COLUMN + " TEXT, " +
                     self.OPEN_TIME_COLUMN + " INTEGER, " +
                     self.CLOSE_TIME_COLUMN + " INTEGER, " +
                     "CHECK (" + self.OPEN_TIME_COLUMN + " >= 0 AND " + self.OPEN_TIME_COLUMN + " < 23 AND " +
                     self.CLOSE_TIME_COLUMN + " >= 0 AND " +
                     self.CLOSE_TIME_COLUMN + " < 23)")

    def add_new_workshop(self, connection, location, open_time, close_time):
        insert(connection, self.TABLE_NAME,
               "NULL, '" + location + "', " + open_time + "', " + close_time)


class CarsTable:
    TABLE_NAME = "Cars"
    ID_COLUMN = "car_id"
    PLUG_TYPE_ID_COLUMN = "plug_type_id"
    CAR_TYPE_ID_COLUMN = "car_type_id"
    COLOUR_COLUMN = "colour"
    PLATE_NUMBER_COLUMN = "plate_number"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.PLUG_TYPE_ID_COLUMN + " INTEGER, " +
                     self.CAR_TYPE_ID_COLUMN + " INTEGER, " +
                     self.COLOUR_COLUMN + " TEXT, " +
                     self.PLATE_NUMBER_COLUMN + " TEXT," +
                     " FOREIGN KEY (" + self.PLUG_TYPE_ID_COLUMN +
                     ") REFERENCES " + PlugTypesTable.TABLE_NAME + "(" + PlugTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.CAR_TYPE_ID_COLUMN +
                     ") REFERENCES " + CarTypesTable.TABLE_NAME + "(" + CarTypesTable.ID_COLUMN + ")")

    def add_new_car(self, connection, plug_type_id, car_type_id, colour, plate_number):
        insert(connection, self.TABLE_NAME,
               "NULL, '" + plug_type_id + ", " + car_type_id + ", '" + colour + "', '" + plate_number)


class SocketsTable:
    TABLE_NAME = "Sockets"
    ID_COLUMN = "socket_id"
    PLUG_TYPE_ID_COLUMN = "plug_type_id"
    CHARGING_STATION_ID = "uid"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.PLUG_TYPE_ID_COLUMN + " INTEGER, " +
                     self.CHARGING_STATION_ID + " INTEGER, " +
                     " FOREIGN KEY (" + self.PLUG_TYPE_ID_COLUMN +
                     ") REFERENCES " + PlugTypesTable.TABLE_NAME + "(" + PlugTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.CHARGING_STATION_ID +
                     ") REFERENCES " + ChargingStationsTable.TABLE_NAME + "(" + ChargingStationsTable.ID_COLUMN + ")")

    def add_new_socket(self, connection, plug_type_id, charging_station_id):
        insert(connection, self.TABLE_NAME,
               "NULL, '" + plug_type_id + "', '" + charging_station_id + "'")


class CustomersTable:
    TABLE_NAME = "Customers"
    ID_COLUMN = "customer_id"
    NAME_COLUMN = "full_name"
    USERNAME_COLUMN = "username"
    EMAIL_COLUMN = "email"
    COUNTRY_COLUMN = "country"
    CITY_COLUMN = "city"
    ZIP_COLUMN = "zip_code"
    PHONE_COLUMN = "phone_number"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.NAME_COLUMN + " TEXT, " +
                     self.USERNAME_COLUMN + " TEXT, " +
                     self.EMAIL_COLUMN + " TEXT, " +
                     self.COUNTRY_COLUMN + " TEXT, " +
                     self.CITY_COLUMN + " TEXT, " +
                     self.ZIP_COLUMN + " TEXT, " +
                     self.PHONE_COLUMN + " TEXT")

    def add_new_customer(self, connection, name, username, email, country, city, zip_code, phone_number):
        insert(connection, self.TABLE_NAME,
               "'" + name + "', '" + username + "', '" + email + "', '" + country + "', '" + city + "', '" +
               "', '" + zip_code + "', '" + phone_number)


class OrdersTable:
    TABLE_NAME = "Orders"
    ID_COLUMN = "order_id"
    CUSTOMER_ID_COLUMN = "customer_id"
    CAR_ID_COLUMN = "car_id"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    INIT_LOCATION_COLUMN = "init_location"
    DESTINATION_COLUMN = "destination"
    COST_COLUMN = "cost"
    DISTANCE_COLUMN = "distance"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.CUSTOMER_ID_COLUMN + " INTEGER, " +
                     self.CAR_ID_COLUMN + " INTEGER, " +
                     self.DATE_COLUMN + " REAL, " +
                     self.START_TIME_COLUMN + " INTEGER, " +
                     self.END_TIME_COLUMN + " INTEGER, " +
                     self.INIT_LOCATION_COLUMN + " TEXT, " +
                     self.DESTINATION_COLUMN + " TEXT, " +
                     self.COST_COLUMN + " INTEGER, " +
                     self.DISTANCE_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + self.CUSTOMER_ID_COLUMN +
                     ") REFERENCES " + CustomersTable.TABLE_NAME + "(" + CustomersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")"
                     )

    def add_new_order(self, connection, customer_id, car_id, date, start_time, end_time, init_location, destination,
                      cost, distance):
        insert(connection, self.TABLE_NAME,
               customer_id + ", " + car_id + ", " + date + ", " + start_time + ", " + end_time + ", '" +
               init_location + "', '" + destination + "', " + cost + ", " + distance)


class PaymentsTable:
    TABLE_NAME = "Payments"
    ID_COLUMN = "cheque_id"
    CUSTOMER_ID_COLUMN = "customer_id"
    ORDER_ID_COLUMN = "order_id"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    TOTAL_SUM_COLUMN = "total_sum"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.CUSTOMER_ID_COLUMN + " INTEGER, " +
                     self.ORDER_ID_COLUMN + " INTEGER, " +
                     self.DATE_COLUMN + " REAL, " +
                     self.START_TIME_COLUMN + " INTEGER, " +
                     self.END_TIME_COLUMN + " INTEGER, " +
                     self.TOTAL_SUM_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + self.CUSTOMER_ID_COLUMN +
                     ") REFERENCES " + CustomersTable.TABLE_NAME + "(" + CustomersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.ORDER_ID_COLUMN +
                     ") REFERENCES " + OrdersTable.TABLE_NAME + "(" + OrdersTable.ID_COLUMN + ")"
                     )

    def add_new_payments(self, connection, customer_id, order_id, date, start_time, end_time, total_sum):
        insert(connection, self.TABLE_NAME,
               customer_id + ", " + order_id + ", " + date + ", " + start_time + ", " + end_time + ", " + total_sum)


class ChargesTable:
    TABLE_NAME = "Charges"
    ID_COLUMN = "charge_id"
    CAR_ID_COLUMN = "car_id"
    STATION_ID_COLUMN = "uid"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    COST_COLUMN = "cost"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.CAR_ID_COLUMN + " INTEGER, " +
                     self.STATION_ID_COLUMN + " INTEGER, " +
                     self.DATE_COLUMN + " REAL, " +
                     self.START_TIME_COLUMN + " INTEGER, " +
                     self.END_TIME_COLUMN + " INTEGER, " +
                     self.COST_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + self.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.STATION_ID_COLUMN +
                     ") REFERENCES " + ChargingStationsTable.TABLE_NAME + "(" + ChargingStationsTable.ID_COLUMN + ")"
                     )

    def add_new_charge(self, connection, car_id, station_id, date, start_time, end_time, cost):
        insert(connection, self.TABLE_NAME,
               car_id + ", " + station_id + ", " + date + ", " + start_time + ", " + end_time + ", " + cost)


class RepairsTable:
    TABLE_NAME = "Repairs"
    ID_COLUMN = "repair_id"
    CAR_ID_COLUMN = "car_id"
    WORKSHOP_ID_COLUMN = "wid"
    PART_TYPE_ID_COLUMN = "part_type_id"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    COST_COLUMN = "cost"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.CAR_ID_COLUMN + " INTEGER, " +
                     self.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     self.PART_TYPE_ID_COLUMN + " INTEGER," +
                     self.DATE_COLUMN + " REAL, " +
                     self.START_TIME_COLUMN + " INTEGER, " +
                     self.END_TIME_COLUMN + " INTEGER, " +
                     self.COST_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + self.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")"
                     )

    def add_new_repair(self, connection, car_id, wid, part_type_id, date, start_time, end_time, cost):
        insert(connection, self.TABLE_NAME,
               car_id + ", " + wid + ", " + part_type_id + ", " + date + ", " +
               start_time + ", " + end_time + ", " + cost)


class OrderPartsTable:
    TABLE_NAME = "OrderParts"
    ID_COLUMN = "order_parts_id"
    PROVIDER_ID_COLUMN = "provider_id"
    WORKSHOP_ID_COLUMN = "wid"
    PART_TYPE_ID_COLUMN = "part_type_id"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    AMOUNT_COLUMN = "amount"

    def __init__(self, connection):
        create_table(connection, self.TABLE_NAME,
                     self.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     self.PROVIDER_ID_COLUMN + " INTEGER, " +
                     self.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     self.PART_TYPE_ID_COLUMN + " INTEGER," +
                     self.DATE_COLUMN + " REAL, " +
                     self.START_TIME_COLUMN + " INTEGER, " +
                     self.END_TIME_COLUMN + " INTEGER, " +
                     self.AMOUNT_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + self.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + self.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")"
                     )

    def add_new_order_parts(self, connection, provider_id, wid, part_type_id, date, start_time, end_time, amount):
        insert(connection, self.TABLE_NAME,
               provider_id + ", " + wid + ", " + part_type_id + ", " + date + ", " +
               start_time + ", " + end_time + ", " + amount)