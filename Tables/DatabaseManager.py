import sqlite3


DATABASE_NAME = "Database"


def create_connection():
    try:
        connection = sqlite3.connect(DATABASE_NAME + ".db")
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