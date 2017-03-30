#/usr/bin/env python
from scapy.all import *
from datetime import datetime
from subprocess import call
import logging
import sys
import json
import time
import threading



class MacScanner:
	
    def __init__(self):
	self.interface = "wlan0"
	self.observedclients = []
	self.timeStamps = []
        self.combo = {"Time Stamps":[], "Addresses":[]} 
        self.timeLimit = 0
	self.dictionary =dict()	    
        self.DEVICE_ID = 1

    def initLogger(self):
        # create debug file handler and set level to debug
        logging.basicConfig(filename='all.log',level=logging.DEBUG)

    """Writes a dictionary containing the Timestamp and MAC address to a json file"""
    def savetofile(self,d):
	logging.debug("Writing to file")
        with open('data.json', 'w+') as fp:
	    json.dump(d, fp,sort_keys=True)
	call(["cat", "data.json"])

    """Takes any given packet that scapy sniffs and filters it down to a macaddress that has not been seen yet
       It then appends a timestamp to the address and saves it to a dictionary."""
    def sniffmgmt(self,p):
	stamgmtstypes = (0, 2, 4)
	if p.haslayer(Dot11):
	    if p.type == 0 and p.subtype in stamgmtstypes:
		if p.addr2 not in self.observedclients:
                    currentStamp = str(datetime.now()).split('.')[0]
                    logging.info(p.addr2 + " " + currentStamp)
		    self.combo['Time Stamps'].append(currentStamp)
		    self.combo['Addresses'].append(p.addr2)
		    self.dictionary = dict(self.combo)

    def restart(self, timeLimit):
        self.observedclients = []
        self.timeStamps = []
        self.combo = dict()
        logging.debug("Sleeping")
        time.sleep(timeLimit)
        logging.debug("Waking up")

    def startSniffing(self,timeLimit):
	while True:
	    sniff(iface=self.interface, prn=self.sniffmgmt, timeout=timeLimit)
	    self.savetofile(self.combo)
            self.restart(timeLimit)
            logging.debug("Starting sniffing again")
    
def main(timeLimit = 60):
    mac = MacScanner()
    mac.initLogger()
    mac.startSniffing(timeLimit)

if __name__ == "__main__":
    main()


