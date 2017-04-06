#/usr/bin/env python
from scapy.all import *
from datetime import datetime
from subprocess import call
import logging
import sys
import json
import time
import os

class MacScanner:
	
    def __init__(self):
	self.interface = "wlan0"
	self.observedclients = []
	self.timeStamps = []
        self.combo = {"DEVICE_ID":1,"Time Stamps":[], "Addresses":[]} 
        self.timeLimit = 0
	self.dictionary =dict()

    def initLogger(self):
        # create debug file handler and set level to debug
        logging.basicConfig(filename='all.log',level=logging.DEBUG)

    """Writes a dictionary containing the Timestamp and MAC address to a json file"""
    def savetofile(self,d):
        fileCounter = 0
        filetime = str(datetime.now())
        if not(os.path.exists(filetime.split()[0])):
            os.makedirs(filetime.split()[0])
        logging.debug("Writing to file")
        for root, dirs, files in os.walk(filetime.split()[0]):
            if not (files):
		pass
	    else:
		print files
		#fileCounter = int(files[0].split('.')[0][4:]) + 1
		fileCounter = int(files[-1].split('.')[0][4:]) + 1
	print fileCounter
        with open(os.path.join(filetime.split()[0], 'data'+str(fileCounter)+'.json'), 'w') as fp:
            json.dump(d, fp,sort_keys=False)
	call(["ls", filetime.split()[0]])

    """Takes any given packet that scapy sniffs and filters it down to a macaddress that has not been seen yet
       It then appends a timestamp to the address and saves it to a dictionary."""
    def sniffmgmt(self,p):
	stamgmtstypes = (0, 2, 4)
	if p.haslayer(Dot11):
	    if p.type == 0 and p.subtype in stamgmtstypes:
		if p.addr2 not in self.observedclients:
            	    print p
	            """change timestamp format to have no special characters"""
                    currentStamp = datetime.now().strftime('%Y%m%d%H%M%S')
		    print(p.addr2)
                    logging.info(p.addr2 + " " + currentStamp)
		    self.combo["Time Stamps"].append(str(currentStamp))
		    self.combo["Addresses"].append(p.addr2)
		    self.dictionary = dict(self.combo)

    def restart(self, timeLimit):
        self.observedclients = []
        self.timeStamps = []
        logging.debug("Sleeping")
        time.sleep(timeLimit)
        logging.debug("Waking up")

    def startSniffing(self,timeLimit):
	while True:
	    sniff(iface=self.interface, prn=self.sniffmgmt, timeout=timeLimit)
	    self.savetofile(self.dictionary)
            self.restart(timeLimit)
            logging.debug("Starting sniffing again")
    
def main(timeLimit = 20):
    mac = MacScanner()
    mac.initLogger()
    mac.startSniffing(timeLimit)

if __name__ == "__main__":
    main()


