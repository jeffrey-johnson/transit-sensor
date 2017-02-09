#! /bin/bash
rfkill unblock wifi
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up
