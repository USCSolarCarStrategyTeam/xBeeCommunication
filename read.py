import serial
import time
from xbee import XBee, DigiMesh

serial_port = serial.Serial('/dev/tty.usbserial-142', 9600)

def error_call(e):
    print e

def print_data(data):
    print data['data']

xbee = DigiMesh(serial_port, callback=print_data, escaped = True, error_callback = error_call)

while True:
    try:
        time.sleep(0.001)
    except KeyboardInterrupt:
        break

xbee.halt()
serial_port.close()
