#!/usr/bin/env python


import time
import serial

ser = serial.Serial(

   port='/dev/ttyUSB0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
ser.flush()


while 1:
	#if ser.in_waiting()>0:
   	x=ser.readline()
   	print ser.in_waiting
   	print x
