#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3.4


import re
import argparse
from confUtils import *
import readUtils

global darg


# A Propos ############################################################################
def apropos():
    print("todo")


# Version ############################################################################
def version():
    print("version 1.0.0")


# Generic Function ##################################################################
def main():
    logThat("INFO", "============ Start Deamon ============")

    state = start()

    while (state.next != Next.toStop):

        if state.next == Next.toWelcomeMessage:
            welcomeMessage(state)

        elif state.next == Next.toReadQuestion:
            readQuestion(state)

        elif state.next == Next.toWaitForInput:
            waitForInput(state)

        elif state.next == Next.toDectectInput:
            dectectInput(state)

        elif state.next == Next.toAnalyseAnswser:
            analyseAnswer(state)

        elif state.next == Next.toAnalyseCommand:
            analyseCommand(state)

        elif state.next == Next.toGoto:
            gotTo(state)

        elif state.next == Next.toReadIndice:
            readIndice(state)

        elif state.next == Next.toReadAnswer:
            readAnwser(state)

    logThat("INFO", "============ Stop Deamon ============")


# Function ##################################################################


def welcomeMessage(state):
    logThat("DEBUG", "WelcomeMessage Function")
    readUtils.readWelcomeMessage()
    state.next = Next.toReadQuestion


def waitForInput(state):
    logThat("DEBUG", " waitForInput Function")
    inputData = input(state.question+">")
    state.data = inputData
    state.next = Next.toDectectInput


# Analyses
def dectectInput(state):
    logThat("DEBUG", "dectectInputFormat Function")
    CommandeParse = re.search("/(?P<commande>.*)$", state.data)
    if CommandeParse is not None:
        state.commande = CommandeParse.group('commande')
        state.next = Next.toAnalyseCommand
    else:
        state.next = Next.toAnalyseAnswser


def analyseCommand(state):
    logThat("DEBUG", "AnalyseCommand Function")
    command = state.commande.split()
    cmd = str(command[0].upper())
    if cmd == "STOP":
        state.next = Next.toStop
    elif cmd == "WHAT":
        state.next = Next.toReadQuestion

    elif cmd == "INDICE":
        state.next = Next.toReadIndice

    elif cmd == "GOTO":
        state.question = int(command[1])
        state.next = Next.toGoto
    else:
        print("pas compris")
        state.next = Next.toWaitForInput


def analyseAnswer(state):
    logThat("DEBUG", "AnalyseAnswer Function")
    state.next = Next.toWaitForInput
    corect = False
    if corect:
        state.next = Next.toGoto
        state.question = state.question + 1
    else:
        state.next = Next.toWaitForInput
        print("wrong")


# Questions
def readQuestion(state):
    logThat("DEBUG", "ReadQuestion Function")
    readUtils.readQuestion(state.question)
    state.next = Next.toWaitForInput


def readAnwser(state):
    logThat("DEBUG", " readAnwser Function")
    readUtils.readAnwser(state.question)
    state.next = Next.toReadQuestion


def readIndice(state):
    logThat("DEBUG", "readIndice Function")
    readUtils.readIndice(state.question)
    state.next = Next.toWaitForInput


# Commands
def gotTo(state):
    logThat("DEBUG", "gotTo Function")
    state.next = Next.toReadQuestion
    print(state.question)


def start():
    logThat("DEBUG", "start Function")
    return State(0, Next.toWelcomeMessage)


def stop():
    logThat("DEBUG", "Stop Function")
    state.next = Next.toStop


# Main ############################################################################
if __name__ == "__main__":

    # création du parse des arguments
    parser = argparse.ArgumentParser(description="Editeur")

    # déclaration et configuration des arguments
    parser.add_argument('conf', nargs='?', type=str, action="store", default="", help="fichier de configuration")
    parser.add_argument('-a', '--about', action='store_true', default=False, help="A propos du logiciel")
    parser.add_argument('-v', '--version', action='store_true', default=False, help="Version du logiciel")

    # dictionnaire des arguments
    dargs = vars(parser.parse_args())

    # print(dargs) # affichage du dictionnaire pour mise au point

    if dargs['about']:
        apropos()
        sys.exit()

    if dargs['version']:
        version()
        sys.exit()

    main()
