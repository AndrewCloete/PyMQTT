#http://stackoverflow.com/questions/31775450/publish-and-subscribe-with-paho-mqtt-client

import paho.mqtt.client as mqtt
import sys

ewh_id = sys.argv[1]
setpoint = sys.argv[2]

mqttc=mqtt.Client()
mqttc.connect("54.201.188.88",1883,60)
mqttc.loop_start()

mqttc.publish("ewhs/" + ewh_id  + "/spoint",setpoint,2)

mqttc.loop_stop()
mqttc.disconnect()
