from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import flight_attribute


class Connect:

    def __init__(self):
        # default connection when call Connect
        print('Connecting to the ' + flight_attribute.connection_string)
        try:
            global vehicle_my
            vehicle_my = connect(args.connect, baud=57600, wait_ready=True)
        except:
            print('something goes wrong when connecting')

    vehicle = vehicle_my
