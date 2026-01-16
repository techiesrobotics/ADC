from codrone_edu.drone import *
import time

#====================== Change LED Color============
COLOR_BLUE = 1
COLOR_GREEN = 2
COLOR_RED = 3
COLOR_YELLOW = 4
COLOR_OFF = 0

def setLedColor(drone, color_code):
    #Change drone LED based on color_code.
    if color_code == COLOR_BLUE:        # Blue
        drone.set_drone_LED(0, 0, 255, 100)
    elif color_code == COLOR_GREEN:      # Green
        drone.set_drone_LED(0, 255, 0, 100)
    elif color_code == COLOR_RED:      # Red
        drone.set_drone_LED(255, 0, 0, 100)
    elif color_code == COLOR_YELLOW:      # Yellow
        drone.set_drone_LED(255, 255, 0, 100)
    else:                      # Off / default
        drone.set_drone_LED(0, 0, 0, 0)

#================MAIN==========================
drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(0.4)
setLedColor(drone, COLOR_BLUE)
drone.move_forward(distance=10, units="cm", speed=1)
drone.land()
