# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("Greenhouse/temp", "32", hostname="localhost")
publish.single("Greenhouse/humidity", "79", hostname="localhost")
print("Done")
