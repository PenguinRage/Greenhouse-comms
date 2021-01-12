#!/usr/bin/env python

# MQTT Sensor
import Adafruit_DHT
import paho.mqtt.publish as publish

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        publish.single("Greenhouse/temp", temperature, hostname="localhost")  #localhost for testing purposes only
        publish.single("Greenhouse/humidity", humidity, hostname="localhost")
    else:
        print("Failed to retrieve data from humidity sensor")
