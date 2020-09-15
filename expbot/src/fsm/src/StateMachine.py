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
print(sys.path)
#package these up
from startState import startState
from Preprocessor import Preprocessor
#from Postprocessor import Postprocessor
class StateMachine:
    Continue = True
    #outProcessor = Postprocessor() #default recieve/publish objects
    inProcessor = Preprocessor()   #"
    currentState = startState() #default state
    inputVector = {}    #fsm input language
    outputVector = {}   #fsm output language
    history = []        #pushdown states
    def __init__(self, testPreprocessor = None):
        if(testPreprocessor != None):
            self.inProcessor = testPreprocessor
        #inputVector = inProcessor.getInputVector()
        #print(inputVector)

    def runStates(self):
        while(self.Continue == True):
            inputVector = self.inProcessor.getInputVector()
            print(inputVector)
            #add methods later
            '''currentState = currentState.getNext(inputVector, history)
            outputVector = currentState.generateRequest()
            outProcessor.generateMessages(outputVector)'''
            self.Continue = inputVector["systemStatus"]
        #currentState = statusExit()

    def statusExit():
        #system cannot continue
        #this might need to be a Postprocessor fuction
        pass
