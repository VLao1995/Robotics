import sys, getopt
import geometry_msgs.msg import Point
import geometry_msgs.msg import Vector3

LOCATION = None

def location_callback(loc_msg):
    
    global LOCATION
    LOCATION = loc_msg
    
def start():

   rospy.init_node('thruster')
   rospy.Suscriber('location', Point, location_callback)    
   
   thrust_pub = rospy.Publisher('thrust', Vector3, queue_size=1)
   
   thrust = Vector3
   
   while location is None and not rospy.is_shutdown():
      rospy.sleep(.1)
      
   target_altitude = 100.0
   
   rate = rospy.Rate(10)
   
   while not rospy.is_shutdown():
      if LOCATION < target_altitude 
         thrust.y = 100.0
         rospy.loginfo("THRUSTERS ENGAGED)
       else
          thrust.y = 0
          
       thrust_pub.publish(thrust)
       rate.sleep()     



if __name__ == "__main__":
  start()