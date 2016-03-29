#http://stackoverflow.com/questions/31775450/publish-and-subscribe-with-paho-mqtt-client

import paho.mqtt.client as mqtt
import sys
import time

ewh_id = sys.argv[1]
period = sys.argv[2]
state = True
setpoint = 30

mqttc=mqtt.Client()
mqttc.connect("54.201.188.88",1883,60)
mqttc.loop_start()

while(True):
    if(state):
        setpoint = 30
    else:
        setpoint = 20

    state = not state

    print("Publish: %s"%setpoint)
    mqttc.publish("ewhs/" + ewh_id  + "/spoint",setpoint,2)

    time.sleep(.500)

mqttc.loop_stop()
mqttc.disconnect()
