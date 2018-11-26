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


def get_number_of_rows(connection, table_name):
    return connection.cursor().execute("SELECT COUNT(*) FROM " + table_name).fetchone()[0]


def drop(connection, table_name):
    connection.cursor().execute("DROP TABLE IF EXISTS " + table_name)
    connection.commit()


class CarTypesTable:
    TABLE_NAME = "CarTypes"
    ID_COLUMN = "car_type_id"
    CAR_TYPE_COLUMN = "car_type"

    @staticmethod 
    def create_table(connection):
        create_table(connection, CarTypesTable.TABLE_NAME,
                     CarTypesTable.ID_COLUMN + " INTEGER PRIMARY KEY, " + CarTypesTable.CAR_TYPE_COLUMN + " TEXT")

    @staticmethod 
    def add_new_car_type(connection, car_type):
        insert(connection, CarTypesTable.TABLE_NAME, "NULL, '" + car_type + "'")


class PlugTypesTable:
    TABLE_NAME = "Plug_Types"
    ID_COLUMN = "plug_type_id"
    PLUG_TYPE_COLUMN = "plug_type"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PlugTypesTable.TABLE_NAME,
                     PlugTypesTable.ID_COLUMN + " INTEGER PRIMARY KEY, " + PlugTypesTable.PLUG_TYPE_COLUMN + " TEXT")

    @staticmethod 
    def add_new_plug_type(connection, plug_type):
        insert(connection, PlugTypesTable.TABLE_NAME, "NULL, '" + plug_type + "'")


class PartTypesTable:
    TABLE_NAME = "Part_Types"
    ID_COLUMN = "part_type_id"
    PART_TYPE_COLUMN = "part_type"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PartTypesTable.TABLE_NAME,
                     PartTypesTable.ID_COLUMN + " INTEGER PRIMARY KEY, " + PartTypesTable.PART_TYPE_COLUMN + " TEXT")

    @staticmethod 
    def add_new_part_type(connection, part_type):
        insert(connection, PartTypesTable.TABLE_NAME, "NULL, '" + part_type + "'")


class PartCarTable:
    TABLE_NAME = "Part_Car"
    PART_TYPE_ID_COLUMN = "part_type_id"
    CAR_TYPE_ID_COLUMN = "car_type_id"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PartCarTable.TABLE_NAME,
                     PartCarTable.PART_TYPE_ID_COLUMN + " INTEGER, " + PartCarTable.CAR_TYPE_ID_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + PartCarTable.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + PartCarTable.CAR_TYPE_ID_COLUMN +
                     ") REFERENCES " + CarTypesTable.TABLE_NAME + "(" + CarTypesTable.ID_COLUMN + ")," +
                     " UNIQUE(" + PartCarTable.PART_TYPE_ID_COLUMN + "," + PartCarTable.CAR_TYPE_ID_COLUMN + ")")

    @staticmethod 
    def add_new_part_car(connection, part_type, car_type):
        insert(connection, PartCarTable.TABLE_NAME, "'" + str(part_type) + "', '" + str(car_type) + "'")


class PartProviderTable:
    TABLE_NAME = "Part_Provider"
    PART_TYPE_ID_COLUMN = "part_type_id"
    PROVIDER_ID_COLUMN = "provider_id"
    COST_COLUMN = "cost"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PartProviderTable.TABLE_NAME,
                     PartProviderTable.PART_TYPE_ID_COLUMN + " INTEGER, " +
                     PartProviderTable.PROVIDER_ID_COLUMN + " INTEGER, " +
                     PartProviderTable.COST_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + PartProviderTable.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + PartProviderTable.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " UNIQUE(" + PartProviderTable.PART_TYPE_ID_COLUMN + "," + PartProviderTable.PROVIDER_ID_COLUMN + ")")

    @staticmethod 
    def add_new_part_provider(connection, part_type, provider_type, cost):
        insert(connection, PartProviderTable.TABLE_NAME, str(part_type) + ", " + str(provider_type) + ", " + str(cost))


