#! /bin/bash
echo pi | sudo -S echo -n 2>/dev/random 1>/dev/random
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode managed
sudo ifconfig wlan0 up
