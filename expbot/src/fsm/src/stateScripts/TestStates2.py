#!bin/bash/python
import sys
from endState import End
class Decent:
    def __init__(self, inputVector, history):
        self.history = history
        self.currentVector = inputVector
        self.outputVector  = {}

    def testprint(self):
        print("Decent")

    def getNext(self, inputVector, history):
        pass
    def generateRequest(self):
        pass
