from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import json
import sys
import time
#to do: 
# 1. create switch that shows ip address for ssh
# 2. setup animation (maybe just an mp4) 


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
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

frames = []

for i in animation_routine:
    image = Image.open(i["path"])
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
    frames.append(image.convert('RGB'))
                  
while True:
    for i in frames:
        matrix.SetImage(i)
        time.sleep(4000)

#


#try:
#    print("Press CTRL-C to stop.")
#    while True:
#        time.sleep(100)
#except KeyboardInterrupt:
#    sys.exit(0)
