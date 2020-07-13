import paho.mqtt.client as mqtt
import json
from random import randrange
import time

mqttPublisher = mqtt.Client('item tracking')
mqttPublisher.connect('192.168.137.1', 1883, 70)

mqttPublisher.loop_start()

message = { "itemPurchasedX" : str(randrange(5)), "itemPurchasedY" : str(randrange(5)), "cartName" : "cart1"}
jmsg = json.dumps(message)
mqttPublisher.publish('item/', jmsg, 2)

time.sleep(10)