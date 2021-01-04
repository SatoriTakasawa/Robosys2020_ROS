#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import String

rospy.init_node('moji')
pub = rospy.Publisher('moji_up', String, queue_size=1)
rate = rospy.Rate(1)
global n
while not rospy.is_shutdown():
    r  = random.choice('abc')
    if r =='a':
        n = 'banana\U0001F34C'
    elif r =='b': 
        n = 'rose\U0001F339'
    else:
        n = 'basket\U0001F3C0'
    pub.publish(n)
    rate.sleep()

