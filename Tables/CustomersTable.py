import TableConstants

class CustomerTable:

    def __init__(self, connection):
        create_table(conn, TableConstants.CUSTOMER_TABLE_NAME,
                     TableConstants.CUSTOMER_TABLE_ID_COLUMN + " INTEGER, " +
                     TableConstants.CUSTOMER_TABLE_NAME_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_USERNAME_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_EMAIL_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_COUNTRY_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_CITY_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_ZIP_COLUMN + " TEXT, " +
                     TableConstants.CUSTOMER_TABLE_PHONE_COLUMN + " TEXT")
