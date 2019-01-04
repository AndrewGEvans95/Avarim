#Andrew Evans 1/2/2019
#Traverses a given root directory to find Jinja templates
#Directory defined in config.ini file

import os
import ConfigParser
import analyzeJinjas

#Get configs
config = ConfigParser.ConfigParser()
config.read('../config/config.ini')

rootDir = config.get("GLOBAL","jinjaTemplateDirectory")

#Now traverse given rootDir to find all jinja Templates

print "Scanning project..."

jinjaTemplates = []
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
	for fname in fileList:
		if ".j2" in fname:
			jinjaTemplates.append(dirName+"/"+fname)

print "Found the following templates: "
print jinjaTemplates

for template in jinjaTemplates:
	for var in analyzeJinjas.assocVars(analyzeJinjas.readJinjaFile(template)):
		print template + " <- " + var