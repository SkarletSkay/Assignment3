import Tables

conn = Tables.create_connection()


car_types = Tables.CarTypesTable(conn)
plug_type = Tables.PlugTypesTable(conn)
car = Tables.CarsTable(conn)
stat = Tables.ChargingStationsTable(conn)
soc = Tables.SocketsTable(conn)
pt = Tables.PartTypesTable(conn)
pc = Tables.PartCarTable(conn)
pr = Tables.ProvidersTable(conn)
pp = Tables.PartProviderTable(conn)
ws = Tables.WorkshopsTable(conn)
pw = Tables.PartWorkshopTable(conn)
wp = Tables.ProviderWorkshopTable(conn)
c = Tables.CustomersTable(conn)
o = Tables.OrdersTable(conn)
p = Tables.PaymentsTable(conn)
ch = Tables.ChargesTable(conn)
re = Tables.RepairsTable(conn)
op = Tables.OrderPartsTable(conn)

conn.close()
