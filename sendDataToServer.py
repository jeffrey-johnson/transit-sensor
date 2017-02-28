import requests
import datetime
import json

timestamp = {"time":"NOW()", "isInitialDetection":1, "deviceID":3, "addressID":5, "routeID":7, "busID":9}
resp = requests.post("http://uaf135131.ddns.uark.edu/api.php/Timestamps", json=timestamp)
if resp.status_code != 200:
	#raise Error('POST TO /timestamps/ {}'.format(resp.status_code))
	print('Failed')
	print(resp.status_code)
else:
	print('Success')
print(str(resp.content))