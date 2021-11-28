#!/usr/bin/env python3

# MQTT Sensor
import time
import Adafruit_DHT
import time
import json
import os

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2

from influxdb import InfluxDBClient
client = InfluxDBClient(host='server.local', port=8086, username=os.environ['INFLUXDB_USER'], password=os.environ['INFLUXDB_PWD'])
client.switch_database('greenhouse')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        payload = [ 
                { "measurement": "temperature", "fields": { "value": temperature } },
                { "measurement": "humidity", "fields": { "value": humidity } }
            ]
        client.write_points(payload)
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(15)
