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

        # "http://64.78.234.173:8534", # KRIZ xtian crap, Seattle
        # "http://relay2.slayradio.org:8000", # often dead?
        # "https://stream.starfm.de/berlin/mp3-192/",

        "http://uk1.internet-radio.com:8355/stream",
        "http://108.178.13.122:8147", # Radio Punjab Seattle

        "http://uk7.internet-radio.com:8000/",
        "http://stream.rockantenne.de/90er-rock/stream/mp3"
    )


    disp = OLEDDisplay.OLEDDisplay(2)
    disp.show_messages(["PiRadio v0.1", "Ready"])

    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
    sensor.enable_proximity = True # must be True for gestures, too
    sensor.enable_gesture = True


    rp = RadioPlayer(station_data)
    rp.set_debug(True)

    rp.check_stations()
    print(f"status: {rp.get_status()}")

    # rp.start_playing()

    station_changed = False

    while True:
        gesture = sensor.gesture()
        
        if gesture != 0:

        #     print('Saw gesture: {0}'.format(gesture))
            if gesture == GESTURE_LEFT:
                rp.prev_station()
                station_changed = True

            elif gesture == GESTURE_RIGHT:
                rp.next_station()
                station_changed = True

            elif gesture == GESTURE_UP:
                print("UP?!")
                rp.start_playing()
                station_changed = True

            elif gesture == GESTURE_DOWN:
                print("DOWN?!")
                rp.stop_playing()

            else:
                print("Unknown gesture!")

            # status = rp.get_status()
            # print(f"status is now {status}")
            # # disp.show_messages((sta, song))

            if station_changed:
                sta  = rp.get_current_station_name()
                song = rp.get_current_song_title()
                print(f"Station is now '{sta}', song '{song}'")
                disp.show_messages((sta, song))

