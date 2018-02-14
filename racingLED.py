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

li = (led1, led2, led3, led4, led5, led6)
button1 = GPIO.input(18)

def button_direction
    p = 1
    if button1 == False:
        print("button pressed")
        sleep(.1)
        p = p + 1


def forward_racing():
    for elem in li:
        elem.on()
        sleep(t)
        elem.off()

def backward_racing():
    for elem in reversed(li):
        elem.on()
        sleep(t)
        elem.off()

def running_stuff:
    while True:
        button_direction()
        if p = 1:
            forward_racing()
        elif p = 2:
            backward_racing()
        else:
            p = 1
            
