import requests
from datetime import datetime
import json
import os.path
#address is URL of the api the data is being sent to
#pathToJSONDirectory is the full path to the folder which the JSON files are stored in
def sendData(serverAddress, pathToJSONDirectory):
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