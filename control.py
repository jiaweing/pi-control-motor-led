#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

led_on = False
motor_on = False
count = 0

LED_PIN = 18
BUTTON_PIN = 23
MOTOR_PIN = 24

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(MOTOR_PIN, GPIO.OUT, initial=GPIO.LOW)

def switch(state=None, device='both'):
    global led_on, motor_on, count

    if device not in ['fan', 'light', 'both']:
        print("Invalid device. Please enter 'fan', 'light', or 'both'.")
        return

    if state is not None:
        if device == 'fan' or device == 'both':
            motor_on = state
        if device == 'light' or device == 'both':
            led_on = state
    else:
        if device == 'fan' or device == 'both':
            motor_on = not motor_on
        if device == 'light' or device == 'both':
            led_on = not led_on

    count += 1

    if led_on == True:
        print("Turning on Lights\tcount: " + str(count))
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print("Turning off Lights\tcount: " + str(count))
        GPIO.output(LED_PIN, GPIO.LOW)

    if motor_on == True:
        print("Turning on Fan\tcount: " + str(count))
        GPIO.output(MOTOR_PIN, GPIO.HIGH)
    else:
        print("Turning off Fan\tcount: " + str(count))
        GPIO.output(MOTOR_PIN, GPIO.LOW)

def buttonPressCallback(channel):
    time.sleep(0.1)  # Add a delay
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Check if the button is still pressed
        switch()

def detectButtonPress():
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=buttonPressCallback, bouncetime=300)
    
def main():
    print("===== FAN AND LIGHTS =====")
    print(f"Button:\tpin {BUTTON_PIN}")
    print(f"Lights:\tpin {LED_PIN}")
    print(f"Fan:\tpin {MOTOR_PIN}")

    setupGPIO()
    detectButtonPress()
    
    while True:
        command = input("Enter a command (fan on/fan off/light on/light off/all on/all off/quit): ").lower()
        if command == "fan on":
            switch(True, 'fan')
        elif command == "fan off":
            switch(False, 'fan')
        elif command == "light on":
            switch(True, 'light')
        elif command == "light off":
            switch(False, 'light')
        elif command == "all on":
            switch(True, 'both')
        elif command == "all off":
            switch(False, 'both')
        elif command == "quit":
            break
        else:
            print("Invalid command. Please enter 'fan on', 'fan off', 'light on', 'light off', 'all on', 'all off', or 'quit'.")

if __name__ == "__main__":
    main()
