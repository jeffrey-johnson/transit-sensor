#/usr/bin/env python
from scapy.all import *
from datetime import datetime
from subprocess import call
import logging
import sys
import json
import time
import threading


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

class MacScanner:
	
    def __init__(self):
	self.interface = "wlan0"
	self.observedclients = []
	self.timeStamps = []
	self.combo = dict()
	self.timeLimit = 0
	"""Writes a dictionary containing the Timestamp and MAC address to a json file"""

    def savetofile(self,d):
	logging.debug("Writing to file")
        with open('data.json', 'w+') as fp:
	    json.dump(d, fp)
	call(["cat", "data.json"])

	""" The sniffmgmt() function is called each time Scapy receives a packet
	(we'll tell Scapy to use this function below with the sniff() function).
	The packet that was sniffed is passed as the function argument, "p"."""
    def sniffmgmt(self,p):
	stamgmtstypes = (0, 2, 4)
	if p.haslayer(Dot11):
	    if p.type == 0 and p.subtype in stamgmtstypes:
		if p.addr2 not in self.observedclients:
		    currentStamp = str(datetime.now()).split('.')[0]
		    self.timeStamps.append(currentStamp)
		    self.observedclients.append(p.addr2)
		    self.combo = dict(zip(self.timeStamps,self.observedclients))


    def startSniffing(self):
	while True:
	    sniff(iface=self.interface, prn=self.sniffmgmt, timeout=30)
	    self.savetofile(self.combo)

    
def main():
    mac = MacScanner()
    print(getattr(mac, 'interface'))
    mac.startSniffing()    

if __name__ == "__main__":
    main()


