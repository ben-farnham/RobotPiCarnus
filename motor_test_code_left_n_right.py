# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

print('Setting the GPIO modes')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print('Finished setting the GPIO modes')

print('Setting the GPIO Pin modes')
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
print('Finished setting the GPIO Pin modes')

print('Turning all motors off')
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)
time.sleep(1)
print('Finshed turning all motors off')

print('Turning the right motor forwards then off')
GPIO.output(9, 0)
GPIO.output(10, 1)
time.sleep(1)
GPIO.output(9, 1)
GPIO.output(10, 0)
time.sleep(1)
GPIO.output(9, 0)
GPIO.output(10, 0)
print('Finished')

time.sleep(1)

print('Turning the left motor forwards then off')
GPIO.output(7, 0)
GPIO.output(8, 1)
time.sleep(1)
GPIO.output(7, 1)
GPIO.output(8, 0)
time.sleep(1)
GPIO.output(7, 0)
GPIO.output(8, 0)
print('Finished')

time.sleep(1)

print('Turning all motors off')
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)
time.sleep(1)
print('Finshed turning all motors off')
