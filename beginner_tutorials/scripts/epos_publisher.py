#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import epos
from std_msgs.msg import Float64
## Give the control mode

SPEED = 0
POSITION = 1
MODE = POSITION

## Define the publisher function
def position_publish(x):
    pub = rospy.Publisher('rpm', epos, queue_size=10)   #Initialize the topic name, message type and data flow rate
    rospy.init_node('epos_motor_control', anonymous=True) # node name
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pos_vel=epos()
        pos_vel.mode = MODE
        if pos_vel.mode==0:
            pos_vel.velocity=x    
        elif pos_vel.mode==1:
            pos_vel.position=x
        else:
            print('please input mode=0 or 1')
        rospy.loginfo(pos_vel)
        pub.publish(pos_vel)
        rate.sleep()
        #return pos1
if __name__ == '__main__':
    try:
        x=float(input('The reference number:'))
        position_publish(x)
    except rospy.ROSInterruptException:
        pass
