import pymssql
import TestVars
import Credentials
 
server = Credentials.Server
user = Credentials.DBuser
password = Credentials.DBPass
DataBaseName = Credentials.DB

conn = pymssql.connect(server, user, password, DataBaseName)
cursor = conn.cursor()

#Will be an insert statement from using the variables pulled from humidity.py
cursor.execute('Insert Into dbo.EMRecords(SensorNum, Temp, Humidity) Values(%i,%i,%i)' % (TestVars.SensorNum, TestVars.Temperature, TestVars.Humidity))
conn.commit() #need .commit() for inserts
conn.close
