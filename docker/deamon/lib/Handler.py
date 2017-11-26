#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3.4



import re
import sys
import http.server
from lib.interac import *
from lib.State import *
from lib.Context import *

global darg


class Handler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        logThat("INFO", "============ Start Deamon ============")

        context = self.server.context
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data)  # <-- Print post data
        self._set_headers()
        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")

        while (context.next != State.toStop or context.next != State.toWaitForInput ):

            if context.next == State.toWelcomeMessage:
                self.welcomeMessage(context)

            elif context.next == State.toQuestion:
                self.Question(context)

            elif context.next == State.toWaitForInput:
                self.waitForInput(context)

            elif context.next == State.toDectectInput:
                self.dectectInput(context)

            elif context.next == State.toAnalyseAnswser:
                self.analyseAnswer(context)

            elif context.next == State.toAnalyseCommand:
                self.analyseCommand(context)

            elif context.next == State.toGoto:
                self.gotTo(context)

            elif context.next == State.toIndice:
                self.Indice(context)

            elif context.next == State.toAnswer:
                self.Anwser(context)

        logThat("INFO", "============ Stop Deamon ============")


    # Function ##################################################################


    def welcomeMessage(self,context):
        logThat("DEBUG", "WelcomeMessage Function")
        readWelcomeMessage(context)
        context.next = State.toQuestion


    def waitForInput(self,context):
        logThat("DEBUG", " waitForInput Function")



    # Analyses
    def dectectInput(self,context):
        logThat("DEBUG", "dectectInputFormat Function")
        CommandeParse = re.search("/(?P<commande>.*)$", context.data)
        if CommandeParse is not None:
            context.commande = CommandeParse.group('commande')

            context.next = State.toAnalyseCommand
        else:
            context.next = State.toAnalyseAnswser


    def analyseCommand(self,context):
        logThat("DEBUG", "AnalyseCommand Function")
        command = context.commande.split()
        cmd = str(command[0].upper())
        if cmd == "STOP":
            context.next = State.toStop
        elif cmd == "WHAT":
            context.next = State.toQuestion

        elif cmd == "INDICE":
            context.next = State.toIndice

        elif cmd == "GOTO":
            context.question = int(command[1])
            context.next = State.toGoto
        else:
            writeToUser("I didn't understand")
            context.next = State.toWaitForInput
        self.cleanContext(context)


    def analyseAnswer(self,context):
        logThat("DEBUG", "AnalyseAnswer Function")
        context.next = State.toWaitForInput
        corect = controlAnwser(context)

        if corect:
            context.next = State.toGoto
            context.question += 1
        else:
            context.next = State.toWaitForInput
            writeToUser("I didn't understand")
        cleanContext(context)


    def cleanContext(self,context):
        context.data = ""
        context.commande = ""


    # Questions
    def Question(self,context):
        logThat("DEBUG", "ReadQuestion Function")
        readQuestion(context)
        context.next = State.toWaitForInput


    def Anwser(self,context):
        logThat("DEBUG", " readAnwser Function")
        readAnwser(context)
        context.next = State.toQuestion


    def Indice(self,context):
        logThat("DEBUG", "readIndice Function")
        readIndice(context)
        context.next = State.toWaitForInput


    # Commands
    def gotTo(self,context):
        logThat("DEBUG", "gotTo Function")
        context.next = State.toQuestion


    def start(self):
        logThat("DEBUG", "start Function")
        return Context(0, State.toWelcomeMessage)


    def stop(self):
        logThat("DEBUG", "Stop Function")
        sys.exit()


