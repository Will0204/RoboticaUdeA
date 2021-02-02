#!/usr/bin/python
#
# Send a value to change the opening of the Robotiq gripper using an action
#

import argparse

import rospy
import actionlib
import control_msgs.msg


def gripper_client(value):
	try:
		# Start the ROS node
        	#rospy.init_node('gripper_command')

		# Create an action client
		client = actionlib.SimpleActionClient(
		'/gripper_controller/gripper_cmd',  # namespace of the action topics
		control_msgs.msg.GripperCommandAction # action type
		)

		# Wait until the action server has been started and is listening for goals
		client.wait_for_server()

		# Create a goal to send (to the action server)
		goal = control_msgs.msg.GripperCommandGoal()
		goal.command.position = value   # From 0.0 to 0.8
		goal.command.max_effort = -1.0  # Do not limit the effort (-1.0)
		client.send_goal(goal)

		client.wait_for_result(rospy.Duration(2.0))

		return client.get_result()
	except rospy.ROSInterruptException:
		print ("Program interrupted before completion")
		return 0;


if __name__ == '__main__':
    try:
	print("Prueba")
        
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
