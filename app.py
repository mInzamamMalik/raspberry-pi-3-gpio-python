import RPi.GPIO as GPIO  # Import GPIO library

# GPIO.setmode(GPIO.BCM) ## Use GPIO pin number
GPIO.setmode(GPIO.BOARD)  # Use board pin numbering

GPIO.setup(7, GPIO.OUT)  # Setup GPIO Pin to OUTPUT

GPIO.output(7, True)  # we can give 0 1, True False, GPIO.LOW GPIO.HIGH 

# GPIO.cleanup(); ## to free resources