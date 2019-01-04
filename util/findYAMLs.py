#Andrew Evans 1/4/2019
#Traverses a given root directory to find yaml files
#Directory defined in config.ini file

import os
import ConfigParser

#Get configs
config = ConfigParser.ConfigParser()
config.read('../config/config.ini')

rootDir = config.get("GLOBAL","yamlFilesDir")

#Now traverse given rootDir to find all jinja Templates

print "Scanning project..."

jinjaTemplates = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
	for fname in fileList:
		if ".yml" in fname:
			jinjaTemplates.append(dirName+"/"+fname)