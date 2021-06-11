from __future__ import print_function
from dronekit import connect, Vehicle
import Vehicle
from Vehicle import MyVehicle

"""this class means add the flight controller value to the code"""

# set up the option parsing to connect the string
import argparse

parser = argparse.ArgumentParser(description="sample about create attribute from mavlink message")
parser.add_argument('--connect',default="ip")  # help is password and default wii auto connect
args = parser.parse_args()
connection_string = args.connect
sitl = None

# start the SITL if no connection string specified
if not connection_string:
    import dronekit_sitl

    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()

# connection to the vehicle
print("connecting to the vehicle on :" + connection_string)
vehicle = connect(args.connect(), wait_ready=True, vehicle_class=MyVehicle())


# Add observer for the custom attribute
def raw_imu_callback(self, attr_name, value):
    # attr_name == 'raw_imu'
    # value == vehicle.raw_imu
    print(value)


vehicle.add_attribute_listener('raw_imu', raw_imu_callback)
print('Display RAW_IMU messages for 5 seconds and then exit.')
time.sleep(5)
# The message listener can be unset using ``vehicle.remove_message_listener``

# close vehicle object before exiting script
print("close vehicle object")
vehicle.close()

#shut down simulator if it was started
if sitl is not None:
    sitl.stop()