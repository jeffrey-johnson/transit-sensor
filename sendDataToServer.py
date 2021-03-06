import requests
from datetime import datetime
import json
import os.path
#address is URL of the api the data is being sent to
#pathToJSONDirectory is the full path to the folder which the JSON files are stored in
def sendData(serverAddress, pathToJSONDirectory):
	fileCounter = 0
	numRecsSentSuccessfully = 0
	if pathToJSONDirectory[-1] != '/':
			pathToJSONDirectory = pathToJSONDirectory + '/'
	while os.path.exists(pathToJSONDirectory+str(fileCounter)+'.json') & os.path.isfile(pathToJSONDirectory+str(fileCounter)+'.json'):
		with open(pathToJSONDirectory + str(fileCounter)+'.json') as data_file:
		    data = json.load(data_file)

		for x in range(0, len(data["Time Stamps"])):
			thisRecord = {"time":data["Time Stamps"][x],"address":data["Addresses"][x],"deviceID":data["DEVICE_ID"]}
			resp = requests.post(serverAddress, json=thisRecord)#json=thisRecord)
			if resp.status_code == 200:
				numRecsSentSuccessfully+=1
		fileCounter+=1
	return numRecsSentSuccessfully