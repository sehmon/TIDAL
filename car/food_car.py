import math		# Library for exponential function
import requests     	# Library for communicating with Topcode Server
# from pololu_drv8835_rpi import motors, MAX_SPEED

def linear(x, b):
	return -x + b

def root(x, b):
	return (x+(1/(b^2)))^(-1/2)	

def logistic(x, b):
	return -(x / (x + math.exp(1 - x)));


def get_food_function(function_type):
    return {
            'linear': linear,
            'root': root,
            'logistic': logistic
            }[function_type]


serverUrl = "http://104.236.85.232:3000/status"

running = True
currFood = {}

while(running):
    r = requests.get(serverUrl)
    serverFood = r.json().get("food", {})
    if (serverFood and (serverFood != currFood)):
        currFood = serverFood
        functionType = currFood["type"]
        calories = currFood["calories"]
        foodFunction = get_food_function(functionType)

        for i in xrange(0, 100000):
            motorValue = foodFunction(i/1000.0, calories)
            if motorValue > 0:
                print motorValue
                # motors.setSpeeds(motorValue, motorValue);
