import requests
import datetime
import json
timestamp = {"time":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "isInitialDetection":1, "deviceID":3, "addressID":6, "routeID":7, "busID":9}
timestamp2 = {"time":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "isInitialDetection":1, "deviceID":4, "addressID":6, "routeID":7, "busID":9}
timestamps = [timestamp, timestamp2]
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", json=timestamps)
if resp.status_code != 200:
	#raise Error('POST TO /timestamps/ {}'.format(resp.status_code))
	print('Failed')
	print(resp.status_code)
else:
	print('Success')
print(str(resp.content))