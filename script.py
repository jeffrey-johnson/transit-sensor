#!/usr/bin/env python
# The previous line ensures that this script is run under the context
# of the Python interpreter. Next, import the Scapy functions:
from scapy.all import *
from datetime import datetime
import json
import time
# Define the interface name that we will be sniffing from, you ca
# change this if needed.
interface = "wlan0"
# Next, declare a Python list to keep track of client MAC addresses
# that we have already seen so we only print the address once per client.
observedclients = []
timeStamps = []
combo = dict()
timeLimit = 0
"""Writes a dictionary containing the Timestamp and MAC address to a json file"""
def savetofile(d):
    with open('data.json', 'w+') as fp:
        json.dump(d, fp)

""" The sniffmgmt() function is called each time Scapy receives a packet
(we'll tell Scapy to use this function below with the sniff() function).
The packet that was sniffed is passed as the function argument, "p"."""
def sniffmgmt(p):
    # Define our tuple (an immutable list) of the 3 management frame
    # subtypes sent exclusively by clients. I got this list from Wireshark.
    stamgmtstypes = (0, 2, 4)
    start = end = time.time()
    print (end-start)
    print timeLimit, "starting loop"
    while((end - start) < timeLimit):
        #time.sleep(100)
        #if (int(end-start))%2==0:
        #    sys.stdout.write('.')
        #else: 
        #    sys.stdout.write('+')
        ## print ("time so far: ", (end - start) )
        # Make sure the packet has the Scapy Dot11 layer present
        if p.haslayer(Dot11):
            # Check to make sure this is a management frame (type=0) and that
            print "Has Dot11 Layer"
# the subtype is one of our management frame subtypes indicating a
            # a wireless client
            if p.type == 0 and p.subtype in stamgmtstypes:
                # We only want to print the MAC address of the client if it
                # hasn't already been observed. Check our list and if the
                # client address isn't present, print the address and then add
                print "p type is 0 and has the subtype"
                # it to our list.
                #if p.addr2 not in observedclients:
                if p.addr2 not in observedclients:
                    currentStamp = str(datetime.now()).split('.')[0]
                    timeStamps.append(currentStamp)
                    print p.addr2, currentStamp
                    observedclients.append(p.addr2)
                combo = dict(zip(timeStamps,observedclients))
                print combo
                savetofile(combo)


        end = time.time() 
# With the sniffmgmt() function complete, we can invoke the Scapy sniff()
# function, pointing to the monitor mode interface, and telling Scapy to call
# the sniffmgmt() function for each packet received. Easy!

def main(time):
    sniff(iface=interface, prn=sniffmgmt)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        timeLimit = sys.argv[1]
    else:
        timeLimit = 60
    main(timeLimit)


