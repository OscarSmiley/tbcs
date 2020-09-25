#!bin/bash/python
import sys
sys.path.insert(1,'/home/oscarmorrison/Documents/AUVIC/Misc_Env/expdfsa/expbot/src/fsm/src')
from testPreprocessor import Preprocessor
from StateMachine import StateMachine

def main(args):
    inProcessor = Preprocessor(args[0])
    testMachine = StateMachine(inProcessor)
    testMachine.runStates()
    print("main end")
if __name__ == '__main__':
    main(sys.argv[1:])
