'''Object oriented programming is a way of enclosing  the data member and member functions into a user defined
entity called a class'''

'''Class holds perticular data items that relates to each other and communicate in a specific way. We access the properties 
and the member functions using objects'''

"""Memory is never allocated when we create a class,but memory gets allocated when we create its instance i.e object"""

# Class, Object, Method, constructor, Inheritance, Polymorphism, Abastraction, Oveloading,Overridding,Data hiding, Encapsulation

'About using Self in python'

# Self argument represents the object itself.
# Self will refer to the specific instance of this object that's being operated on.
# It is a part of the Python syntax to access data member of objects.
# Self is always pointing to current object.
# Self is the first argument to be passed in constructor and instance method. If you don't provide it, will cause an error.


# use __new__ when you need to control the creation of new instance
# use _init__ when you need to control intialization of the new instance.

# A method is a function that takes a class instance as its first parameter. Methods are members of classes.

class vehicle:
    # This is an employee class
    # emp_name="Akhila Khandala"

    # def intro(self):
    #     print("hello OOP world")

    # def __new__(self, parameter):
    #     print("new invoked", parameter)
    #     return super().__new__(self)

    def __init__(self, brand, model, type):
        self.brand = brand,
        self.model = model,
        self.type = type,
        self.gas_tank_size = 20
        self.fuel_level = 0

    def fuel_up(self,fuel_cost_per_trip):
        self.fuel_level = self.gas_tank_size
        print('Gas tank is full now')
        print('Cost per trip',fuel_cost_per_trip)

    def drive(self):
        print(f'The {self.model} is ready for drive')

    def update_fuel_level(self, new_level):
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print("exceeded capacity")







# object.__new__(class, *args,**kwargs)
# print(dir(obj))

