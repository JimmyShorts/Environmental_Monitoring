#Monitoring humidity found "https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9"
import adafruit_dht
from issstreamer.streamer import Streamer
import time
import board

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Office"
BUCKET_NAME = ":partly_sunny: Room Temperatures"
BUCKET_KEY = "dht22sensor"
ACCESS_KEY = "ENTER ACCESS KEY HERE"
MINUTES_BETWEEN_READS = 10
METRIC_UNITS = False
# ---------------------------------

dhtSensor = adafruit_dht.DHT22(board.D4)
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
        try:
                humidity = dhtSensor.humidity
                temp_c = dhtSensor.temperature
        except RuntimeError:
                print("RuntimeError, trying again...")
                continue
                
        if METRIC_UNITS:
                streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
        else:
                temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
                streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
        humidity = format(humidity,".2f")
        streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
        streamer.flush()
        time.sleep(60*MINUTES_BETWEEN_READS)