#Connecting to the Squirrel server

import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server}; Server=192.168.1.14, 1433; Database=Mushroom; UID=Taylor; PWD=Shroomy;')
cursor = conn.cursor()
cursor.execute('Select * from Mushroom.dbo.EMRecords')

for row in cursor:
    print(row)

conn.close()