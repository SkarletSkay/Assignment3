import Tables

conn = Tables.create_connection()

car_types = Tables.CarTypesTable(conn)

conn.close()
