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
	self.combo = dict()
	self.timeLimit = 0
        self.ourMacs = {'ac:0d:1b:d1:92:22':'Caleb',
                        'ac:0d:1b:f5:f6:8a':'Jeff',
                        '10:68:3f:3b:cc:c4':'Vitaly',
                        'ec:9b:f3:77:8a:d2':'Jake'}

    def initLogger(self):
        # create debug file handler and set level to debug
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG,
            format='[%(levelname)s] (%(threadName)-10s) %(message)s',
            )
        handler = logging.FileHandler(os.path.join('/home/pi/Documents/GProjects/transit-sensor', "all.log"),"w")
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
	
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
                    for key, value in self.ourMacs.items():
                        if p.addr2 == key:
                            logging.debug(p.addr2 + " - "+ value)
                    currentStamp = str(datetime.now()).split('.')[0]
		    logging.debug(currentStamp + " " + p.addr2)
                    self.timeStamps.append(currentStamp)
		    self.observedclients.append(p.addr2)
		    self.combo = dict(zip(self.timeStamps,self.observedclients))

    def restart(self):
        self.observedclients = []
        self.timeStamps = []
        self.combo = dict()
        print(self.observedclients,self.timeStamps,self.combo)
        logging.debug("Sleeping")
        time.sleep(60)
        logging.debug("Waking up")

    def startSniffing(self):
	while True:
	    sniff(iface=self.interface, prn=self.sniffmgmt, timeout=69)
	    self.savetofile(self.combo)
            self.restart()
            logging.debug("Starting sniffing again")

    
def main():
    mac = MacScanner()
    mac.initLogger()
    mac.startSniffing()    

if __name__ == "__main__":
    main()


