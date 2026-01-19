class Employee:
    def __init__(self, name: str, address: str, age: int):
        self.name = name
        self.address = address
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def emp_address(self):
        return self.address



# emp = Employee(name="saurav", address="Hyderabad", age=30)
# print(emp., emp.address, emp.age)


