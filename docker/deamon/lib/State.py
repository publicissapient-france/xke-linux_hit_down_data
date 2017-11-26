from enum import Enum
class State(Enum):
    toStart = 1
    toStop = 2
    toWelcomeMessage = 3
    toWaitForInput = 4
    toQuestion = 5
    toDectectInput = 6
    toAnalyseAnswser = 7
    toAnalyseCommand = 8
    toIndice = 9
    toAnswer = 10
    toGoto = 11