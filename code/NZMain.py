from codrone_edu.drone import *
DESIRED_HEIGHT = 60 #cm
LOWEST_HEIGHT = 25 #cm
DESCEND_SPEED = -30 # negative = down
ASCEND_SPEED = 15
TOLERANCE = 3
#====================== Change LED Color============
COLOR_BLUE = 1
COLOR_GREEN = 2
COLOR_RED = 3
COLOR_YELLOW = 4
COLOR_OFF = 0


# -------- MAIN --------
def main():

    drone = Drone()
    drone.connect()
    #drone.takeoff()
    #drone.hover(0.4)
    setLedColor(COLOR_GREEN) 
    
    print("===========after takeoff")
    passRedArch_GreenKeyhole()   # TODO_1 INPUT flight distance
    # set the blue color
    setLedColor(COLOR_BLUE)  
    flyThroughPanel() # TODO_2 Adjust flight distance
    goBackToPath() # TODO_2 Adjust flightxs2 distance
    stablize()
    setLedColor(COLOR_GREEN)
    goThroughTunnel()
    setLedColor(COLOR_OFF)
    #setLedColor(COLOR_RED)
    goThroughYellowKeyhole()
    goThroughBlueArch()
    drone.land()  
    
def stablize():
    drone.hover(0.4)

def setLedColor(color_code):
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

def raiseToHeight(target_height, raise_speed):
    """
    Raise the drone until it reaches target_height (cm),
    then stabilize by hovering.
    """
    print("raiseToHeight:", target_height, raise_speed)

    TOLERANCE = 3        # cm, handles sensor noise

    while True:
        height = drone.get_bottom_range("cm")
        #print("Current height:", height)

        # Stop ascending once close enough to target height
        if height >= target_height - TOLERANCE:
            drone.set_throttle(0)     # stop vertical movement
            drone.hover(0.4)          # stabilize
            print("Reached target height --", height)
            break
        # Continue ascending
        drone.set_throttle(raise_speed)
        drone.move(0.3)

def descendToHeight(target_height, descend_speed):
    """
    Gradually descend until the drone reaches target_height (cm),
    then stabilize by hovering.
    """
    print("descendToHeight", target_height, descend_speed)
    while True:
        height = drone.get_bottom_range("cm")
        print("Current height:", height)

        # Stop descending once close enough to target height
        if height <= target_height + TOLERANCE:
            drone.set_throttle(0)     # stop vertical movement
            drone.hover(0.4)          # stabilize
            print("Reached target height. Hovering at:", height)
            break
        drone.set_throttle(-1 * descend_speed)   # descend_speed must be negative
        drone.move(0.3)


def passRedArch_GreenKeyhole():
    # raise to the green circle level,
    raiseToHeight(100, 15)
    print("===========after raiseToHeight")
    #  then move forward to pass red arch adn green circle
    stablize()
    drone.move_forward(30, "cm", 25)
    print("==========pass red arch and green circle")

def flyThroughPanel():
    ############## go through the panel start ==============
    # descend to the same level as circle on the panel
    descendToHeight(40, 30)
    stablize()
    # move to pass the panel 
    drone.move_forward(30, "cm", 15)
    print("enter the circle")
    drone.move_right(40, "cm", 15)  # change the speed later
    print("exit the right circle")

def goBackToPath():
    # after exit, go back to the normal path
    drone.move_forward(30, "cm", 20)
    print("===========go through the panel")
    #stablize()
    drone.move_left(30, "cm", 20)
    #stablize()
    drone.move_forward(30, "cm", 20)
    stablize()
    print("==========before go through the tunnel")

def goThroughTunnel():
    raiseToHeight(100, 15)  # tunnel height
    stablize()
    drone.move_forward(25, "cm", 15) # pass the tunnel
    stablize()

def goThroughYellowKeyhole():
    #descend to the yellw circle
    descendToHeight(40, 30)
    setLedColor(COLOR_OFF)
    stablize()
    # go through the hole
    drone.move_right(30, "cm", 20) 
    stablize()
    # back to original path
    drone.move_forward(30, "cm", 15) 
    stablize()
    drone.move_left(30, "cm", 15) 
    stablize()

def  goThroughBlueArch():
    print("goThroughBlueArch, start")
    #drone.move_forward(30, "cm", 20) 
    #stablize()
    #drone.move_left(30, "cm", 20) 
    #stablize()
    drone.move_forward(30, "cm", 20) 
    print("goThroughBlueArch, end")





# -------- Run Program --------
if __name__ == "__main__":
    main()
