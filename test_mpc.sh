#!/bin/bash
# test what mpc commands I need to use
# cf https://www.musicpd.org/doc/mpc/html/

# clear the queue
#
mpc clear

# add URLs to the queue
#
mpc add "http://uk1.internet-radio.com:8355/stream"
# mpc add "http://uk7.internet-radio.com:8000/"
mpc add "http://stream.rockantenne.de/90er-rock/stream/mp3"
# mpc add "http://relay2.slayradio.org:8000"
mpc add "https://stream.starfm.de/berlin/mp3-192/"

# mpc stats # this is never useful, seeing as we don't have a backing database
mpc status

# echo -e "\n**** Playing for 10 seconds....\n"
# mpc play
# sleep 10


for foo in 1 2 3 4
do
    echo -e "\nPlaying # $foo...."
	mpc play
	sleep 10
    mpc next
done
mpc stop
exit 0


echo -e "\n**** Playing for 4 seconds\n"
mpc clear
mpc add "http://stream.rockantenne.de/90er-rock/stream/mp3"
mpc play
sleep 4

echo -e "\n**** Playing for 4 seconds\n"
mpc clear
mpc add "http://relay2.slayradio.org:8000"
mpc play
sleep 4

echo -e "\n**** Playing for 4 seconds\n"
mpc clear
mpc add "https://stream.starfm.de/berlin/mp3-192/"
mpc play
sleep 4


mpc stop
echo "Done"
