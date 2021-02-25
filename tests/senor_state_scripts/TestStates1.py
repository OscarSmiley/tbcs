#!bin/bash/python
import sys
from endState import End
class TEST1:
    def __init__(self, inputVector, history):
        self.history = history
        self.currentVector = inputVector
        self.outputVector  = {}

    def testprint(self):
        print("TEST1")

    def getNext(self, inputVector, history):
        self.currentVector = inputVector
        self.history = history
        nextState = self
        print("TEST1: ", self.currentVector)
        if(self.currentVector["systemStatus"] == "Good"):
            if(float(self.currentVector["key1"]) < 2.417):
                print("TEST1: shift -> TEST2")
                nextState = TEST2(self.currentVector, self.history)

            else:
                print("TEST1: no shift")
            return nextState

    def generateRequest(self):
            self.outputVector = self.currentVector
            return self.outputVector

class TEST2:
    def __init__(self, inputVector, history):
        self.history = history
        self.currentVector = inputVector
        self.outputVector  = {}

    def testprint(self):
        print("TEST2")

    def getNext(self, inputVector, history):
        self.currentVector = inputVector
        self.history = history
        nextState = self
        print("TEST2: ", self.currentVector)
        if(self.currentVector["systemStatus"] == "Good"):
            if(float(self.currentVector["key2"]) < 5.781):
                print("TEST2: shift -> endState")
                nextState = End()
            else:
                print("TEST2: no shift")
            return nextState


    def generateRequest(self):
            self.outputVector = self.currentVector
            return self.outputVector
