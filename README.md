# Greenhouse-comms
Humidity and temperature being transferred through a local network for monitoring and automation sake.

## Versions
* v1 - used MQTT to Home-Assistant [Depreciated]. File can be found in old.
* v2 - Sends metrics through to Influxdb
``
## Dependencies
* Adafruit_DHT.DHT11 - Rpi Sensor
* Influxdb - Event DB

## Notes
sensor - script designed running on a extremely lightweight RPI device using bare min of anything that matters CPU, RAM, MEM.
