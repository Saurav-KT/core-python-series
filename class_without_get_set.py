
# Basic method of setting and getting attributes in Python
# class Celsius:
#     def __init__(self, temperature =0):
#         self.temperature = temperature
#
#     def fahrenheit(self):
#         return (self.temperature * 1.8)+32
#
#
# obj= Celsius(37)
# print(obj.temperature)
# print(obj.fahrenheit())

""" Implement a constraint that temperature of any 
object cannot reach below -273.15 degrees Celsius"""

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = None
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature()*1.8)*32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self,value):
        if value< -273.15:
            raise ValueError("temperature below -273.15 is not possible")
        self._temperature= value

obj= Celsius(37)
print(obj.get_temperature())
print(obj.to_fahrenheit())

# new constraint implementation
obj.set_temperature(-280)

# Get the to_fahrenheit method
obj.to_fahrenheit()
