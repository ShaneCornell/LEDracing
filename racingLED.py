# Racing LEDs with buttons to change direction and frequency

from time import sleep
import RPI.GPIO as GPIO

#Button setup
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#LED setup
GPIO.setup(27, GPIO.OUT)
GPIO.output(27,0)


while True:
    if(GPIO.input(22) == 1):
        GPIO.output(27,1)
    else:
        GPIO.output(27,0)
        
