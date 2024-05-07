# piradio
Internet radio on a RPiZeroW!


# New Minimum Viable Product - May '24
 * Configurable
   * Via Adafruit IoT?
 * Workaround for missing metadata
   * Just show canned station name; more if available
 * Using speaker and amp - NOT PCM5102 ???
   * So we need to reconfigure Linux ????


# Open Questions
 * (Also see 'problems' below)


# Testbed
* PiZero1W - PiZero W v1.1 - sufficient?
* Raspian 'Bullseye'
  * Update to Bookworm?
* Generic PCM5102 PCM module
* Mini OLED display
  * How to coexist with I2C bus?
  * Soldered I2C pigtail to top of OLED
* APDS-9960 gesture contoller


# RPi prep
 * As per https://raspberrypi.stackexchange.com/questions/76188/how-to-make-pcm5102-dac-work-on-raspberry-pi-zerow
 * and https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/

 Note that `dtoverlay=hifiberry-dac` is correct.


## Install
* install mpd, mpc
* Install Adafruit CircuitPython libraries ("Blinka")
* pip3 install adafruit-circuitpython-ssd1306


## Prep
* config.txt
<pre>
...
# Enable audio (loads snd_bcm2835)
# cran: removed: dtparam=audio=on
...
# Enable DRM VC4 V3D driver
# cran: modified
dtoverlay=vc4-kms-v3d,noaudio
...
# cran: added
dtoverlay=hifiberry-dac
</pre>

## Check
<pre>rob@pizero2dub:~ $ aplay -l
	**** List of PLAYBACK Hardware Devices ****
	card 0: sndrpihifiberry [snd_rpi_hifiberry_dac], device 0: HifiBerry DAC HiFi pcm5102a-hifi-0 [HifiBerry DAC HiFi pcm5102a-hifi-0]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
</pre>	

## Test
<pre>rob@pizerow1:/boot $ mpc
volume: n/a   repeat: off   random: off   single: off   consume: off
rob@pizerow1:/boot $ history | grep mpc

rob@pizerow1:/boot $ mpc add http://uk1.internet-radio.com:8355/stream

rob@pizerow1:/boot $ mpc play
The Zone - Dublin: Clairo - Hello? (feat. Rejjie Snow)
[playing] #1/2   0:00/0:00 (0%)
volume: n/a   repeat: off   random: off   single: off   consume: off
rob@pizerow1:/boot $ 
</pre>

## Problems
* Network latency
  * Slow to start play
    - Intrinsic to mpc/mpd - happens from command line too
  * Some streams time out
    - Again, intrinsic to protocol/situation.
  * Upshot is that we can't expect station switching to happen instantaneously.

### Problems RESOLVED
* Audio out is noisy - sensitive to touch
  * A result of breaboarding? Yes! Fixed.
* Volume won't change
<pre>
rob@pizerow1:/boot $ mpc volume 50
The Zone - Dublin: Claire Rosinkranz - Screw Time
[playing] #1/2   4:35/0:00 (0%)
volume:100%   repeat: off   random: off   single: off   consume: off
</pre>

** Fixed as per https://forums.raspberrypi.com/viewtopic.php?t=150505
* Add an ALSA mixer to /etc/mpd.conf:
<pre>
# add software mixer - NOT "bit perfect", fine
#
audio_output {
    type                "alsa"
    name                "My ALSA mixer"
#    device             "hw:0,0"        # optional
    mixer_type      "software"  # optional
#    mixer_device       "default"       # optional
#    mixer_control      "PCM"           # optional
#    mixer_index        "0"             # optional
}
</pre>
<pre>
rob@pizerow1:/etc $ mpc volume 75
The Zone - Dublin: The Vanns - Harder To Find
[playing] #2/2   0:41/0:00 (0%)
volume: 75%   repeat: off   random: off   single: off   consume: off
</pre>



 # Resources
  * https://funprojects.blog/tag/internet-radio/


# Software to install
* mpd, mpc


# Stations
 * from https://www.internet-radio.com/
<pre>
    [playlist]
    NumberOfEntries=1
    File1=http://uk1.internet-radio.com:8355/stream
    Title1=The Zone - Dublin
    Length1=-1
    Version=2
</pre>

## Notes re mpc & mpd

* Maybe need to set timeout for some (like 'STAR FM MAXIMUM ROCK Berlin')

  MPD error: Failed to decode http://relay2.slayradio.org:8000; CURL failed: Connection timed out after 10010 milliseconds
