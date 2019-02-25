#!/usr/bin/env python
import roslib
import rospy
import actionlib
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState
from std_msgs.msg import String

def do_motion(x):
#create the play motion goal and tell it which motion to perform
    print("doing motion")
    pmg = PlayMotionGoal()
    pmg.motion_name = x.data
    pmg.skip_planning = False
#tell the client to send the goal
    pmc.send_goal_and_wait(pmg)


pmc = actionlib.SimpleActionClient("play_motion", PlayMotionAction)
pmc.wait_for_server

rospy.Subscriber("motion_name", String, do_motion)



if __name__ == '__main__':
    rospy.init_node("motion_player")
rospy.spin()
