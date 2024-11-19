from gpiozero import Button
import os
Button(22).wait_for_press()
os.system("sudo poweroff")
