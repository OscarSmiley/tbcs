#!bin/bash/python
#import rospy
import std_msgs

#Contains a Preprocessor and current state and Postprocessor instances
#Compairs the current state and the imput language input using a transition algorithm (Contained in the state object)
#Decides to remain in the current state or transition to a new one
#the post-transition state object then issues control arguments to the Postprocessor that publishes messages
class StateMachine:
    Continue = False
    currentState = startState()

    inProcessor = Preprocessor()
    outProcessor = Postprocessor()
    inputVector = {}    #fsm input language
    outputVector = {}   #fsm output language
    history = []        #pushdown states
    def __init__(self):
        inputVector = inProcessor.getInputVector()
        Continue = inputVector[systemStatus]

    def runStates():
        while(Continue):
            inputVector = Preprocessor.getInputVector()
            currentState = currentState.getNext(inputVector, history)
            outputVector = currentState.generateRequest()
            outProcessor.generateMessages(outputVector)
            Continue = inputVector[systemStatus]
        currentState = statusExit()

    def statusExit():
        #system cannot continue
        #this might need to be a Postprocessor fuction
        pass
