import webiopi

GPIO = webiopi.GPIO

LIGHT1 = 11 # GPIO pin using BCM numbering
LIGHT2 = 9 # GPIO pin using BCM numbering

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT1, GPIO.OUT)
    GPIO.setFunction(LIGHT2, GPIO.OUT)	

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT1, GPIO.LOW)
    GPIO.digitalWrite(LIGHT2, GPIO.LOW)