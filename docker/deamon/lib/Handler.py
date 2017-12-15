#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python 3.4

import re
import sys
import http.server
import copy
from lib.interac import *
from lib.State import *
from lib.Context import *

global darg


class Handler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        logThat("INFO", "============ Receive Request ============")
        context = self.getContext()
        context.data = self.getInput()

        while (context.next != State.toStop and context.next != State.toEndWorking):
            logThat("INFO", str(context.next))
            if context.next == State.toWelcomeMessage:
                data=self.welcomeMessage(context)
                context.answer.extend(data)
                context.next = State.toQuestion

            elif context.next == State.toQuestion:
                context.answer.extend(self.Question(context))
                context.next = State.toEndWorking

            elif context.next == State.toDectectInput:
               self.dectectInput(context)

            elif context.next == State.toAnalyseAnswser:
                self.analyseAnswer(context)

            elif context.next == State.toAnalyseCommand:
                self.analyseCommand(context)

            elif context.next == State.toGoto:
                self.gotTo(context)

            elif context.next == State.toIndice:
                context.answer.extend(self.Indice(context))
                context.next = State.toEndWorking

            elif context.next == State.toAnswer:
                context.answer.extend(self.Anwser(context))
                context.question += 1
                context.next = State.toQuestion
        self.saveContext(context)
        self.sendAnswer(context)

    # Function ##################################################################
    def getInput(self):
        try:
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length).decode("utf-8").rstrip()
        except:
            logThat("ERROR", " Syntax problem")
            data = "Syntax Invalid"

        return data

    def getContext(self):
        return self.server.context

    def saveContext(self, context):
        savedContext = copy.copy(context)
        savedContext.data = ""
        savedContext.commande = ""
        savedContext.next = State.toDectectInput
        savedContext.answer = []
        self.server.context = savedContext

    def sendAnswer(self, context):
        self._set_headers()
        context.answer.append("\n")
        response='\n'.join(context.answer)
        self.wfile.write(bytes(response, 'utf-8'))

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # Analyses
    def dectectInput(self, context):
        logThat("DEBUG", "dectectInputFormat Function")
        CommandeParse = re.search("-(?P<commande>.*)$", context.data )
        if CommandeParse is not None:
            context.commande = CommandeParse.group('commande')
            context.next = State.toAnalyseCommand
        else:
            context.next = State.toAnalyseAnswser

    def analyseCommand(self, context):
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
            context.next = State.toEndWorking
            context.answer.append("I didn't understand")

    def analyseAnswer(self, context):
        logThat("DEBUG", "AnalyseAnswer Function")
        context.next = State.toEndWorking
        corect = controlAnwser(context)

        if corect:
            context.next = State.toAnswer
            context.answer.append("Perfect")
        else:
            context.next = State.toEndWorking
            context.answer.append("Nope")

    # interacs
    def welcomeMessage(self, context):
        logThat("DEBUG", "WelcomeMessage Function")
        return readWelcomeMessage(context)

    def Question(self, context):
        logThat("DEBUG", "ReadQuestion Function")
        return readQuestion(context)

    def Anwser(self, context):
        logThat("DEBUG", "readAnwser Function")
        return readAnwser(context)

    def Indice(self, context):
        logThat("DEBUG", "readIndice Function")
        return readIndice(context)

    # Commands
    def gotTo(self, context):
        logThat("DEBUG", "gotTo Function")
        context.next = State.toQuestion

    def start(self):
        logThat("DEBUG", "start Function")
        return Context(0, State.toWelcomeMessage)

    def stop(self):
        logThat("DEBUG", "Stop Function")
        sys.exit()
