#!/usr/bin/env python3
import sys
import os
import rospy
from std_msgs.msg import String
from Fileprocessor import Preprocessor
from Datapublisher import Datapublisher

def main(args):
    rospy.init_node("depthsensor", anonymous = True)
    rate = rospy.Rate(7) #how do I pick these rates? I don't even know
    depthInput = Preprocessor(args[0])
    #Can use the statndard datapublisher here
    ioFilePath = os.path.abspath(os.getcwd()) + "/src/test_depth_sensor/io.txt"
    depthPublisher = Datapublisher(depthInput.getKeys(), ioFilePath)
    while(not rospy.is_shutdown()):
        depthVector = depthInput.getInputVector()
        depthFrame = "{}".format(depthVector["xdepth"])
        print("FRAME: ", depthFrame)
        depthPublisher.publish_data({"depthFrame" : depthFrame})
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv[1:])
