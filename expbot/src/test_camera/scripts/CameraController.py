#!/usr/bin/env python3
import sys
import os
import rospy
from std_msgs.msg import String
from Fileprocessor import Preprocessor
from Datapublisher import Datapublisher

def main(args):
    rospy.init_node("camera", anonymous = True)
    rate = rospy.Rate(5)
    cameraInput = Preprocessor(args[0])
    #Can use the statndard datapublisher here
    ioFilePath = os.path.abspath(os.getcwd()) + "/src/test_camera/io.txt"
    cameraPublisher = Datapublisher(cameraInput.getKeys(), ioFilePath)
    while(not rospy.is_shutdown()):
        #cameraFrame = ("%s,%s", cameraInput.getInputVector()["x"],cameraInput.getInputVector()["x"])
        cameraVector = cameraInput.getInputVector()
        cameraFrame = "{},{}".format(cameraVector["x"], cameraVector["y"])
        #print("FRAME: ", cameraFrame)
        cameraPublisher.publish_data({"cameraframe" : cameraFrame})
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv[1:])
