import rospy
import geodesy.utm
from geographic_msgs.msg import GeoPose

class PathExecutor:

	def __init__(self):

		print "Starting path executor"
		rospy.init_node('path_executor', anonymous=False)
		self.wp_pub = rospy.Publisher('/crw_waypoint_sub', GeoPose, queue_size=100)
		self.wp_sub = rospy.Subscriber('/crw_waypoint_reached', GeoPose, self.reached_callback)

	def reached_callback(self, msg):

		if self.path.len() > 2:
			# TODO: Add in the replanning here
			self.wp_pub(self.path.pop(0))
		else:
			while (self.path.len() > 0):
				self.wp_pub(self.path.pop(0))