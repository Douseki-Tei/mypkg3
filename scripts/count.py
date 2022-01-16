#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2022 Ryuich Ueda. All rights reserved.
#*Copyright(c)2022 Douseki Tei. All rights reserved.


import rospy
from std_msgs.msg import Int32

rospy.init_node('second')
pub = rospy.Publisher('second_up', Int32, queue_size = 1)
rate = rospy.Rate(3)

n = 0

while not rospy.is_shutdown():
        n += 10
        pub.publish(n)
        rate.sleep()
