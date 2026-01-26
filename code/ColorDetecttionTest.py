from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
drone.takeoff()
drone.hover(2)
drone.land()


def detectColorandSetLed(duration):        
    drone.load_color_data("color_data")
    color = "green"
    start_time = time.time()

    while (time.time() - start_time) < duration:

        color_data = drone.get_color_data()
        detected = drone.predict_colors(color_data)
        if color == "green":
            drone.set_drone_LED(0, 255, 0, 100)
        elif color == "blue":
            drone.set_drone_LED(0, 0, 255, 100)
        elif color == "yellow":
            drone.set_drone_LED(255, 255, 0, 100)
        elif color == "red":
            drone.set_drone_LED(255, 0, 0, 100)
        else:
            drone.set_drone_LED(0, 0, 0, 0)


        color = detected[0]
        #print(detected[0])
        time.sleep(0.2)

drone.land()
detectColorandSetLed(1)


 





 
