import rospy
from std_msgs.msg import String
import sys
import os

### Notes ###
# May want to change the scheme from constant updating to a scanning sort of process if it is possible

#Object that takes control system subscriptions
#And converts them to a standardized input language for the fsm
#Adds abstraction between the fsm and and the robot systems
class Preprocessor:
    def __init__(self):
        self.currentData = {}
        self.subscribers = {} #keyed for local naming
        self.publishers = {}
        #
        #   Should find a way to do locate the io file regardless of start directory.
        #   Or possibly lock down the run location using a launchfile (maybe?)
        #
        ioFilePath = os.path.abspath(os.getcwd()) + "/src/fsm/io.txt"
        ioFile = open(ioFilePath, "r")
        pubsSubs = ioFile.readlines()
        rospy.loginfo(pubsSubs)
        for line in pubsSubs:
            if line[0] == '#':
                pass
            elif line[0] == ">":
                subName = line[1:].strip()
                self.subscribers[subName] = rospy.Subscriber(subName, String, self.callback, (subName, subName))
            elif line[0] == "<":
                pubName = line[1:].strip()
                self.publishers[pubName] = rospy.Publisher(pubName, String, queue_size=10)
            else:
                print("invalid io manifest file")

        rospy.loginfo(self.publishers)

    #callback fuction   constantly being called when new data is being published
    #need a way to pass self argument so currentData can be updated across the object
    ##Subscriber callbacks:
    #   All subscriber callbacks come here. Subscriber name is identified by args[1] fsm dictionary in args[0]
    def callback(self, data, args):
        dictOut = args[0]
        callerId = args[1]
        self.currentData[callerId] = str(data.data).split(',')[0] #take the timestap off from test_talker (change in other applications)

    def getInputVector(self):
        #takes a snapshot of what data is published at approximatly the present time
        #print("getInputVector", self.currentData)
        return self.currentData
