#!bin/bash/python
import sys
from FilePreprocessor import Preprocessor
from StateMachine import StateMachine
#Simple wrap up of the sub fsm. May change the "fatal" and "restart" options later. But they sound cool for now

def main(args):
    while(True):
        #Restart loop
        inProcessor = Preprocessor(args[0])
        inProcessor = Preprocessor(args[0])
        testMachine = StateMachine(inProcessor)
        Exit_Status = testMachine.runStates()
        if(Exit_Status == "Fatal"): #may want to make this the else catch all
            #call abort fuction
            #test print statement
            print("Fatal Exit")
            break
        elif(Exit_Status == "Mission_Complete"):
            #shutdown fuction
            #test print statement
            print("Complete Exit")
            break
        elif(Exit_Status == "Restart"):
            #make system log entry and attempt to restart the control module
            print("FSM Restart")
            pass

if __name__ == '__main__':
    main(sys.argv[1:])
