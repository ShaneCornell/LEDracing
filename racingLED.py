# Racing LEDs with buttons to change direction and freque

from time import sleep
from gpiozero import LED
import RPi.GPIO as gpiozero

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

led1 = LED(5)
led2 = LED(6)
led3 = LED(13)
led4 = LED(19)
led5 = LED(26)
led6 = LED(9)



def forward_racing():
    x = 0
    for x in range(1, 6):
        ledx.on()
        sleep(t)
        ledx.off()
