# rospy-turtlebot-move-and-rotate

Basic Rospy code to move turtlebot forward and rotate for x number of seconds.

Unfortunely, for now docker version of ROS has issues relating to [real sense lib](https://github.com/IntelRealSense/librealsense/issues/2402), so manual download on VM or local is required.
# How to install: 
1. Install Ubuntu 16.04

2. Install ROS Kinetic full desktop version
http://wiki.ros.org/kinetic/Installation/Ubuntu

3. Install Extra Packages for turtlebots
https://yainnoware.blogspot.com/2018/09/install-turtlebot-on-ros-kinetic-ubuntu.html

4. If you are using VM - Fix issue with listening on image view (rosrun image_view image_view image:=/camera/rgb/image_raw fails)
https://stackoverflow.com/questions/55181205/gazebo-crashing-when-subscribing-to-scan

# How to Run:
- Ensure main node is running
  - roslaunch turtlebot_bringup minimal.launch OR roslaunch turtlebot_gazebo turtlebot_world.launch
- Run [move.py](https://github.com/KaleabTessera/rospy-turtlebot-move-and-rotate/blob/master/src/turtlebotcontroller/scripts/move.py) in specified pacakage.
  - rosrun [package] move.py

# Errors
- If running in simulator and you having issues with time durations:
  - rosparam set /use_sim_time false
