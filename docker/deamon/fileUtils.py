

# Save Json Object in File ##################################################################
def saveJsonInFile(file, jsonObject):
    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(jsonObject, json_file, sort_keys=True, indent=2)
        json_file.close

# Load Json Object in File ##################################################################
def loadJsonFromFile(file):
    with open(file, encoding='utf-8') as json_file:
        return json.load(json_file)


 # Save  Object in File ##################################################################
def saveInFile(file, object):
    with open(file, 'a', encoding='utf-8') as open_file:
        open_file.write(str(object))
        open_file.close

# List File in Directory ##################################################################
def listFile(pattern, path):
    resultFiles = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                resultFiles.append(os.path.join(root, name))
    return resultFiles

def makeDirectoryIfNotExist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)