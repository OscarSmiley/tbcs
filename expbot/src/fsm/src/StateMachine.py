#!bin/bash/python
#import rospy
#import std_msgs
from Preprocessor import Preprocessor

#Contains a Preprocessor and current state and Postprocessor instances
#Compairs the current state and the imput language input using a transition algorithm (Contained in the state object)
#Decides to remain in the current state or transition to a new one
#the post-transition state object then issues control arguments to the Postprocessor that publishes messages
class StateMachine:
    Continue = True
    #currentState = startState()

    #inProcessor = Preprocessor()    #test preprocessor loads state vectors from a sample file
    #outProcessor = Postprocessor()
    inputVector = {}    #fsm input language
    outputVector = {}   #fsm output language
    history = []        #pushdown states
    inProcessor = Preprocessor()
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