class PartWorkshopTable:
    TABLE_NAME = "Part_Workshop"
    PART_TYPE_ID_COLUMN = "part_type_id"
    WORKSHOP_ID_COLUMN = "workshop_id"
    QUANTITY_COLUMN = "quantity"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PartWorkshopTable.TABLE_NAME,
                     PartWorkshopTable.PART_TYPE_ID_COLUMN + " INTEGER, " +
                     PartWorkshopTable.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     PartWorkshopTable.QUANTITY_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + PartWorkshopTable.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + PartWorkshopTable.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " UNIQUE(" + PartWorkshopTable.PART_TYPE_ID_COLUMN + "," +
                     PartWorkshopTable.WORKSHOP_ID_COLUMN + ")")

    @staticmethod 
    def add_new_part_workshop(connection, part_type, workshop, quantity):
        insert(connection, PartWorkshopTable.TABLE_NAME, "NULL, '" + part_type + "', '" + workshop + "', " + quantity)


class ProviderWorkshopTable:
    TABLE_NAME = "Provider_Workshop"
    PROVIDER_ID_COLUMN = "provider_id"
    WORKSHOP_ID_COLUMN = "workshop_id"

    @staticmethod 
    def create_table(connection):
        create_table(connection, ProviderWorkshopTable.TABLE_NAME,
                     ProviderWorkshopTable.PROVIDER_ID_COLUMN + " INTEGER, " +
                     ProviderWorkshopTable.WORKSHOP_ID_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + ProviderWorkshopTable.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + ProviderWorkshopTable.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " UNIQUE(" + ProviderWorkshopTable.PROVIDER_ID_COLUMN + "," +
                     ProviderWorkshopTable.WORKSHOP_ID_COLUMN + ")")

    @staticmethod 
    def add_new_provider_workshop(connection, provider, workshop):
        insert(connection, ProviderWorkshopTable.TABLE_NAME, str(provider) + ", " + str(workshop))


class ChargingStationsTable:
    TABLE_NAME = "Charging_Stations"
    ID_COLUMN = "uid"
    LOCATION_COLUMN = "location"

    @staticmethod 
    def create_table(connection):
        create_table(connection, ChargingStationsTable.TABLE_NAME,
                     ChargingStationsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     ChargingStationsTable.LOCATION_COLUMN + " TEXT")

    @staticmethod 
    def add_new_station(connection, location):
        insert(connection, ChargingStationsTable.TABLE_NAME,
               "NULL, '" + location + "'")


class ProvidersTable:
    TABLE_NAME = "Providers"
    ID_COLUMN = "provider_id"
    NAME_COLUMN = "provider_name"
    LOCATION_COLUMN = "location"
    PHONE_COLUMN = "phone_column"

    @staticmethod 
    def create_table(connection):
        create_table(connection, ProvidersTable.TABLE_NAME,
                     ProvidersTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     ProvidersTable.NAME_COLUMN + " TEXT, " +
                     ProvidersTable.LOCATION_COLUMN + " TEXT, " +
                     ProvidersTable.PHONE_COLUMN + " TEXT")

    @staticmethod 
    def add_new_provider(connection, name, location, phone):
        insert(connection, ProvidersTable.TABLE_NAME,
               "NULL, '" + name + "', '" + location + "', '" + phone + "'")


class WorkshopsTable:
    TABLE_NAME = "Workshops"
    ID_COLUMN = "workshop_id"
    LOCATION_COLUMN = "location"
    OPEN_TIME_COLUMN = "open_time_column"
    CLOSE_TIME_COLUMN = "close_time_column"

    @staticmethod 
    def create_table(connection):
        create_table(connection, WorkshopsTable.TABLE_NAME,
                     WorkshopsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     WorkshopsTable.LOCATION_COLUMN + " TEXT, " +
                     WorkshopsTable.OPEN_TIME_COLUMN + " INTEGER, " +
                     WorkshopsTable.CLOSE_TIME_COLUMN + " INTEGER, " +
                     "CHECK (" + WorkshopsTable.OPEN_TIME_COLUMN + " >= 0 AND " +
                     WorkshopsTable.OPEN_TIME_COLUMN + " <= 23 AND " +
                     WorkshopsTable.CLOSE_TIME_COLUMN + " >= 0 AND " +
                     WorkshopsTable.CLOSE_TIME_COLUMN + " <= 23)")

    @staticmethod 
    def add_new_workshop(connection, location, open_time, close_time):
        insert(connection, WorkshopsTable.TABLE_NAME,
               "NULL, '" + location + "', " + str(open_time) + ", " + str(close_time))


