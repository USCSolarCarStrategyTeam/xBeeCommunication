from xbee.thread import XBee, DigiMesh, ZigBee
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
xbee = ZigBee(ser)

while True:
    try:
        xbee.tx(dest_addr = '\x00\x13\', data = 'hello')
        print "sent"
        time.sleep(0.5)
    except KeyboardInterrupt:
        break

ser.close()
