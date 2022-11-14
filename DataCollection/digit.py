import rospy
from datetime import datetime
import csv
import rosbag
import os
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

from sensor_msgs.msg import Image

def getCurrentTimeStamp():
	now = datetime.now()
	timestamp = time.mktime(now.timetuple())
	return int(timestamp)


'''
Sensor: Digit Tactile Sensor
Data: Tactile Images
Format: .jpg
'''
class Digit:
	def __init__(self, object_dir):
		self.object_dir = object_dir
		self.bridge = CvBridge()

		self.digit_count = 0
		self.digit_path = object_dir
		print("reading in the digit images...")
		self.digit_sub = rospy.Subscriber('/digit/image_raw', Image, self.digitCallback)

	def digitCallback(self, img):
		try:
			self.img = self.bridge.imgmsg_to_cv2(img, 'bgr8')
		except CvBridgeError as  e:
			print(e)

	def stopRecord(self):
		self.digit_sub.unregister()

	def __str__(self):
		return 'Digit'
