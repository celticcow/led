#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

def main():
    green_led_pin = 18
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(green_led_pin, GPIO.OUT)
    
    GPIO.output(green_led_pin, True)
    for i in range(10):
        print("-", end=" ")
        time.sleep(1)
    #time.sleep(20)
    GPIO.output(green_led_pin, False)

if __name__ == "__main__":
    main()
#end of program