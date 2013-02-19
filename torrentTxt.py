"""
   __                             __ ______     __ 
  / /_____  _____________  ____  / //_  __/  __/ /_
 / __/ __ \/ ___/ ___/ _ \/ __ \/ __// / | |/_/ __/
/ /_/ /_/ / /  / /  /  __/ / / / /_ / / _>  </ /_  
\__/\____/_/  /_/   \___/_/ /_/\__//_/ /_/|_|\__/  
                                                   
Author: Leland Batey

Description
-----------
torrentTxt monitors a directory and whenever a file is added, you will recieve a txt message (via Twilio) with the name of the file added. torrentTxt is meant to be installed as a cronJob that runs every few minutes.

Requirements:
	Python 2.7
	Twilio tools installed (pip install twilio)
	A Twilio account

"""

from twilio.rest import TwilioRestClient
import subprocess as sub
import os

#+-----+ Twilio Configuration Info +-----+
# You're going to need to paste in your "Account SID" for "account", and your "Auth Token" for "token" 

account = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account, token)
fromNumber = "+xxxxxxxxxxx" # The number that registered to your Twilio account that you want to use to send texts from.
toNumber = "+xxxxxxxxxxx" # The number you want to recieve text messages about the files added. This is probably your cell phone number.
# Note: this can also be a list of phone numbers, so that you can have multiple people receive text messages.

# Enter the full path to the directory that you want monitored
searchDir = "XxXxXxX"
trackingFile = "knownNames.txt" # This is the name of the file that stores the "known" list of files. You can change this name here.


def mainHandler():
	if os.path.isfile(os.getcwd()+"/"+trackingFile): # If the file tracking known filenames exists
		knownNames = open(trackingFile,'r') 
		knownNamesList = knownNames.read()
		knownNames.close()
		knownNamesList = knownNamesList.split('\n')
	else: # If the tracking file doesn't exist, then fake it
		knownNamesList = []

	output = readDir()
	splitLines = output.split('\n')
	filenames = []
	for stuff in splitLines:
		filenames.append(stuff.split('/')[-1]) # Removes everything before the last forwardslash, leaving only each files name with no path.

	diffList = list(set(filenames) - set(knownNamesList)) # Get the files that are not already in list of files we know about

	if len(diffList) > 0:
		buildString = "Files added:\n"

		for stuff in diffList:
			buildString += stuff+"\n"

		buildString = buildString[:120] # Make the buildstring nice and short for use as a text message. It's assumed this will be with a trial account that puts a header on the top of the text message, so it has to accommadate the fewer characters 

		print buildString

		writeString = "" # This will build a string of all the known file names, with no asscociated folder
		for stuff in filenames:
			writeString += stuff+"\n"

		# Write the new list of known files to the "knownFiles.txt" file
		knownNames = open(trackingFile,'w')
		knownNames.write(writeString)
		knownNames.close()

		if isinstance(toNumber,list):
			for j in toNumber:
				client.sms.messages.create(to=j, from_=fromNumber, body=buildString)
		elif isinstance(toNumber,str):
			client.sms.messages.create(to=toNumber, from_=fromNumber, body=buildString)

def readDir(): # Gets the list of all files in the directory that is being monitored
	searchCommand = "find ."
	currentDirContents = sub.Popen(searchCommand,cwd=searchDir,stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
	output, errors = currentDirContents.communicate()

	return output	

# Since this is not currently meant to be a module, I'm skipping all the "__name__" stuff that normally goes in a python program.
mainHandler()