import pymssql
import TestVars
import Credentials
 
server = ('192.168.1.14')
user = Credentials.DBuser
password = Credentials.DBPass
DataBaseName = Credentials.DB

conn = pymssql.connect(server, user, password, DataBaseName)
cursor = conn.cursor()
#Will be an insert statement from using the variables pulled from humidity.py
cursor.execute('Insert Into dbo.EMRecords(SensorNum, Temp, Humidity) Values(1,7,9)')
conn.commit()
conn.close
