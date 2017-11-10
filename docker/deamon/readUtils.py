
from confUtils import *

def readWelcomeMessage():
    print(story["welcome"])

def readQuestion(question):
    logThat("GAME", "Start Question :"+ str(question))
    print(story["quizz"][str(question)]["storybegin"])
    print(story["quizz"][str(question)]["question"])



def readAnwser(question):
    logThat("GAME", "Answer Question :" + str(question))
    print(story["quizz"][str(question)]["answer"])
    print(story["quizz"][str(question)]["storyEnd"])



def readIndice(question):
    logThat("GAME", "Indice Question :" + str(question))
    print(story["quizz"][str(question)]["indice"])


