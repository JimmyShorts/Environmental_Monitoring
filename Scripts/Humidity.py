import adafruit_dht
import time
import board

DHT22_1 = adafruit_dht.DHT22(board.D4)

def Check_The_Humidity():
    Temperature_c = DHT22_1.temperature
    Humidity = DHT22_1.humidity
    return Temperature_c, Humidity
