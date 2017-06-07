# Autor: Sergio Abarca Flores
# Contacto: sergioaf1991@gmail.com

# Practical Internet of Things (loT) with RaspberryPi
# Practical exercise, module 1
# Make a python program that makes an LED blink three times when a
# button is pressed. This exercise will be corrected by some of your partners.

import RPi.GPIO as GPIO
import time

# Variables
led = 4
button = 14

# Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Main
while True:
    input_state = GPIO.input(button)
    if input_state != True:
        for i in range(0, 3):
            GPIO.output(led, True)
            time.sleep(1)
            GPIO.output(led, False)
            time.sleep(1)
