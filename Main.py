import Tables.DatabaseManager as DatabaseManager

conn = DatabaseManager.create_connection()
conn.close()
