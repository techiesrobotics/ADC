from codrone_edu.drone import *

drone = Drone()
drone.pair()


drone.takeoff()
# fly forward until a wall is found 50 cm away. run this loop for 10 seconds.
drone.avoid_wall(10, 50)
#drone.move_forward(distance=20, "cm", speed=3)
drone.set_throttle(30)
drone.move(2)

# Stop upward movement
drone.set_throttle(0)
drone.hover(2)
drone.move_forward(20, "cm", 3)
drone.land()


drone.close()
