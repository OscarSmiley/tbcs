#!bin/bash/python
import sys
sys.path.insert(1,)
from testPreprocessor import Preprocessor
from StateMachine import StateMachine

def main(args):
    print(args[0])
    inProcessor = Preprocessor(args[0])
    #Preprocessor = Preprocessor(args[0])
    inProcessor.dataPrint();
    inputVector = inProcessor.getInputVector()
    while(inputVector != None):
        print(inputVector)
        inputVector = inProcessor.getInputVector()
    #testMachine = StateMachine(Preprocessor)
    #testMachine.runStates()

if __name__ == '__main__':
    main(sys.argv[1:])
