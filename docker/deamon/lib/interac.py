import subprocess
import time

from lib.conf import *


def readWelcomeMessage(context):
    logThat("GAME", " Welcome Message :".format(context.question))
    response = []
    for message in story["welcome"]:
        response.append(message)
    return response


def readQuestion(context):
    logThat("GAME", " Start Question :{}".format(context.question))
    response = []
    if story["quizz"][context.question]["storybegin"]:
        response.append(story["quizz"][context.question]["storybegin"])
    if story["quizz"][context.question]["question"]:
        response.append(story["quizz"][context.question]["question"])
    return response


def readAnwser(context):
    logThat("GAME", " Answer Question : {}".format(context.question))
    response = []
    context.indice = 0
    if story["quizz"][context.question]["answer"]:
        response.append(story["quizz"][context.question]["answer"])
    if story["quizz"][context.question]["storyEnd"]:
        response.append(story["quizz"][context.question]["storyEnd"])
    return response


def readIndice(context):
    logThat("GAME", " Indice {} Question : {}".format(context.indice, context.question))
    response = []

    if story["quizz"][context.question]["indice"][context.indice]:
        response.append(story["quizz"][context.question]["indice"][context.indice])

    if len(story["quizz"][context.question]["indice"]) <= context.indice + 1:
        context.indice = 0
    else:
        context.indice += 1

    return response


def controlAnwser(context):
    cmd = list(story["quizz"][context.question]["control"])
    cmd.append(context.data)
    print(cmd)
    out_bytes = subprocess.check_output(cmd).decode().rstrip()
    logThat('DEBUT',out_bytes)

    if out_bytes == 'True':
        logThat("GAME", " Question :{} anwser correct : {}".format(context.question, context.data))
        return True
    elif out_bytes == "False":
        logThat("GAME", " Question :{} anwser wrong : {}".format(context.question, context.data))
        return False
    else:
        logThat("ERROR", "question : {} script control error - result :{}:".format(context.question, out_bytes))
        return False
