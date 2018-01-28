#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node('count')
pub = rospy.Publisher('count_up', Float64, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
    n += 1
    pub.publish(n)
    rate.sleep()
