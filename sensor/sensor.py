#!/usr/bin/env python3

# MQTT Sensor
import time
import Adafruit_DHT
import time
import json
import os
import logging

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2

from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBServerError

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        payload = [
                {
                    "measurement": "sensors",
                    "tags": { "environment": "greenhouse" },
                    "fields": { "temperature": temperature, "humidity": humidity }
                }
            ]
        try:
            client = InfluxDBClient(host='server.local', port=8086, username=os.environ['INFLUXDB_USER'], password=os.environ['INFLUXDB_PWD'])
            client.switch_database('home_assistant')
            client.write_points(payload)
            client.close()
        except (InfluxDBServerError):
            logging.error('Failed to send metrics to influxdb')
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(60)
