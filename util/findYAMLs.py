#Andrew Evans 1/4/2019
#Traverses a given root directory to find yaml files
#Directory defined in config.ini file

import os
import ConfigParser
import parseYAMLs

#Get configs
config = ConfigParser.ConfigParser()
config.read('../config/config.ini')

rootDir = config.get("GLOBAL","yamlFilesDir")
ignoreFile = config.get("GLOBAL", "ignoreFile")

#Now traverse given rootDir to find all jinja Templates

print "Gathering YAML files..."

#Must assume that all files are yaml files
yamlFiles = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
	for fname in fileList:
		if ".pem" not in fname:
			if ".txt" not in fname:
				if "inventory" not in fname:
					yamlFiles.append(dirName+"/"+fname)
print yamlFiles


for yamlFile in yamlFiles:
	parseYAMLs.getYamlKeys(yamlFile)
	reload(parseYAMLs)