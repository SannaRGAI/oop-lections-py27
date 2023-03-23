# from abc import ABC, abstractmethod

# class AbstractAnimal(ABC):
#     @abstractmethod 
#     def speak():
#         pass

# class Dog(AbstractAnimal):
#     pass
# obj = Dog
# class Dog(AbstractAnimal):
#     def speak(self):
#         print('gav-gav')

# from abc import abstractmethod
# class Makers(ABC):
#     def __init__(self,name) -> None:
#         self.name = name 
#     @abstractmethod 
#     def study(self):
#         pass
# class Students(Makers):
#     def study(self):
#         print(" i can smth")
#     def play(self):
#         print("i m playing a game")
# kul = Students(name= "John")
# # obj.study()
# kul.play()
        

   
from abc import ABC, abstractmethod
class Airplane(ABC):
    def __init__(self,length) -> None:
        self.length = length
    @abstractmethod
    def fly(self,speed):
        pass

class Helicopter(Airplane):
    def __init__ (self,length):
        self.length = length
    def fly (self,speed):
        print(f"i can fly with a turbo {speed}")
obj = Helicopter(length= 700)
obj.fly(speed = 400) 
obj.fly(500)               





