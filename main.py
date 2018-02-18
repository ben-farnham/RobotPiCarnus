import cwiid
import time
import motor.controller
from motor.MotorCommand import MotorCommand as MotorCommand

button_delay = 0.1

print("Please press buttons 1 + 2 on your Wiimote now ...")
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print("Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!")
  quit()

motor.controller.init()

print("Wiimote connection established!\nGo ahead and press some buttons\nPress PLUS and MINUS together to disconnect and quit.\n")

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print('\nClosing connection ...')
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    print('Left pressed')
    motor.controller.turn_left()
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print('Right pressed')
    motor.controller.right_wheel(MotorCommand.STOP)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print('Up pressed')
    motor.controller.move_forward()
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print('Down pressed')
    motor.controller.move_backward()
    time.sleep(button_delay)
