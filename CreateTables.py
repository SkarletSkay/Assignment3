import Tables


conn = Tables.create_connection()

Tables.CarTypesTable.create_table(conn)
Tables.PlugTypesTable.create_table(conn)
Tables.CarsTable.create_table(conn)
Tables.ChargingStationsTable.create_table(conn)
Tables.SocketsTable.create_table(conn)
Tables.PartTypesTable.create_table(conn)
Tables.PartCarTable.create_table(conn)
Tables.ProvidersTable.create_table(conn)
Tables.PartProviderTable.create_table(conn)
Tables.WorkshopsTable.create_table(conn)
Tables.PartWorkshopTable.create_table(conn)
Tables.ProviderWorkshopTable.create_table(conn)
Tables.CustomersTable.create_table(conn)
Tables.OrdersTable.create_table(conn)
Tables.PaymentsTable.create_table(conn)
Tables.ChargesTable.create_table(conn)
Tables.RepairsTable.create_table(conn)
Tables.OrderPartsTable.create_table(conn)

conn.close()
