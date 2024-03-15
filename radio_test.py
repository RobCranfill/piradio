# piradio, by cran

from mpd import MPDClient
import time


client = MPDClient()
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command, default: None
client.connect("localhost", 6600)


print(f"mpd client version {client.mpd_version}")

url = "http://uk1.internet-radio.com:8355/stream"

client.add(url)

print(f"playing {url}....")
client.play()

time.sleep(10)
client.stop()
print("stopped.")


client.close()                     # send the close command
client.disconnect()                # disconnect from the server

