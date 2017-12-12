from datetime import datetime
from lib.file import *

global conf
global story


# Logger ##################################################################
def logThat(level, message):
    for confLevel in conf["levels"]:
        if confLevel == level:
            #print("{} -- {} : {}".format(datetime.now(), level, message))
            saveInFile(conf["fileLog"], "{} -- {} : {}\n".format(datetime.now(), level, message))


# Read Config ##################################################################
def readConfig(file):
    return loadJsonFromFile(file)


# Load Json Object in File ##################################################################
def loadJsonFromFile(file):
    with open(file, encoding='utf-8') as json_file:
        return json.load(json_file)


conf = readConfig('conf/config.json')
story = readConfig('conf/story.json')
