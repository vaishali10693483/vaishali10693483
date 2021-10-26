import paho.mqtt.publish as publish
import serial
import time
import string

ser = serial.Serial("/dev/rfcomm3")

while True:
 #print(ser)
 rawserial = ser.readline()
 
 cookedserial = rawserial.decode('utf-8').strip('\r\n')
 publish.single("ULTRASONIC", cookedserial, hostname="localhost")
 print("Done")
