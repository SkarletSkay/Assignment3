import sqlite3
import TableConstants


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

    return None


def create_table(con, table_name, columns_of_table):
    try:
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + "(" + columns_of_table + "); ")
        con.commit()
    except sqlite3.Error as e:
        print(e)


conn = create_connection(TableConstants.DATABASE_NAME+".db")
create_table(conn, TableConstants.CUSTOMER_TABLE_NAME,
             TableConstants.CUSTOMER_TABLE_ID_COLUMN + " INTEGER, " +
             TableConstants.CUSTOMER_TABLE_NAME_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_USERNAME_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_EMAIL_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_COUNTRY_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_CITY_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_ZIP_COLUMN + " TEXT, " +
             TableConstants.CUSTOMER_TABLE_PHONE_COLUMN + " TEXT")

conn.cursor().execute("INSERT INTO customer VALUES (1,'bob','bob','boob','RUSISA', 'Moskva', '13', '8888')")
for row in conn.cursor().execute('SELECT * FROM customer ORDER BY customer_id'):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
