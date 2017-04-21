#!/usr/bin/env python2
import os
import led

nint = "wlan0"
tmp = os.popen("iwconfig " + nint + " | grep Mode").read()

if (tmp.find("Managed") != -1 ):
    tmp = os.popen("bash /home/pi/Documents/GProjects/transit-sensor/startup.sh").read()
    
    
if (tmp.find("Monitor") != -1 ):
    tmp = os.popen("python2.7 /home/pi/Documents/GProjects/transit-sensor/script.py").read()
