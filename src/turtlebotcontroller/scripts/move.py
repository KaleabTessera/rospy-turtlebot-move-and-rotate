#!/usr/bin/env python
# A very basic TurtleBot script that moves TurtleBot forward indefinitely. Press CTRL + C to stop.  To run:
# On TurtleBot:
# roslaunch turtlebot_bringup minimal.launch
# On work station:
# python move.py

import rospy
from geometry_msgs.msg import Twist
class GoForward:

    def forward(self,lin,ang):
	rospy.loginfo("Moving - lin : {} ang : {}".format(lin,ang))
        # Twist is a datatype for velocity
        move_cmd = Twist()
	# let's go forward 
        move_cmd.linear.x = lin
	# let's turns
	move_cmd.angular.z = ang
	# publish the velocity
        self.cmd_vel.publish(move_cmd)

    def __init__(self):
        # initiliaze
        rospy.init_node('GoForward', anonymous=False)

	# tell user how to stop TurtleBot
	rospy.loginfo("To stop TurtleBot CTRL + C")

        # What function to call when you ctrl + c    
        rospy.on_shutdown(self.shutdown)
        
	# Create a publisher which can "talk" to TurtleBot and tell it to move
        # Tip: You may need to change cmd_vel_mux/input/navi to /cmd_vel if you're not using TurtleBot2
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
     
	#TurtleBot will stop if we don't keep telling it to move.  How often should we tell it to move? 10 HZ
        r = rospy.Rate(10);
	
	# as long as you haven't ctrl + c keeping doing...
        while not rospy.is_shutdown():
		# Move forward at 0.3 for 5 sec
		t0 = rospy.get_rostime().secs
		while(t0 + 5 >= rospy.get_rostime().secs):
			self.forward(0.3,0)
		# Rotate at 1  for 1 sec
		t0 = rospy.get_rostime().secs
		while(t0 + 1 >= rospy.get_rostime().secs):
			self.forward(0,1)
		# Move forward at 0.2  for 5 sec
		t0 = rospy.get_rostime().secs
		while(t0 + 5 >= rospy.get_rostime().secs):
			self.forward(0.2,0)
	#	r.sleep()
		break
                        
        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	# a default Twist has linear.x of 0 and angular.z of 0.  So it'll stop TurtleBot
        self.cmd_vel.publish(Twist())
	# sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        move = GoForward()
	
    except:
        rospy.loginfo("GoForward node terminated.")


