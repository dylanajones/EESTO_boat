#!/usr/bin/env python

# Code for converting wind sensor data to world frame

import rospy

from geographic_msgs.msg import Vector3
from geographic_msgs.msg import GeoPose

class Converter:

	def __init__(self):

		self.wind_sub = rospy.Subscriber('/crw_wind_pub', Vector3, self.wind_callback)
		self.pose_sub = rospy.Subscriber('/crw_geopose_pub', GeoPose, self.pose_callback)

		self.wind_pub = rospy.Publisher('/wind_converted', Vector3, queue_size=100)

		self.current_pose = GeoPose()

	def wind_callback(self, msg):
		print "Wind callback"

	def pose_callback(self, msg):
		print "Pose callback"