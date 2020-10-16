#!bin/bash/python
import sys
class History:
    def __init__(self, history_depth):
        self.__position = 0
        self.__depth = history_depth
        self.__historyList = []
    def add(self, inputVector, outputVector):
        if(len(self.__historyList) == self.__depth):
            self.__historyList.pop() #forget the last element to make room
        self.__historyList.insert(0,  [inputVector, outputVector])  #add the current element
    def peektop(self):
        self.__position = 1
        return(self.__historyList[0])
    def peeknext(self):
        if(self.__position < self.__depth):
            self.__position += 1
            return(self.__historyList[self.__position - 1])
        else:
            self.__position == self.__depth
            return None
