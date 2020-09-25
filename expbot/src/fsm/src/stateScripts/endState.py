#!bin/bash/python
import sys
class End:
    def __init__(self):
        self.currentVector = {}
        self.outputVector  = {}

    def getNext(self, inputVector, history):
        self.currentVector = inputVector
        nextState = self
        return nextState

    def generateRequest(self):
         self.outputVector =  {"systemStatus": "End"}
         return self.outputVector
