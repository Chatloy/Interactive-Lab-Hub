import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()



while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    cur_time = time.strftime("%m/%d/%Y %H:%M:%S") 
    y = top
    draw.text((x, y), cur_time, font=font, fill="#FFFFFF")
    print (time.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    print("\r", end="", flush=True)

    month= int(time.strftime('%m'))
    day = int(time.strftime('%d'))
    hr = int(time.strftime('%H'))
    if day==20:
        msg = 'anniversary'
    elif month==9 and day==21:
        msg = 'Happy Mid-Autumn Festival!'
    elif month==12 and day==25:
        msg = 'Merry Christmas!'
    else:
        msg='Just a normal day!'

    if  buttonA.value and not buttonB.value:  
        y = y + font.getsize(cur_time)[1]
        draw.text((x, y), msg, font=font, fill="#FF00FF")       
      
    
    if hr > 22 or hr < 1:
        dayTimer = 'Time to sleep. Good Night!'
    elif hr==8:
        dayTimer = 'Time to get up.Good Morning!'
    elif hr>8 and hr<23:
        dayTimer='Time to study.You are doing a great job'
    else:
        dayTimer='Just sleeping!'
        

    if not buttonA.value and buttonB.value:
        y = y + font.getsize(msg)[1]
        draw.text((x, y), dayTimer, font=font, fill="#0000FF")
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
