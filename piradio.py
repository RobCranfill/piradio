# piradio, by cran

import OLEDDisplay
from RadioPlayer import RadioPlayer

import board
import busio
import adafruit_apds9960.apds9960

import time

GESTURE_UP    = 1
GESTURE_DOWN  = 2
GESTURE_LEFT  = 3
GESTURE_RIGHT = 4


if __name__ == "__main__":

    station_data = (
        ("Radio Dublin", "http://uk1.internet-radio.com:8355/stream"),
        ("SLAY Radio",   "http://relay2.slayradio.org:8000"),
        ("KEXP",         "http://live-mp3-128.kexp.org/kexp128.mp3")
    )


    disp = OLEDDisplay.OLEDDisplay(2)
    disp.show_messages(["PiRadio v0.1"])

    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
    sensor.enable_proximity = True
    sensor.enable_gesture = True


    rp = RadioPlayer(disp, station_data)
    rp.start_playing()

    while True:
        gesture = sensor.gesture()
        if gesture != 0:
        #     print('Saw gesture: {0}'.format(gesture))
            if gesture == GESTURE_LEFT:
                rp.prev_station()
                # print("Prev!")
            elif gesture == GESTURE_RIGHT:
                rp.next_station()
                # print("Next!")
            elif gesture == GESTURE_UP:
                print("UP?!")
            elif gesture == GESTURE_DOWN:
                print("DOWN?!")
            else:
                print("What?!")
