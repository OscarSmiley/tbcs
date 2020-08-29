#!bin/bash/python
#import rospy
#import std_msgs

#Object that takes control system subscriptions
#And converts them to a standardized input language for the fsm
#Adds abstraction between the fsm and and the robot systems
class Preprocessor:
    inputVector = {}
    def __init__(self):
        inputVector = {
            #Continue signal
            "systemStatus" : True,
            #Position components
            "X": 0,  #longitudinal
            "Y": 0, #lateral
            "Z": 0,  #vertical
            #Velocity components
            "Xvel": 0,
            "Yvel": 0,
            "Zvel": 0,
            #X-Y plane, heading
            "Bearing": 0,
            #Object detection
            "hasTarget"   : False, #nav has located sensor target
            "targetX"     : 0, #Vertical in sensor image
            "targetY"     : 0, #Horizontal in sensor image
            "targetRange" : 0, #detected distance to target
        }


    def getInputVector(self):
        #takes subscription services and creates an output vector (Dictionary)

        return self.inputVector
