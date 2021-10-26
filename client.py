import paho.mqtt.client as mqtt
import serial
import time
import string
import RPi.GPIO as GPIO
from time import sleep
buzzer = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)


def on_connect(client, userdata, flags, rc): # func for making connection
 print("Connected to MQTT")
 print("Connection returned result: " + str(rc) )
 client.subscribe("RP")

def on_message(client, userdata, msg): # Func for Sending msg
 
 print(msg.topic+" "+str(msg.payload))
 print(str(msg.payload))
 if int(msg.payload) == 1:   
  print("Buzzer on")
  GPIO.output(buzzer,GPIO.HIGH)
 else:
  GPIO.output(buzzer,GPIO.LOW)
  print ("No Beep")

 
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("54.165.184.16", 1883, 60)
client.loop_forever()
