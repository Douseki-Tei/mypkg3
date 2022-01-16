#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2022 Ryuich Ueda. All rights reserved.
#*Copyright(c)2022 Douseki Tei. All rights reserved.

import rospy
from std_msgs.msg import Int32

rospy.Init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 100

while not rospy.is_shutdown():
     n -= 10
     pub.publish(n)
     rate.sleep()

