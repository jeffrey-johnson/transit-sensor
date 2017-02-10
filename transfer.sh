ifconfig wlan0 down
iwconfig wlan0 mode managed
ifconfig wlan0 up

# this line do not work nmcli not exists
# nmcli d connect Cisco04011
