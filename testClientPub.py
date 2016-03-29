#http://stackoverflow.com/questions/31775450/publish-and-subscribe-with-paho-mqtt-client

import paho.mqtt.client as mqtt

mqttc=mqtt.Client()
mqttc.connect("54.201.188.88",1883,60)
mqttc.loop_start()

mqttc.publish("ewhs/12345678/spoint","A setpoint for you sir",2)

mqttc.loop_stop()
mqttc.disconnect()
