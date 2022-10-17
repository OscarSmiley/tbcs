#!/usr/bin/env python3
#^^ very important ^^
import rospy
from std_msgs.msg import String
import sys
import os
#not sure why I have to do this in noetic, might need to use an __init__.py file or something
#sys.path.insert(0, os.path.abspath(os.getcwd()))
#print(sys.path[0])

from FilePreprocessor import Preprocessor
from StateMachine import StateMachine
#Simple start/restart container for the fsm
#May change the "fatal" and "restart" options later. But they sure look cool for now

def main(args):
    rospy.init_node('statemachine', anonymous = True)
    while(True):
        #Restart loop
        #inProcessor = Preprocessor(args[0])
        workingMachine = StateMachine(args[1], args[2])         #FsmController needs a path to the state script file
        exitStatus = "Fatal"
        if(workingMachine.startup()):
            exitStatus = workingMachine.runStates()
        if(exitStatus == "Fatal"):                  #may want to make this the else catch all
            #call abort fuction
            print("Fatal Exit")
            break
        elif(exitStatus == "Mission_Complete"):
            #shutdown fuction
            print("Complete Exit")
            break
        elif(exitStatus == "Restart"):
            #make system log entry and attempt to restart the control module
            print("FSM Restart")
            pass

if __name__ == '__main__':
    #try:
    main(sys.argv)
    #except rospy.ROSInterruptException
        #pass
