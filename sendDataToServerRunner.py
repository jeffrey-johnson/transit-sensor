import sendDataToServer

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
print sendDataToServer.sendData("http://uaf135131.ddns.uark.edu/api.php/Timestamps","/Users/Jake/documents/transit-sensor/2017-04-18")
=======
>>>>>>> Stashed changes
import socket
REMOTE_SERVER = "http://uaf135131.ddns.uark.edu/api.php/Timestamps"
try:
    socket.create_connection(("www.google.com", 80))
    print str(sendDataToServer.sendData(REMOTE_SERVER, "/home/pi/Documents/GProjects/transit-sensor/2017-04-20/"))
except:
    print "Error connection"
    pass

<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