class CarsTable:
    TABLE_NAME = "Cars"
    ID_COLUMN = "car_id"
    PLUG_TYPE_ID_COLUMN = "plug_type_id"
    CAR_TYPE_ID_COLUMN = "car_type_id"
    COLOUR_COLUMN = "colour"
    PLATE_NUMBER_COLUMN = "plate_number"

    @staticmethod 
    def create_table(connection):
        create_table(connection, CarsTable.TABLE_NAME,
                     CarsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     CarsTable.PLUG_TYPE_ID_COLUMN + " INTEGER, " +
                     CarsTable.CAR_TYPE_ID_COLUMN + " INTEGER, " +
                     CarsTable.COLOUR_COLUMN + " TEXT, " +
                     CarsTable.PLATE_NUMBER_COLUMN + " TEXT," +
                     " FOREIGN KEY (" + CarsTable.PLUG_TYPE_ID_COLUMN +
                     ") REFERENCES " + PlugTypesTable.TABLE_NAME + "(" + PlugTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + CarsTable.CAR_TYPE_ID_COLUMN +
                     ") REFERENCES " + CarTypesTable.TABLE_NAME + "(" + CarTypesTable.ID_COLUMN + ")")

    @staticmethod 
    def add_new_car(connection, plug_type_id, car_type_id, colour, plate_number):
        insert(connection, CarsTable.TABLE_NAME,
               "NULL, " + str(plug_type_id) + ", " + str(car_type_id) + ", '" + colour + "', '" + plate_number + "'")


class SocketsTable:
    TABLE_NAME = "Sockets"
    ID_COLUMN = "socket_id"
    PLUG_TYPE_ID_COLUMN = "plug_type_id"
    CHARGING_STATION_ID = "uid"

    @staticmethod 
    def create_table(connection):
        create_table(connection, SocketsTable.TABLE_NAME,
                     SocketsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     SocketsTable.PLUG_TYPE_ID_COLUMN + " INTEGER, " +
                     SocketsTable.CHARGING_STATION_ID + " INTEGER, " +
                     " FOREIGN KEY (" + SocketsTable.PLUG_TYPE_ID_COLUMN +
                     ") REFERENCES " + PlugTypesTable.TABLE_NAME + "(" + PlugTypesTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + SocketsTable.CHARGING_STATION_ID +
                     ") REFERENCES " + ChargingStationsTable.TABLE_NAME + "(" + ChargingStationsTable.ID_COLUMN + ")")

    @staticmethod 
    def add_new_socket(connection, plug_type_id, charging_station_id):
        insert(connection, SocketsTable.TABLE_NAME,
               "NULL, " + str(plug_type_id) + ", '" + str(charging_station_id) + "'")


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

    @staticmethod 
    def create_table(connection):
        create_table(connection, CustomersTable.TABLE_NAME,
                     CustomersTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     CustomersTable.NAME_COLUMN + " TEXT, " +
                     CustomersTable.USERNAME_COLUMN + " TEXT, " +
                     CustomersTable.EMAIL_COLUMN + " TEXT, " +
                     CustomersTable.COUNTRY_COLUMN + " TEXT, " +
                     CustomersTable.CITY_COLUMN + " TEXT, " +
                     CustomersTable.ZIP_COLUMN + " TEXT, " +
                     CustomersTable.PHONE_COLUMN + " TEXT")

    @staticmethod 
    def add_new_customer(connection, name, username, email, country, city, zip_code, phone_number):
        insert(connection, CustomersTable.TABLE_NAME,
               "NULL, '" + name + "', '" + username + "', '" + email + "', '" + country + "', '" + city + "', '" +
               str(zip_code) + "', '" + phone_number + "'")


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

    @staticmethod 
    def create_table(connection):
        create_table(connection, OrdersTable.TABLE_NAME,
                     OrdersTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     OrdersTable.CUSTOMER_ID_COLUMN + " INTEGER, " +
                     OrdersTable.CAR_ID_COLUMN + " INTEGER, " +
                     OrdersTable.DATE_COLUMN + " REAL, " +
                     OrdersTable.START_TIME_COLUMN + " REAL, " +
                     OrdersTable.END_TIME_COLUMN + " REAL, " +
                     OrdersTable.INIT_LOCATION_COLUMN + " TEXT, " +
                     OrdersTable.DESTINATION_COLUMN + " TEXT, " +
                     OrdersTable.DISTANCE_COLUMN + " INTEGER," +
                     " FOREIGN KEY (" + OrdersTable.CUSTOMER_ID_COLUMN +
                     ") REFERENCES " + CustomersTable.TABLE_NAME + "(" + CustomersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + OrdersTable.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")"
                     )

    @staticmethod 
    def add_new_order(connection, customer_id, car_id, date, start_time, end_time, init_location, destination, distance):
        insert(connection, OrdersTable.TABLE_NAME,
               "NULL," + str(customer_id) + ", " + str(car_id) +
               ", julianday('" + date + "'), julianday('" + start_time + "'), julianday('" + end_time + "'), '" +
               init_location + "', '" + destination + "', " + str(distance))


