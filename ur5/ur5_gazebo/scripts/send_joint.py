#!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
import rospy

def joint_client(position):

	rospy.init_node('send_joints')
	pub = rospy.Publisher('/trajectory_controller/command',
		          JointTrajectory,
		          queue_size=10)

	# Create the topic message
	traj = JointTrajectory()
	traj.header = Header()
	# Joint names for UR5
	traj.joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint',
		        'elbow_joint', 'wrist_1_joint', 'wrist_2_joint',
		        'wrist_3_joint']

	rate = rospy.Rate(10)
	i=0
	while not rospy.is_shutdown():
		traj.header.stamp = rospy.Time.now()
		pts = JointTrajectoryPoint()
		pts.time_from_start = rospy.Duration(1.0)
		pts.positions = position

		# Set the point to the trajectory
		traj.points = []
		traj.points.append(pts)
		# Publish the message
		pub.publish(traj)

		if(i == 20000): break;
		i = i + 1;


if __name__ == '__main__':
    try:
        joint_client()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
