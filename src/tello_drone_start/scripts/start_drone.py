from djitellopy import Tello
import time

# Create a Tello instance. This will automatically try to connect to your Tello drone.
tello = Tello()

try:
    tello.connect()  # Connect to the drone
    tello.takeoff()  # Command the drone to take off

    time.sleep(1)  # Wait for 2 seconds

    # tello.move_up(5)
    tello.move_forward(50)
    # tello.move_left(20)
    # tello.move_right(20)
    # tello.move_back(20)  # Move up by 50cm
    # tello.rotate_clockwise(90)  # Rotate clockwise by 90 degrees
    time.sleep(1)


    # time.sleep(2)  # Wait for 2 seconds
    print('drone connected')
finally:
    tello.land()  # Land the drone
    tello.end()  # End the connection with the drone
    pass
