#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
Nabeatsu = 0

def cb(message):
    global Nabeatsu
    m=message.data
    if m % 3 == 0:
        Nabeatsu = str(m)+":   3 no baisu"

    elif"3" in str(m):
        Nabeatsu = str(m)+":   3 no tsuku suji"

    else:
        Nabeatsu = str(m)
    return Nabeatsu


if __name__ == '__main__': 
    rospy.init_node('Nabeatsu_counter')
    sub = rospy.Subscriber('count_up', Float64, cb) 
    pub = rospy.Publisher('Nabeatsu_counter', String, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(Nabeatsu)
        rate.sleep()
