import json
from confUtils import *
from datetime import datetime
from enum import Enum

global conf
global story

# Logger ##################################################################
def logThat(level, message):
    for confLevel in conf["log"]:
        if confLevel == level:
            saveInFile(str(datetime.now()) + " -- " + level + " : " + message)



# Read Config ##################################################################
def readConfig(file):
    return loadJsonFromFile(file)


# Load Json Object in File ##################################################################
def loadJsonFromFile(file):
    with open(file, encoding='utf-8') as json_file:
        return json.load(json_file)


class State:
    question = 0
    next
    data =""
    commande=""

    def __init__(self,question,next):
        self.question = question
        self.next=next


class Next(Enum):
    toStart = 1
    toStop = 2
    toWelcomeMessage=3
    toWaitForInput = 4
    toReadQuestion=5
    toDectectInput = 6
    toAnalyseAnswser = 7
    toAnalyseCommand = 8
    toReadIndice=9
    toReadAnswer=10
    toGoto=11



conf = readConfig('conf/config.json')
story = readConfig('conf/story.json')