class PaymentsTable:
    TABLE_NAME = "Payments"
    ID_COLUMN = "cheque_id"
    CUSTOMER_ID_COLUMN = "customer_id"
    ORDER_ID_COLUMN = "order_id"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    TOTAL_SUM_COLUMN = "total_sum"

    @staticmethod 
    def create_table(connection):
        create_table(connection, PaymentsTable.TABLE_NAME,
                     PaymentsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     PaymentsTable.CUSTOMER_ID_COLUMN + " INTEGER, " +
                     PaymentsTable.ORDER_ID_COLUMN + " INTEGER, " +
                     PaymentsTable.DATE_COLUMN + " REAL, " +
                     PaymentsTable.START_TIME_COLUMN + " REAL, " +
                     PaymentsTable.END_TIME_COLUMN + " REAL, " +
                     PaymentsTable.TOTAL_SUM_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + PaymentsTable.CUSTOMER_ID_COLUMN +
                     ") REFERENCES " + CustomersTable.TABLE_NAME + "(" + CustomersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + PaymentsTable.ORDER_ID_COLUMN +
                     ") REFERENCES " + OrdersTable.TABLE_NAME + "(" + OrdersTable.ID_COLUMN + ")"
                     )

    @staticmethod 
    def add_new_payments(connection, customer_id, order_id, date, start_time, end_time, total_sum):
        insert(connection, PaymentsTable.TABLE_NAME,
               "NULL, " + str(customer_id) + ", " + str(order_id) +
               ", julianday('" + date + "'), julianday('" + start_time + "'), julianday('" + end_time + "'), " +
               str(total_sum))


