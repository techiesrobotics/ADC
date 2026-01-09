from codrone_edu.drone import *
DESIRED_HEIGHT = 60 #cm
LOWEST_HEIGHT = 25 #cm
DESCEND_SPEED = -30 # negative = down
HOVER_SPEED = 1

#====================== Change LED Color============
COLOR_BLUE = 1
COLOR_GREEN = 2
COLOR_RED = 3
COLOR_YELLOW = 4
COLOR_OFF = 0

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


def raiseToHeight(drone, target_height):
    #Raise the drone until it reaches target_height (cm), then hover.
    RAISE_SPEED = 20
    HOVER_SPEED = 0

    while True:
        height = drone.get_bottom_range("cm")
        print("== in the while loop Height:", height)

        if height >= target_height:
            drone.set_throttle(HOVER_SPEED)
            drone.move(0.3)
            print("Reached target height")
            break

        drone.set_throttle(RAISE_SPEED)
        print("== not reached the Height:", height)

        drone.move(0.3)
        
def descendToHeight(drone, target_height):
    
    #Gradually descend until the drone reaches target_height (cm),
    #then hover.
    while True:
        height = drone.get_bottom_range("cm")
        print("Current height:", height)

        # Stop descending once target height is reached
        if height <= target_height:
            drone.set_throttle(0)      # hover
            drone.move(0.8)
            print("Reached target height. Hovering.")
            break
        drone.set_throttle(DESCEND_SPEED)
        drone.move(0.3)


# -------- MAIN --------
def main():

    drone = Drone()
    drone.connect()
    drone.takeoff()
    drone.hover(2)
    print("===========after takeoff")
    # raise to a height that can go through 
    #raiseToHeight(drone, 150)
    print("===========after raiseToHeight")

    # move through red arch and green circle
    drone.set_pitch(0)
    drone.set_roll(0)
    drone.set_yaw(0)
    drone.move(0.5)

    drone.move_forward(50, "cm", 25)

    # set the blue color
    setLedColor(COLOR_BLUE)  

    ############## go through the panel start ==============
    # descend to the same level as circle
    descendToHeight(drone, 25)
    # move to pass the panel 
    drone.move_forward(30, "cm", 20)
     
    drone.move_right(30, "cm", 20)  # change the speed later
    
    ############## go through the panel end maybe -- this can repeat multiple times ==============
    # after exit, go back to the normal path
    drone.move_forward(30, "cm", 20)
    print("===========go through the panel")
    drone.move_left(30, "cm", 20)
    drone.move_forward(30, "cm", 20)
    setLedColor(COLOR_GREEN)
    raiseToHeight(drone, 100)  # tunnel height
    drone.move_forward(30, "cm", 20) # pass the tunnel
    #descend to the yellw circle
    
    descendToHeight(drone, 40)
    setLedColor(COLOR_OFF)
    # pass the yellow circle
    drone.move_right(30, "cm", 20) 
    # pass the blue arch
    drone.move_forward(30, "cm", 20)  # adjust the distance to land
   
    #set_led_by_number(drone, COLOR_OFF)
    drone.land()


# -------- Run Program --------
if __name__ == "__main__":
    main()
