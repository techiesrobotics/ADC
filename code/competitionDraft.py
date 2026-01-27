from codrone_edu.drone import *
drone = Drone()
drone.pair()
# 1 - Take off
drone.takeoff()

def detectColorandSetLed(duration):        
    drone.load_color_data("color_data")

    start_time = time.time()

    while (time.time() - start_time) < duration:

        color_data = drone.get_color_data()
        color = drone.predict_colors(color_data)
        if color[0] == "green":
            drone.set_drone_LED(0, 255, 0, 100)
        elif color[0] == "blue":
            drone.set_drone_LED(0, 0, 255, 100)
        elif color[0] == "yellow":
            drone.set_drone_LED(255, 255, 0, 100)
        elif color[0] == "red":
            drone.set_drone_LED(255, 0, 0, 100)
        else:
            drone.set_drone_LED(0, 0, 0, 0)

        print(color[0])
        time.sleep(0.2)
        
def changeHeight(power, time, hoverTime):
    drone.set_throttle(power)
    drone.move(time)
    drone.set_throttle(20)
    drone.hover(hoverTime)

def moveForward(power, time, hoverTime):
    drone.set_pitch(power)  
    drone.move(time)
    drone.set_pitch(0)
    drone.hover(hoverTime)
    
    #drone.move_forward(distance=50, units="cm", speed=1)
    #drone.move_distance(0.5, 0.5, 0.25, 1) # move forward 0.5m, left 0.5m, and upward 0.25m simultaneously at 1m/s

def moveRight(power, time, hoverTime):
    drone.set_roll(power)  
    drone.move(time)
    drone.set_roll(0)
    drone.hover(hoverTime)

def moveLeft(power, time, hoverTime):
    drone.set_roll(-1*power)  
    drone.move(time)
    drone.set_roll(0)
    drone.hover(hoverTime)

def path1():
    changeHeight(67, 1.3, 2)
    # pass gate and green keyhole
    moveForward(60, 1, 1)
    drone.land()
    detectColorandSetLed(1)

def path2():
    # 2 - Raise get ready for passing Red Gate
    changeHeight(67, 1.3, 2)
    # pass gate, green keyhole and panel
    moveForward(80, 1, 1)
    drone.land()
    detectColorandSetLed(1)

def path3():

    changeHeight(40, 1, 2)
    moveForward(30,1,1)
    changeHeight(-25, 1 ,2)
    moveRight(30, 1,1)
    moveForward(30,1,1)
    moveLeft(30, 1,1)
    moveForward(30,1,1)
    drone.land()
    drone.close()

#path1()
#path2()
path3()
