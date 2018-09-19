#!/usr/bin/env python
import roslib
import rospy
import actionlib
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState
from std_msgs.msg import String



rospy.init_node("give_receive")
pms = actionlib.SimpleActionClient("play_motion", PlayMotionAction)
pms.wait_for_server



#if __name__ == '__main__':    
