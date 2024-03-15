import board
import busio
import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True

sensor.enable_gesture = True

gesture = sensor.gesture()
while gesture == 0:
    gesture = sensor.gesture()
print('Saw gesture: {0}'.format(gesture))

