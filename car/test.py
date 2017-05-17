import serial
import requests

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

running = True
if not running:
    ser.write('e');
else:
    while True:
        r = requests.get('http://localhost:3000/status')
        if r.json()["forward"]:
            ser.write('w')
        else:
            ser.write('e')
