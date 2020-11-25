import rospy
from std_msgs.msg import String
import sys

#Object that takes control system subscriptions
#And converts them to a standardized input language for the fsm
#Adds abstraction between the fsm and and the robot systems
class Preprocessor:
    def __init__(self, externalPublishers):
        self.currentData = {}
        self.listeners = {}
        for pub in externalPublishers:
            ##
            # Create subscriber for each publsher key.
            # Subscriber class updatekey when a new message is published, passes arguments currentData and key as args[0,1]
            # Update key addes the most recent key to the currentData dictionary
            # when .getInputVector is called the current dictionary is returned
            ##
            self.listeners[pub + "_listener"] = rospy.Subscriber(key, String, updatekey, (self.currentData, key))

        ### debug code ###
        for listener in self.listeners:
            print(">>> " + listener)        #print listener key name
            print(self.listeners[listener]) #print listener object


    def updatekey(data, args):
        data_dictionary = args[0]
        publisher_key = args[1]

    def getInputVector(self):
        return self.currentData
        #takes a snapshot of what data is published at approximatly the present time

### Notes ###
# May want to change the scheme from constant updating to a scanning sort of process if it is possible
