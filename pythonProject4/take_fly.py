import connect_my
import time
import Vehicle


def take_off(height, vehicle):
    connect_my.Connect()
    vehicle.mode = Vehicle.VehicleMode("GUIDED")
    vehicle.is_armable = True
    while not vehicle.is_armable:
        print("waiting for drone initialize")
        time.sleep(1)
        print("take off")
        vehicle.simple_takeoff(height)
    return vehicle
    # this method is means take off the height and return the vehicle status


#this height means check the you input == now
def check_the_height(vehicle, checkHeight):
    while True:
        print("Height",vehicle.location.global_relative_frame.alt )
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt>= checkHeight * 0.95:
            print("Reached target altitude")
            break


def getVehicle():
    vehicle = connect_my.Connect.vehicle
    return vehicle
