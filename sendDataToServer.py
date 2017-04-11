import requests
import datetime
import json

with open('2017-04-11/data2.json') as data_file:
    data = json.load(data_file)

timestamp = {"time":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "isInitialDetection":1, "deviceID":3, "addressID":6, "routeID":7, "busID":9}
timestamp2 = {"time":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "isInitialDetection":1, "deviceID":4, "addressID":6, "routeID":7, "busID":9}
timestamps = [timestamp, timestamp2]

jsonString =  json.dumps(data)
print (jsonString) #this will send nothing 
print data #This will send the last value in a json list
resp = requests.post("http://uaf135131.ddns.uark.edu/test.php", data=(jsonString))
if resp.status_code != 200:
	#raise Error('POST TO /timestamps/ {}'.format(resp.status_code))
	print('Failed')
	print(resp.status_code)
else:
	print('Success')
print(str(resp.content))
print (resp.status_code, resp.text, resp.reason)
