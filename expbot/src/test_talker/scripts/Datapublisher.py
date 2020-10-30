import sys
import rospy
from std_msgs.msg import String

class Datapublisher:
    def __init__(self, datakeys):
        self.pubdict = {}
        #create a publisher object for each key in a dictionary
        for key in datakeys:
            self.pubdict[key] = rospy.Publisher(key, String, queue_size=10)

    def publish_data(self, datavector):
        #publish each item in the dictionary in a serperate publisher initialized in __init__
        #item must be a string and have a key that matches a publisher
        for item in datavector:
            if item in self.pubdict and type(datavector[item]) is str:
                outstr = datavector[item] + ", time=%s"  % rospy.get_time()
                rospy.loginfo(outstr)
                self.pubdict[item].publish(outstr)
            else:
                #record missed publishing time
                rospy.loginfo("Invalid data item at %s" % rospy.get_time())
