# RadioPlayer class

from mpd import MPDClient
import time


class RadioPlayer:

    """Station list is tuple of (station name, station URL)"""
    def __init__(self, station_list):

        self._station_list = station_list

        self._client = MPDClient()
        self._client.timeout = 10                # network timeout in seconds (floats allowed), default: None
        self._client.idletimeout = None          # timeout for fetching the result of the idle command, default: None
        self._client.connect("localhost", 6600)

        for s in station_list:
            self._client.add(s[1])
        self._selected_station_index = 0


    def __del__(self):
        self._client.stop()
        self._client.close()
        self._client.disconnect()
        print("RadioPlayer destroyed.")

    def start_playing(self):
        print("RadioPlayer starting.")
        self._client.play()

    def stop_playing(self):
        print("RadioPlayer stopping.")
        self._client.stop()

    def next_station(self):
        '''Start playing the next station in the station list.'''
        self._selected_station_index = self._selected_station_index + 1
        if self._selected_station_index == len(self._station_list):
            self._selected_station_index = 0
        
        self._client.next()

    def prev_station(self):
        '''Start playing the previous station in the station list.'''
        self._selected_station_index = self._selected_station_index - 1
        if self._selected_station_index < 0:
            self._selected_station_index = len(self._station_list) - 1
        self._client.previous()

    def get_current_song_title(self):
        cs = self._client.currentsong()
        if cs is None:
            print("Song is none!")
            return "(None)"
        print(f"self._client.currentsong(): {self._client.currentsong()}")
        title = cs.get("title")
        if title is None:
            print("title is none!")
            title = "(None)"
        return title

    def get_current_station_name(self):
        return "Station X"

    def get_status(self):
        return self._client.status()

    def volume_up(self):
        print("Volume up?")

    def volume_down(self):
        print("Volume down?")

    
# for testing
if __name__ == "__main__":

    rp = RadioPlayer(["http://uk1.internet-radio.com:8355/stream",
                      "http://relay2.slayradio.org:8000"])

    rp.start_playing()
    time.sleep(10)
    rp.stop_playing()


