#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(4)
n = 0

while not rospy.is_shutdown():    
    if 0 <= n < 50:
        n += 1

    elif 50 <= n < 100:
        n += 2

    else:
        n -= 100

    pub.publish(n)
    rate.sleep()
