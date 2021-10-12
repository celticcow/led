#!/usr/bin/python3

import time
from random import randint
import RPi.GPIO as GPIO

def set_pin(pin_index, pin_state):
    pins = [18, 23, 24]

    if pin_state == -1:
        GPIO.setup(pins[pin_index], GPIO.IN)
    else:
        GPIO.setup(pins[pin_index], GPIO.OUT)
        GPIO.output(pins[pin_index], pin_state)
#end of set_pin

def light_led(led_number, pin_led_states):
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        set_pin(pin_index, pin_state)
#end of light_led

def uniq_rand(prev_int):
    led_int = randint(0, 5)

    if(led_int == prev_int):
        led_int = randint(0, 5)
        if(led_int == prev_int):
            print("going recursive")
            led_int = uniq_rand(led_int)
        
        return(led_int)
    else:
        return(led_int)
#end of uniq_rand

def main():
    debug = 1
    
    pin_led_states = [
    [1, 0, -1], # A green top left    0
    [0, 1, -1], # B blue top right    1
    [1, -1, 0], # E orange mid left   2
    [0, -1, 1], # F green mid right   3
    [-1, 1, 0], # C white bottom left 4
    [-1, 0, 1]  # D blue bottom blue  5
    ]

    GPIO.setmode(GPIO.BCM)

    set_pin(0, -1)
    set_pin(1, -1)
    set_pin(2, -1)

    """
    # user input mode
    while True:
        x = int(input("Pin (0 to 5 / 9 to quit):"))
        if(x == 9):
            break
        light_led(x, pin_led_states)
    """
    prev_rand = -1

    for i in range(50):
        #led_int = randint(0, 5)
        led_int = uniq_rand(prev_rand)

        print(str(led_int))
        prev_rand = led_int

        light_led(led_int, pin_led_states)
        time.sleep(1)
    #end of for loop


    GPIO.cleanup()
#end of main

if __name__ == "__main__":
    main()
#end of multi_led