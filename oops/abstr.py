# class Animal():
#     print("Animal makes sound")

# class Dog(Animal):
#     def sound (self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound (self):
#         print("Cat meows")

# animals = [Dog(), Cat()]
# for a in animals:
#     a.sound()   
from abc  import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
a= Animal()   