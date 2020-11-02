#!/usr/bin/python

import rospy  
from geometry_msgs.msg import Twist
import time
import math

class my_class:
	def __init__(self):
		self.pub = rospy.Publisher('/donatello/cmd_vel',Twist,queue_size=1)
		self.sub = rospy.Subscriber('/turtle1/cmd_vel',Twist,self.func)
	def func(self, msg):
		self.pub.publish(msg)

rospy.init_node('my_listener')
m = my_class()

rospy.spin()

