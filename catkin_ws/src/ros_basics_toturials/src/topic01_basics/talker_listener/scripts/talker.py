#!/usr/bin/env python
import rospy
from std_msgs.msg import String       

def talker() : 
    pub = rospy.Publisher('chatter', String, queue_size=10) 
     #we need to initialize the node
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'talker' node 
    rospy.init_node('talker' , anonymous=True)
    rate = rospy.Rate(1) #1hz
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s"% i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i=i+1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass        
