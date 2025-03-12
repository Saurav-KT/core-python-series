from parent import *

vehicle_obj = vehicle('Honda','X-ADV','MoterBike')
print(vehicle_obj.brand,vehicle_obj.model, vehicle_obj.type)

# Calling Method
vehicle_obj.fuel_up(10000)
vehicle_obj.drive()
vehicle_obj.update_fuel_level(19)

print("tank size",vehicle_obj.model, vehicle_obj.fuel_level)