class ChargesTable:
    TABLE_NAME = "Charges"
    ID_COLUMN = "charge_id"
    CAR_ID_COLUMN = "car_id"
    STATION_ID_COLUMN = "uid"
    DATE_COLUMN = "date"
    START_TIME_COLUMN = "start_time"
    END_TIME_COLUMN = "end_time"
    COST_COLUMN = "cost"

    @staticmethod 
    def create_table(connection):
        create_table(connection, ChargesTable.TABLE_NAME,
                     ChargesTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     ChargesTable.CAR_ID_COLUMN + " INTEGER, " +
                     ChargesTable.STATION_ID_COLUMN + " INTEGER, " +
                     ChargesTable.DATE_COLUMN + " REAL, " +
                     ChargesTable.START_TIME_COLUMN + " REAL, " +
                     ChargesTable.END_TIME_COLUMN + " REAL, " +
                     ChargesTable.COST_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + ChargesTable.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + ChargesTable.STATION_ID_COLUMN +
                     ") REFERENCES " + ChargingStationsTable.TABLE_NAME + "(" + ChargingStationsTable.ID_COLUMN + ")"
                     )

    @staticmethod 
    def add_new_charge(connection, car_id, station_id, date, start_time, end_time, cost):
        insert(connection, ChargesTable.TABLE_NAME,
               "NULL, " + str(car_id) + ", " + str(station_id) +
               ", julianday('" + date + "'), julianday('" + start_time + "'), julianday('" + end_time + "'), "
               + str(cost))


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

    @staticmethod 
    def create_table(connection):
        create_table(connection, RepairsTable.TABLE_NAME,
                     RepairsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     RepairsTable.CAR_ID_COLUMN + " INTEGER, " +
                     RepairsTable.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     RepairsTable.PART_TYPE_ID_COLUMN + " INTEGER," +
                     RepairsTable.DATE_COLUMN + " REAL, " +
                     RepairsTable.START_TIME_COLUMN + " REAL, " +
                     RepairsTable.END_TIME_COLUMN + " REAL, " +
                     RepairsTable.COST_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + RepairsTable.CAR_ID_COLUMN +
                     ") REFERENCES " + CarsTable.TABLE_NAME + "(" + CarsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + RepairsTable.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + RepairsTable.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")"
                     )

    @staticmethod 
    def add_new_repair(connection, car_id, wid, part_type_id, date, start_time, end_time, cost):
        insert(connection, RepairsTable.TABLE_NAME,
               "NULL, " + str(car_id) + ", " + str(wid) + ", " + str(part_type_id) +
               ", julianday('" + date + "'), julianday('" + start_time + "'), julianday('" + end_time + "'), "
               + str(cost))


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

    @staticmethod 
    def create_table(connection):
        create_table(connection, OrderPartsTable.TABLE_NAME,
                     OrderPartsTable.ID_COLUMN + " INTEGER PRIMARY KEY, " +
                     OrderPartsTable.PROVIDER_ID_COLUMN + " INTEGER, " +
                     OrderPartsTable.WORKSHOP_ID_COLUMN + " INTEGER, " +
                     OrderPartsTable.PART_TYPE_ID_COLUMN + " INTEGER," +
                     OrderPartsTable.DATE_COLUMN + " REAL, " +
                     OrderPartsTable.START_TIME_COLUMN + " REAL, " +
                     OrderPartsTable.END_TIME_COLUMN + " REAL, " +
                     OrderPartsTable.AMOUNT_COLUMN + " INTEGER, " +
                     " FOREIGN KEY (" + OrderPartsTable.PROVIDER_ID_COLUMN +
                     ") REFERENCES " + ProvidersTable.TABLE_NAME + "(" + ProvidersTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + OrderPartsTable.WORKSHOP_ID_COLUMN +
                     ") REFERENCES " + WorkshopsTable.TABLE_NAME + "(" + WorkshopsTable.ID_COLUMN + ")," +
                     " FOREIGN KEY (" + OrderPartsTable.PART_TYPE_ID_COLUMN +
                     ") REFERENCES " + PartTypesTable.TABLE_NAME + "(" + PartTypesTable.ID_COLUMN + ")"
                     )

    @staticmethod 
    def add_new_order_parts(connection, provider_id, wid, part_type_id, date, start_time, end_time, amount):
        insert(connection, OrderPartsTable.TABLE_NAME,
               "NULL, " + str(provider_id) + ", " + str(wid) + ", " + str(part_type_id) +
               ", julianday('" + date + "'), julianday('" + start_time + "'), julianday('" + end_time + "'), "
               + str(amount))

