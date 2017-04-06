#! /bin/bash
echo pi | sudo -S echo -n 2>/dev/random 1>/dev/random
sudo rfkill unblock wifi
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
sudo ifconfig wlan0 up
