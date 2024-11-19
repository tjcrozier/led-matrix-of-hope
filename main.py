from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import json
import sys
import time
#to do: 
# 1. set up auto network connection (prob need euid for this)
# 2. solder button for turning it off
# 3. designing a 3d printed plate to mount the pi and potentially act as a stand
# 4. get qr code for linktree/discord/whatever and making headings for them to pop up
# 5. SET UP SYSTEMD AUTO START

#stretch goals:
# 1. transitions (fading, sliding, etc)
# 2. video support?
# 3. implement fast api or similar for easier access
# 4. extend routine.json for transition data/other?




if len(sys.argv) < 2:
    sys.exit("Require a .json file argument")
else:
    file_path = sys.argv[1]
with open(file_path, "r") as file:
    animation_routine = json.load(file)
    file.close()

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.gpio_slowdown = 4
options.brightness=50
options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

frames = []

for i in animation_routine['frames']:
    image = Image.open(i['path'])
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.NEAREST)
    frames.append({'image' : image.convert('RGB'), 'time' : int(i['time'])})
                  
while True:
    for i in frames:
        matrix.SetImage(i['image'])
        time.sleep(i['time'])

#


#try:
#    print("Press CTRL-C to stop.")
#    while True:
#        time.sleep(100)
#except KeyboardInterrupt:
#    sys.exit(0)
