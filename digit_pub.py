""" ROS image publisher for DIGIT sensor """

import argparse
# OpenCV
import cv2
from PIL import Image as Im
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Ros libraries
import roslib
import rospy

# Ros Messages
from sensor_msgs.msg import Image
from sensor_msgs.msg import std_msgs
from digit_sensor import DigitSensor


class ImageFeature:

    def __init__(self):
        # topic where we publish

        self.image_pub = rospy.Publisher("/digit/image_raw/",
                                         Image, queue_size=10)
        self.br = CvBridge()


def rgb_pub(digit_sensor: DigitSensor):
    # Initializes and cleanup ros node
    ic = ImageFeature()
    rospy.init_node('image_feature', anonymous=True)
    digit_call = digit_sensor()
    br = CvBridge()
    while True:
        frame = digit_call.get_frame()
        print(frame.shape)
        msg = br.cv2_to_imgmsg(frame, encoding="bgr8")
        ic.image_pub.publish(msg)
        rospy.loginfo("published ...")
        if cv2.waitKey(1) == 27:
            break


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--fps", type=int, default=30)
    argparser.add_argument("--resolution", type=str, default="VGA")
    argparser.add_argument("--serial_num", type=str, default="D20001")
    args, unknown = argparser.parse_known_args()
    digit = DigitSensor(args.fps, args.resolution, args.serial_num)
    rgb_pub(digit)