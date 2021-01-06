#!/usr/bin/env python3
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


    def getInputVector(self):
        VectorsAvalible = True
        vectorCounter = 0
        inputVector = {}
        if(self.lineposition < len(self.sampleData)):
            #print(len(self.sampleData))
            try:
                endposition = self.sampleData[self.lineposition + 1:].index(";")
            except ValueError:
                print("no avalible vectors")
                VectorsAvalible = False
                inputVector["systemStatus"] = "Bad"
                return inputVector
            vectorArray = self.sampleData[self.lineposition + 1:self.lineposition + endposition + 1].split(",");
            if(not VectorsAvalible):
                inputVector["systemStatus"] = "Bad"
            #inputVector["systemStatus"] = VectorsAvalible
            for key, val in zip(self.inputKeys, vectorArray):
                inputVector[key] = val
            self.lineposition += endposition + 1
            #print(inputVector)
            return inputVector
        return None
