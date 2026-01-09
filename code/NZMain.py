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

def stablize():
    drone.hover(0.3)

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
    #Raise the drone until it reaches target_height (cm), then hover.
   
    while True:
        height = drone.get_bottom_range("cm")
        print("== in the while loop Height:", height)

        if height >= target_height:
            drone.set_throttle(HOVER_SPEED)
            drone.move(0.3)
            print("Reached target height")
            break

        drone.set_throttle(raise_speed)
        print("== not reached the Height:", height)

        drone.move(0.3)
        
def descendToHeight(target_height, descend_speed):
    
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
        drone.set_throttle(descend_speed)
        drone.move(0.3)

def passRedArch_GreenKeyhole(distance):
    # raise to the green circle level,
    raiseToHeight(150, 20)
    print("===========after raiseToHeight")
    #  then move forward to pass red arch adn green circle
    drone.move_forward(distance, "cm", 25)
    print("==========pass red arch and green circle")

def flyThroughPanel():
    ############## go through the panel start ==============
    # descend to the same level as circle on the panel
    #descendToHeight(40, -30)
    # move to pass the panel 
    drone.move_forward(30, "cm", 15)
    print("enter the circle")
    drone.hover(0.4)
    drone.move_right(40, "cm", 15)  # change the speed later
    print("exit the right circle")
    stablize()

def goBackToPath():
    # after exit, go back to the normal path
    drone.move_forward(30, "cm", 20)
    print("===========go through the panel")
    drone.move_left(30, "cm", 20)
    drone.move_forward(30, "cm", 20)
    print("==========before go through the tunnel")

def goThroughTunnel():
    raiseToHeight(100, 15)  # tunnel height
    drone.move_forward(30, "cm", 20) # pass the tunnel

def goThroughYellowKeyhole():
    #descend to the yellw circle
    descendToHeight(40, -30)
    setLedColor(COLOR_OFF)
    stablize()
    # pass the yellow circle
    drone.move_right(30, "cm", 20) 

def  goThroughBlueArch():
    drone.move_forward(30, "cm", 20) 
    drone.move_left(30, "cm", 20) 
    drone.move_forward(30, "cm", 20) 


# -------- MAIN --------
def main():

    drone = Drone()
    drone.connect()
    drone.takeoff()
    drone.hover(0.4)
    print("===========after takeoff")
    passRedArch_GreenKeyhole(40)   # TODO_1 INPUT flight distance
    # set the blue color
    setLedColor(COLOR_BLUE)  
    flyThroughPanel() # TODO_2 Adjust flight distance
    goBackToPath() # TODO_2 Adjust flight distance
    stablize()
    setLedColor(COLOR_GREEN)
    goThroughTunnel()
    goThroughYellowKeyhole()
    goThroughBlueArch()
    drone.land()  


# -------- Run Program --------
if __name__ == "__main__":
    main()
