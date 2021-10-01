#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

def turn_led_on(color):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(color, GPIO.OUT)
    
    GPIO.output(color, True)
#end of turn_led_on 

def turn_led_off(color):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(color, GPIO.OUT)
    
    GPIO.output(color, False)
#end of turn_led_off

def main():
    green_led_pin = 18
    
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(green_led_pin, GPIO.OUT)
    
    #GPIO.output(green_led_pin, True)
    turn_led_on(green_led_pin)

    for i in range(10):
        print("-")
        time.sleep(1)
    #time.sleep(20)
    turn_led_off(green_led_pin)

    GPIO.cleanup()
#end of main

if __name__ == "__main__":
    main()
#end of program