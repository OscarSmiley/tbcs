#!bin/bash/python
import sys
import StateMachine
def main(args):
    testMachine = StateMachine()
    testMachine.runStates()
if __name__ == '__main__':
    main(sys.argv[1:])
