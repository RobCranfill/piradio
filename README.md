# piradio
Internet radio on a RPiZeroW?


# Questions
 * Update Pi to Bookworm?
 * <strike>WHY CAN'T I SSH VIA TERMIUS????</strike>
   * pizerow1 is hostname

# RPi prep
 * As per https://raspberrypi.stackexchange.com/questions/76188/how-to-make-pcm5102-dac-work-on-raspberry-pi-zerow
 * and https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/

 Note that `dtoverlay=hifiberry-dac` is correct.


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