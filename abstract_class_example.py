from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def makesound(self):
        pass

    def sleep(self):
        print("sleeping")

class Dog(Animal):
    def makesound(self):
        print("Woof")

class Cat(Animal):
    def makesound(self):
        print("Meow")

dog= Dog()
dog.makesound()
dog.sleep()

cat= Cat()
cat.makesound()