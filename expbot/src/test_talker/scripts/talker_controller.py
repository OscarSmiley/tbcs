#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import sys
from Fileprocessor import Preprocessor
from Datapublisher import Datapublisher

#####
# talker_controller
# creates a set of test publications used to develope the fsm inprocessor and its subscribers
# reads input from a testfile in the same format as those use by the filepreprossor testers
#####

def main(args):
    #args: location of test sampledata file

    #create ros node and debuging publisher
    rospy.init_node('testtalker', anonymous = True)
    talker_debugpub = rospy.Publisher('talker_debugpub', String, queue_size=10)
    rate = rospy.Rate(10)

    #create fileprocessor and internal publisher objects
    Fileprocessor = Preprocessor(args[0])
    Publisher = Datapublisher(Fileprocessor.getKeys())

    while(not rospy.is_shutdown()):
        #debug timestamp
        time_str = "test_talker at %s" % rospy.get_time()
        #rospy.loginfo(time_str)
        talker_debugpub.publish(time_str)

        #publish each item in the dictionary in a seperate publisher
        sense_dictionary = Fileprocessor.getInputVector()
        Publisher.publish_data(sense_dictionary)

        #print("\n")
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv[1:])
