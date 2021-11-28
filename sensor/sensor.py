#!/usr/bin/env python

# MQTT Sensor
import paho.mqtt.client as paho
import time
import Adafruit_DHT
import time
import json
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2
IP="192.168.1.106"

def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))


def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


client = paho.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(IP, 1883)
client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        payload = { "temperature": temperature, "humidity": humidity }
        (rc, mid) = client.publish("greenhouse/sensor", json.dumps(payload), qos=1)
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(60)
