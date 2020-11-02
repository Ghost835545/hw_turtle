#! /usr/bin/python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt

class turtlemove():

    def __init__(self):
        rospy.init_node('turtlemove_node')
        self.velocity_publisher = rospy.Publisher('/leonardo/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/leonardo/pose', Pose, self.callback)
	self._subscriber = rospy.Subscriber('donatello/pose', Pose, self.move2goal)
	self.initPose = 1
        self.pose = Pose()
        self.rate = rospy.Rate(5)


    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def move2goal(self,msg):
		goal_pose = Pose()
		goal_pose.x = msg.x
		goal_pose.y = msg.y
		distance_tolerance = 1
		vel_msg = Twist()
   		if sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:
				vel_msg.linear.x = 0.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0

		 
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
				self.velocity_publisher.publish(vel_msg)

x = turtlemove()
rospy.spin()
 

