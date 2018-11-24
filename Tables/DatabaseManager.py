import sqlite3


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
