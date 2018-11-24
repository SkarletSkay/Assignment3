from Tables import DatabaseManager


class CustomerTable:
    CUSTOMER_TABLE_ID_COLUMN = "customer_id"
    CUSTOMER_TABLE_NAME = "Customer"
    CUSTOMER_TABLE_NAME_COLUMN = "full_name"
    CUSTOMER_TABLE_USERNAME_COLUMN = "username"
    CUSTOMER_TABLE_EMAIL_COLUMN = "email"
    CUSTOMER_TABLE_COUNTRY_COLUMN = "country"
    CUSTOMER_TABLE_CITY_COLUMN = "city"
    CUSTOMER_TABLE_ZIP_COLUMN = "zip_code"
    CUSTOMER_TABLE_PHONE_COLUMN = "phone_number"
    
    def __init__(self, connection):
        DatabaseManager.create_table(connection, self.CUSTOMER_TABLE_NAME,
                                     self.CUSTOMER_TABLE_ID_COLUMN + " INTEGER PRIMARY KEY, " +
                                     self.CUSTOMER_TABLE_NAME_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_USERNAME_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_EMAIL_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_COUNTRY_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_CITY_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_ZIP_COLUMN + " TEXT, " +
                                     self.CUSTOMER_TABLE_PHONE_COLUMN + " TEXT")

    def add_new_customer(self, connection, name, username, email, country, city, zip_code, phone_number):
        DatabaseManager.insert(connection, self.CUSTOMER_TABLE_NAME, 
                               "'" + name + "', '" + username + "', '" + email + "', '" +
                               "', '" + country + "', '" + city + "', '" +
                               "', '" + zip_code + "', '" + phone_number)
