import math		# Library for exponential function
import requests     	# Library for communicating with Topcode Server
from pololu_drv8835_rpi import motors, MAX_SPEED

def linear(x):
	return -x

def root(x):
	return x^(-1/2)	

def logistic(x):
	return -(x / (x + math.exp(1 - x)));


# motors.setSpeeds(480, 480)
motors.setSpeeds(0, 0);






# running = True      # Tells car to start moving or not
# if not running:
#     ser.write('e'); # Tell car to stop
# else:
#     while True:
#         # Reach out to the server and grab the newest value of 'carMoving'
#         r = requests.get('http://localhost:3000/status')
# 
#         # If the server response is true, tell the car to move forward
#        if r.json()["forward"]:
##            ser.write('w')
#        else:
#            ser.write('e')
