#!bin/bash/python

##################### Overview ######################
#   Contains a Preprocessor and current state and Postprocessor instances
#   Compairs the current state and the imput language input using a transition algorithm (Contained in the state object)
#   Decides to remain in the current state or transition to a new one
#   the post-transition state object then issues control arguments to the Postprocessor that publishes messages


#python standard and ros
#import rospy
#import std_msgs
import sys
#Machine objects and state scripts
sys.path.insert(1, sys.path[1] + '/stateScripts')
#package these up
from startState import startState
from Preprocessor import Preprocessor
#from Postprocessor import Postprocessor
class StateMachine:
    def __init__(self, testPreprocessor = None):
        self.Continue = "Good"
        #outProcessor = Postprocessor() #default recieve/publish objects
        self.inProcessor = Preprocessor()
        self.currentState = startState() #default state
        self.inputVector = {}    #fsm input language
        self.outputVector = {}   #fsm output language
        self.history = []        #pushdown states
        if(testPreprocessor != None):
            self.inProcessor = testPreprocessor
        #inputVector = inProcessor.getInputVector()
        #print(inputVector)

    def runStates(self):
        cycleCount = 0
        while(self.Continue == "Good"):
            print(">> Cycle: ", cycleCount)
            #self.currentState.testprint()
            self.inputVector = self.inProcessor.getInputVector()
            print("StateMachine input:", self.inputVector)
            #add methods later
            self.currentState = self.currentState.getNext(self.inputVector, self.history)
            self.outputVector = self.currentState.generateRequest()
            print("StateMachine output:", self.outputVector)
            #outProcessor.generateMessages(outputVector)
            self.Continue = self.outputVector["systemStatus"]
            cycleCount += 1


    def statusExit():
        #system cannot continue
        #this might need to be a Postprocessor fuction
        pass
