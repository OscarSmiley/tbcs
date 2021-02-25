import sys
import os
import rospy
from std_msgs.msg import String
import re
class Datapublisher:
    def __init__(self, datakeys):
        #read the test_talker.txt file and load a list of publishers and a list of subscribers
        #create a dictionary for the realion of publishers to data keys
        self.subscribers = {} #these gotta be keyed because ros doesn't seem to provide a way to get the name of a publisher object
        self.publishers = {}
        ioFilePath = os.path.abspath(os.getcwd()) + "/src/test_talker/io.txt"
        ioFile = open(ioFilePath, "r")
        pubsSubs = ioFile.readlines()
        rospy.loginfo(pubsSubs)
        for line in pubsSubs:
            if line[0] == '#':
                pass
            elif line[0] == ">":
                pass
                #self.subscribers[line[1:]] = ##make a subscriber
            elif line[0] == "<":
                pubName = line[1:].strip()
                self.publishers[pubName]= rospy.Publisher(pubName, String, queue_size=10)
            else:
                print("invalid io manifest file")

        rospy.loginfo(self.publishers)

    def publish_data(self, datavector):
        #publish each item in the dictionary in a serperate publisher initialized in __init__
        #item must be a string and have a key that matches a publisher
        for item in datavector:
            if item in self.publishers and type(datavector[item]) is str:
                outstr = datavector[item] + ", time=%s"  % rospy.get_time()
                #print("publish --> " + outstr)
                self.publishers[item].publish(outstr)
                #print(self.publishers[item])
                #rospy.loginfo(outstr)
            else:
                #record missed publishing time
                rospy.loginfo("Invalid data item at %s" % rospy.get_time())
