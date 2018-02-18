import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
from MotorCommand import MotorCommand as MotorCommand

def init():
    print('init: setting the GPIO modes')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print('init: set the GPIO modes')

    print('init: setting the GPIO Pin modes')
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    print('init: set the GPIO Pin modes')

    print('init: turning all motors off')
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)
    time.sleep(1)
    print('init: turned all motors off')    

def move_forward():
    print('called move_forward')
    return

def move_backward():
    print('called move_backward')
    return

def stop():
    GPIO.output(7, 0)
    GPIO.output(8, 0)
    GPIO.output(9, 0)
    GPIO.output(10, 0)

def right_wheel(command):
    print("called right_wheel [%s]" % command)
    if(command == MotorCommand.FORWARD):
        GPIO.output(9, 0)
        GPIO.output(10, 1)
    elif(command == MotorCommand.BACKWARD):
        GPIO.output(10, 0)
        GPIO.output(9, 1)
    else:
        GPIO.output(10, 0)
        GPIO.output(9, 0) 

def turn_right():
    print('called turn_right')
    GPIO.output(10, 1)
    time.sleep(0.5)
    GPIO.output(10, 0)
    return

def turn_left():
    print('called turn_left')
    GPIO.output(7, 1)
    time.sleep(0.5)
    GPIO.output(7, 0)
    return
