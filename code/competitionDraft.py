from codrone_edu.drone import *
drone = Drone()
drone.connect()


drone.takeoff()


drone.get_pressure()


drone.set_throttle(67)
drone.move(1.3)
drone.set_throttle(20)
#Approaching the ring
drone.avoid_wall(99,20)


drone.set_throttle(80)
drone.move(2)
drone.set_throttle(20)


drone.hover(3)


drone.set_pitch(60)
drone.move(1.5)
drone.set_pitch(0)
#Descending from the ring
drone.set_throttle(-60)
drone.move(1.5)
drone.set_throttle(10)


drone.set_pitch(40)
drone.move(1)
drone.set_pitch(0)


drone.land()
