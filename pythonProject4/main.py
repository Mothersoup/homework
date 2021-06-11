import take_fly

operation = take_fly
height = 15
# this height unit is meter
vehicle = operation.getVehicle()
vehicle = operation.take_off(height,vehicle)
operation.check_the_height(vehicle, height)
print('take off',height,'complete')