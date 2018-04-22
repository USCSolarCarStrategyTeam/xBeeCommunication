#!/usr/bin/env python


import time
import serial


arduino = serial.Serial(port='/dev/ttyUSB1', baudrate=115200)

xBeeOut = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

incomingData = arduino.readline()

while incomingData is not None:
   #print incomingData.decode("UTF-8")
    print incomingData
    xBeeOut.write(incomingData)
    incomingData = arduino.readline()