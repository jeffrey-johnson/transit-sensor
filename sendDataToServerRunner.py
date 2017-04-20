import sendDataToServer

import socket
REMOTE_SERVER = "http://uaf135131.ddns.uark.edu/api.php/Timestamps"
try:
    socket.create_connection(("www.google.com", 80))
    print str(sendDataToServer.sendData(REMOTE_SERVER, "/home/pi/Documents/GProjects/transit-sensor/2017-04-20/"))
except:
    print "Error connection"
    pass

