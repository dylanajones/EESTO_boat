# Code for converting wind sensor data to world frame

import rospy

class Converter():

	def __init__(self):

		self.wind_sub = 