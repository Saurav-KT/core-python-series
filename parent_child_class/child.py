# Inheritance
'''Inheritance is a feature used in object oriented programming, it refers to defining a new class with less or no
modification to an existing class. This allows you to extend your classes by driving properties and methods from parent classes'''

'''When one class inherits from another, it automatically has access to all of the attributes and method of the parent class.
you can declare new attributes and methods in the child class and override attribute and method of the parent class.
To inherit from another class includes the name of the parent class in parantheses when defining the new class.
'''
# The new class is called derived class and from one which it inherits is called the base class.
from parent import vehicle


class ElectricVehicle(vehicle):
    def __init__(self, brand, model, type):
        # The Python super() function returns objects represented in the parents class and enables multiple inheritances.
        # It returns a proxy object which is represented in the parent's class.

        super().__init__(brand, model, type)
        self.battery_size = 85
        self.charge_level = 0

    def charge(self):
        self.charge_level = 100
        print('The vehicle is now charged')

    def fuel_up(self, fuel_cost_per_trip):
        if fuel_cost_per_trip == 0:
            print('This vehicle has no fuel tank with zero trip')
        else:
            super().fuel_up(fuel_cost_per_trip)


child_obj = ElectricVehicle('Tesla', 'Model 3', 'Car')
child_obj.charge()
child_obj.drive()
child_obj.fuel_up(0)
