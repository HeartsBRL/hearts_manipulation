#!/usr/bin/env python
import roslib
import rospy
import actionlib
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState
from std_msgs.msg import String

def do_it(name):
#create the play motion goal and tell it which motion to perform
    pmg = PlayMotionGoal()
    pmg.motion_name = name.data
    pmg.skip_planning = False
#tell the client to send the goal
    pmc.send_goal_and_wait(pmg)    

rospy.init_node("give_receive")
pmc = actionlib.SimpleActionClient("play_motion", PlayMotionAction)
pmc.wait_for_server()

#Subscriber to get motion name from '/motion_name' topic
rospy.Subscriber("motion_name", String, do_it)

rospy.spin()



#if __name__ == '__main__':    
    
