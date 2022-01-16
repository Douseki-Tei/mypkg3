#!/usr/bin/env python3

#SPDX-License-Identifier:BSD-2.0

#*Copyright(c)2022 Ryuich Ueda. All rights reserved.
#*Copyright(c)2022 Douseki Tei. All rights reserved.

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*3

if __name__== '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
