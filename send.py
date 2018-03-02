from xbee.thread import XBee, DigiMesh
import serial
import time

ser = serial.Serial('/dev/tty.usbserial-141', 9600)
xbee = DigiMesh(ser)

while True:
    try:
        xbee.send('tx', dest_addr = '\x00\x13\xA2\x00\x40\xF7\xF9\xF7', data = 'hello')
        print "sent"
        time.sleep(0.5)
    except KeyboardInterrupt:
        break

ser.close()
