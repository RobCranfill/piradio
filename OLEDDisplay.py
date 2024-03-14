# Display wrapper for I2C OLED display.
# robcranfill@gmail.com
#
# TODO: destructor? clear screen
#
import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class OLEDDisplay:
    
    def __init__(self, n_lines) -> None:

        # font_size  8 -> 4 lines of text
        # font_size 11 -> 3 lines of text
        # font_size 17 -> 2 lines of text
        # font_size 36 -> 1 lines of text - and about 8 characters! :-(

        font_sizes = [36, 17, 11, 8]
        self._font_size = font_sizes[n_lines-1]
    
        # Create the I2C interface
        i2c = busio.I2C(SCL, SDA)

        # Create the SSD1306 OLED class.
        # The first two parameters are the pixel width and pixel height.
        #
        self._disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        # Clear the display
        self._disp.fill(0)
        self._disp.show()

        # Create blank image for drawing.
        # Image mode '1' is 1-bit color.
        #
        self._width = self._disp.width
        self._height = self._disp.height
        self._image = Image.new("1", (self._width, self._height))

        # Get drawing object to draw on image.
        self._draw = ImageDraw.Draw(self._image)

        # # Draw a black filled box to clear the image.
        ### erm, didn't we already do this?
        # self._draw.rectangle((0, 0, self._width, self._height), outline=0, fill=0)

        # Load default font.
        # self._font = ImageFont.load_default()
        
        # Alternatively, load a TTF font.
        # Some other nice fonts to try: http://www.dafont.com/bitmap.php
        #
        self._font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', self._font_size)


    # def clear_display(self):
    #     self._disp.fill(0)
    #     self._disp.show()


    def __del__(self):
        # clear_display(self)
        self._disp.fill(0)
        self._disp.show()


    def draw_messages(self, msg_list):

        padding = -2
        top = padding
        bottom = self._height - padding
        x = 0

        # Draw a black filled box to clear the image.
        self._draw.rectangle((0, 0, self._width, self._height), outline=0, fill=0)

        # Write the text.
        #
        for i in range(len(msg_list)):
            self._draw.text((x, top + i*self._font_size), msg_list[i], font=self._font, fill=255)

        # Display image.
        self._disp.image(self._image)
        self._disp.show()



# Example of how to use this class
#
if __name__ == "__main__":

    d = OLEDDisplay(3)
    i = 1
    while True:
        d.draw_messages([
                "All classes have a function", 
               f"And this is #{i}", 
                "Internet radio stations can be found", 
                "These displays are small, only about 1\" diagonal"
                ])
        i = i + 1
        # time.sleep(.1)
