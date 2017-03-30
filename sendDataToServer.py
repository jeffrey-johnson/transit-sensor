import requests
from datetime import datetime
import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

print(data["timestamps"][0])
for x in range(0, len(data["timestamps"])):
	timestamp = data["timestamps"][x]
	timestampDate = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
	thisRecord = {"time":timestamp,"address":data["addresses"][x],"deviceID":data["deviceID"]}
	resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", data=thisRecord)
	if resp.status_code != 200:
		print('Failed '+str(x))
		print(resp.status_code)
	else:
		print('Success '+str(x))
	print str(resp.content)
	print('\n\n')
#timestamp = {"time":, "isInitialDetection":1, "deviceID":3, "addressID":5, "routeID":7, "busID":9}
#resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", json=timestamp)
#if resp.status_code != 200:
	#raise Error('POST TO /timestamps/ {}'.format(resp.status_code))
#	print('Failed')
#	print(resp.status_code)
#else:
#	print('Success')
#print(str(resp.content))
