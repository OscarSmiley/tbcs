#!bin/bash/python
import sys
import TestStates
class startState:

    def __init__(self):
        self.currentVector = {}
        self.outputVector  = {}
        self.history = {}

    def testprint(self):
        print("startState")

    def getNext(self, inputVector, history):
        print("startState:", inputVector)
        nextState = self
        self.currentVector = inputVector
        if(self.currentVector["systemStatus"] == "Good"):
            print("startState.getNext: shift -> TEST1")
            nextState = TestStates.TEST1(self.currentVector, self.history)
        return nextState
        #if not return self then create and instance of the next state with the inputVector
    def generateRequest(self):
        #normally output vector would be generated here
        self.outputVector = self.currentVector
        print("startState output:", self.outputVector)
        return self.outputVector
