#!/usr/bin/env python

# MQTT Client
# Continuously monitor two different MQTT topics for data,

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the other clients.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("greenhouse/sensor")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("server", 1883, 60)
client.loop_forever()
