#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def cb( message ):

    if 'n' in message.data:
      n  = ' fruit'
    elif 'r' in message.data:
      n = ' flower'
    else:
      n = ' sport'
    rospy.loginfo(message.data+n)

if __name__ == '__main__':
    rospy.init_node( 'type' )
    sub = rospy.Subscriber( 'moji_up', String, cb )
    rospy.spin()

