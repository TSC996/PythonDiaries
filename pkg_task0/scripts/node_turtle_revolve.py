#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
def node_turtle_revolve():
    ## Initalsing the node 
    rospy.init_node('node_turtle_revolve', anonymous=True)

    # Publisher command
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
     
    # Linear and angular velocities as per the data by the e yantra Hints
    cmd = Twist()
    cmd.linear.x =  1.0
    cmd.angular.z = 1.0

    
    now = rospy.Time.now()
    rate = rospy.Rate(10)
    def pose_msg(msg):
        rospy.loginfo("Moving in a circle: x:%0.6f", msg.x)
        # rospy.loginfo("turtle position:  x:%0.6f ",msg.x)
    # rospy.loginfo("Moving Turtle: ")
    while rospy.Time.now() < now + rospy.Duration.from_sec(6):
        # rospy.loginfo(theta, x)
        pub.publish(cmd)
        rate.sleep()
        rospy.Subscriber("/turtle1/pose", Pose, pose_msg)
    rospy.loginfo("Goal Reached Succesfully!!")
if __name__ == '__main__':
    try:
        node_turtle_revolve()
        
        
    except rospy.ROSInterruptException:
        pass
