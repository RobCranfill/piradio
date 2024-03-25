# RadioPlayer class

from mpd import MPDClient
import time


class RadioPlayer:

    """Station list just station URLs"""
    def __init__(self, station_list):

        self._client = MPDClient()
        self._client.timeout = 10                # network timeout in seconds (floats allowed), default: None
        self._client.idletimeout = None          # timeout for fetching the result of the idle command, default: None
        self._client.connect("localhost", 6600)

        # This client just talks to the server and builds a playlist there. 
        # We need to clear the current playlist, then add the URLs to the playlist.
        #
        self._client.clear()
        for url in station_list:
            self._client.add(url)

        self._debug = False


    def __del__(self):
        self._client.stop()
        self._client.close()
        self._client.disconnect()
        print("RadioPlayer destroyed.")

    def set_debug(self, debug):
        self._debug = debug

    def check_stations(self):
        print(" check_stations -------------------------")
        for p in self._client.listplaylists():
            print(f"Playlist: {p}")
        print(" ----------------------------------------")

    def start_playing(self):
        print("RadioPlayer starting.")
        self._client.play()

    def stop_playing(self):
        print("RadioPlayer stopping.")
        self._client.stop()

    def next_station(self):
        '''Start playing the next station in the station list.'''

        try:
            self._client.next()
        except:
            print("\n *** next_station timed out!\n")


    def prev_station(self):
        '''Start playing the previous station in the station list.'''
        self._client.previous()

    def get_current_song_title(self):

        cs = None
        try:
            cs = self._client.currentsong()
        except:
            print("Timed out!")
            return "Timeout!"

        print(f"get_current_song_title: currentsong(): {self._client.currentsong()}")
        if cs is None:
            print("Song is none!")
            return "(None)"
        title = cs.get("title")
        if title is None:
            print("title is none!")
            title = "(None)"
        return title

    def get_current_station_name(self):

        cs = None
        try:
            cs = self._client.currentsong()
        except:
            print("Timed out!")
            return "Timeout!"

        # print(f"get_current_station_name: currentsong(): {self._client.currentsong()}")
        if cs is None:
            print("Song is none!")
            return "(None)"
        name = cs.get("name")
        if name is None:
            print("name is none!")
            name = "(None)"
        return name

    def get_status(self):
        return self._client.status()

    """ Not so useful? """
    def get_stats(self):
        return self._client.stats()

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

