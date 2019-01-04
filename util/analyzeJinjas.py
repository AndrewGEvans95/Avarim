#Andrew Evans 1/4/2019
#Extract variabls from jinja templates

import re

def readJinjaFile(fileLocation):
	data = ""
	with open(fileLocation, "r") as myfile:
		data = myfile.read()
	firstPass = re.sub('{%\s*for\s*[a-z]\s*in\s*', '{{ ', data)
	secondPass = re.sub('%}\s*{{\s*[a-z]\s*}}\s*{%\s*endfor\s*%}', ' }}', firstPass)
	return secondPass

def extractVars(fileString):
	fileStrings = fileString.split("\r")
	targetVars = []
	for singleString in fileStrings:
		if "{{" in singleString:
			targetVars.append(singleString)
	return targetVars

def assocVars(fileString):
	allVars = re.findall('{{\s*.+\s*}}', fileString)
	return allVars