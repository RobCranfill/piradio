# more or less from https://python-mpd2.readthedocs.io/en/latest/topics/getting-started.html

from mpd import MPDClient
client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("localhost", 6600)  # connect to localhost:6600
print(f"mpd client version {client.mpd_version}")          # print the MPD version
print(f"found: {client.find('any', 'house')}") # print result of the command "find any house"
client.close()                     # send the close command
client.disconnect()                # disconnect from the server
