# Display wrapper for I2C OLED display.
# robcranfill@gmail.com
#
import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class OLEDDisplay:
    
    def __init__(self) -> None:

        # Create the I2C interface
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.
        #
        self._disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        # Clear display.
        self._disp.fill(0)
        self._disp.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self._width = self._disp.width
        self._height = self._disp.height
        self._image = Image.new("1", (self._width, self._height))

        # Get drawing object to draw on image.
        self._draw = ImageDraw.Draw(self._image)

        # Draw a black filled box to clear the image.
        self._draw.rectangle((0, 0, self._width, self._height), outline=0, fill=0)

        # Load default font.
        self._font = ImageFont.load_default()
        
        # Alternatively load a TTF font.  Make sure the .ttf font file is in the
        # same directory as the python script!
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        #
        self._font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)


        font2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

    def draw_messages(self, s1, s2, s3, s4):

        padding = -2
        top = padding
        bottom = self._height - padding
        x = 0

        # Draw a black filled box to clear the image.
        self._draw.rectangle((0, 0, self._width, self._height), outline=0, fill=0)

        # Write four lines of text.

        self._draw.text((x, top + 0),  s1, font=self._font, fill=255)
        self._draw.text((x, top + 8),  s2, font=self._font, fill=255)
        self._draw.text((x, top + 16), s3, font=self._font, fill=255)
        self._draw.text((x, top + 24), s4, font=self._font, fill=255)

        s5 = "Is there more????"
        self._draw.text((x, top + 32), s5, font=self._font, fill=255)

        # Display image.
        self._disp.image(self._image)
        self._disp.show()


    def clear_display(self):
        self._disp.fill(0)
        self._disp.show()


if __name__ == "__main__":

    d = OLEDDisplay()
    i = 1
    while True:
        d.draw_messages("All classes have a function", 
                        f"And this is {i}", 
                        "Internet radio stations can be found", 
                        "These displays are small, only about 1\" diagonal")
        i = i + 1
        # time.sleep(.1)
