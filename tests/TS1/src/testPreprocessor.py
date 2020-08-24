#!bin/bash/python
#import regex
import sys
class Preprocessor:
    lineposition = 0
    inputI = 0
    inputKeys = []
    def __init__(self, testFileLoc):
        self.testFile = testFileLoc
        with open(self.testFile, 'r') as f:
            self.sampleData = f.read()
        self.lineposition = self.sampleData.index(";")
        self.inputKeys = self.sampleData[:self.lineposition].split(",")
        #for char in self.sampleData:
            #if (char == ';'):
                #self.inputKeys = self.sampleData[:index(char)].split(",")


    def dataPrint(self):
        print("input keys:")
        for key in self.inputKeys:
            print(key + " ", end="")
        print("\nsample data:\n" + self.sampleData)
        print("lineposition =", self.lineposition)

    def getInputVector(self):
        vectorCounter = 0
        inputVector = {}
        if(self.lineposition < len(self.sampleData)):
            print(len(self.sampleData))
            try:
                endposition = self.sampleData[self.lineposition + 1:].index(";")
            except ValueError:
                print("no avalible vectors")
                return None
            vectorArray = self.sampleData[self.lineposition + 1:self.lineposition + endposition + 1].split(",");
            print(self.sampleData[self.lineposition + 1:self.lineposition + endposition + 1])
            print("\ngetInputVector:: lineposition =",self.lineposition +1 , "endposition =", self.lineposition + endposition + 1)
            print("getInputVector:: |inputKeys| =", len(self.inputKeys))
            print("getInputVector:: vectorArray =", vectorArray)
            for key, val in zip(self.inputKeys, vectorArray):
                inputVector[key] = val
            self.lineposition += endposition + 1
            return inputVector
        return None

"""def main(args):
    Preprocessor = testPreprocessor(args[0])
    Preprocessor.dataPrint()
    #testMachine = StateMachine(testPreprocessor)
    #testMachine.runStates()
    print("testPreprocessor main")
if __name__ == '__main__':
    main(sys.argv[1:])"""
