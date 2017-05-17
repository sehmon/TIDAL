import serial       # Library for communicating with Arduino
import requests     # Library for communicating with Topcode Server

# Connect to the Arduino's serial port

SERIAL_PORT = '/dev/cu.usbmodem1421'
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

running = True      # Tells car to start moving or not
if not running:
    ser.write('e'); # Tell car to stop
else:
    while True:
        # Reach out to the server and grab the newest value of 'carMoving'
        r = requests.get('http://localhost:3000/status')

        # If the server response is true, tell the car to move forward
        if r.json()["forward"]:
            ser.write('w')
        else:
            ser.write('e')
