#!bin/bash/python
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
        self.startposition = self.lineposition
        self.inputKeys = self.sampleData[:self.lineposition].split(",")

    def getKeys(self):
        return self.inputKeys

    def getInputVector(self):
        VectorsAvalible = True
        vectorCounter = 0
        inputVector = {}
        if(self.lineposition < len(self.sampleData)):
            try:
                endposition = self.sampleData[self.lineposition + 1:].index(";")
            except ValueError:
                #print("No avalible vectors")
                #VectorsAvalible = False
                #inputVector["systemStatus"] = "Bad"
                #return inputVector
                self.lineposition = self.startposition
                endposition = self.sampleData[self.lineposition + 1:].index(";")

            vectorArray = self.sampleData[self.lineposition + 1:self.lineposition + endposition + 1].split(",");
            for key, val in zip(self.inputKeys, vectorArray):
                inputVector[key] = val
            self.lineposition += endposition + 1
            #print(inputVector)
            return inputVector
        return None
