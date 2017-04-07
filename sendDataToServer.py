import requests
from datetime import datetime
import json
from pprint import pprint
import os.path

fileCounter = 0;
while os.path.exists('data'+str(fileCounter)+'.json') & os.path.isfile('data'+str(fileCounter)+'.json'):
	with open('data'+str(fileCounter)+'.json') as data_file:
	    data = json.load(data_file)

	for x in range(0, len(data["timestamps"])):
		thisRecord = {"time":data["timestamps"][x],"address":data["addresses"][x],"deviceID":data["deviceID"]}
		resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", json=thisRecord)#json=thisRecord)
		if resp.status_code != 200:
			print('Failed '+str(x))
			print(resp.status_code)
		else:
			print('Success '+str(x))
		print str(resp.content)

	fileCounter+=1;
#timestamp = {"time":, "isInitialDetection":1, "deviceID":3, "addressID":5, "routeID":7, "busID":9}
#resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", json=timestamp)
#if resp.status_code != 200:
	#raise Error('POST TO /timestamps/ {}'.format(resp.status_code))
#	print('Failed')
#	print(resp.status_code)
#else:
#	print('Success')
#print(str(resp.content))
