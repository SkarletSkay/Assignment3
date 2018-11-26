import Tables

connection = Tables.create_connection()

Tables.drop(connection, Tables.CarTypesTable.TABLE_NAME)
Tables.drop(connection, Tables.PlugTypesTable.TABLE_NAME)
Tables.drop(connection, Tables.CarsTable.TABLE_NAME)
Tables.drop(connection, Tables.ChargingStationsTable.TABLE_NAME)
Tables.drop(connection, Tables.SocketsTable.TABLE_NAME)
Tables.drop(connection, Tables.PartTypesTable.TABLE_NAME)
Tables.drop(connection, Tables.PartCarTable.TABLE_NAME)
Tables.drop(connection, Tables.ProvidersTable.TABLE_NAME)
Tables.drop(connection, Tables.PartProviderTable.TABLE_NAME)
Tables.drop(connection, Tables.WorkshopsTable.TABLE_NAME)
Tables.drop(connection, Tables.PartWorkshopTable.TABLE_NAME)
Tables.drop(connection, Tables.ProviderWorkshopTable.TABLE_NAME)
Tables.drop(connection, Tables.CustomersTable.TABLE_NAME)
Tables.drop(connection, Tables.OrdersTable.TABLE_NAME)
Tables.drop(connection, Tables.PaymentsTable.TABLE_NAME)
Tables.drop(connection, Tables.ChargesTable.TABLE_NAME)
Tables.drop(connection, Tables.RepairsTable.TABLE_NAME)
Tables.drop(connection, Tables.OrderPartsTable.TABLE_NAME)

connection.close()

