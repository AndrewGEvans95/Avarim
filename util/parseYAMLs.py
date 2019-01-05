import yaml
import collections

def getYamlKeys(yamlFile):
	print "============" + yamlFile
	for key in flatten(yaml.safe_load(open(yamlFile))):
		print key
	print "\n\n\n"


def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)