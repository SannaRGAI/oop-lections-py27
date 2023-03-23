# #magic - 
# class A:
#     def __init__(self,b):
#         self.b = b
#         print("init works")

#     def fly (self):
#         print("dreamimg")


#     def __str__(self) -> str:
#         return self.b    
# obj = A(b = "processing")
# # print(obj) 
# # obj.fly()
# """
# Создайте класс-миксин RadioMixin, 
# и реализуйте в нем метод для проигрывания музыки play_music, который принимает в переменную title название песни.

# Метод должен печатать строку "Песня называется title", где вместо title должно быть переданное название песни.

# Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина.
#  Класс Amphibian также как в предыдущем задании должен наследоваться от классов Auto и Boat.
#   Создайте экземпляры auto, boat и obj от трех классов и примените метод play_music
#  """

# class RadioMixin:
#     def play_music(self,title):
#         print(f"Песня называется {title}")
# class Auto(RadioMixin):
#     pass
# class Boat(RadioMixin):
#     pass 
# class Amphibian(Auto,Boat):
#     pass

# auto = Auto()
# boat = Boat()
# boat.play_music("MIlK")
# obj = Amphibian()
# auto.play_music(title="Love")
# obj.play_music("Shake")

# """ Будильник. Создайте класс Clock, у которого будет метод current_time показывающий текущее время и класс Alarm, с методами on и off для включения и выключения будильника.

# Далее, создайте класс AlarmClock, который наследуется от двух предыдущих классов.

# Добавьте к нему метод alarm_on для установки будильника, при вызове которого должен включатся будильник.

# Создайте экземпляр clock класса AlarmClock и примените к ниму методы current_time и alarm_on.

# Ввод должен быть:

# clock.current_time() 
# clock.alarm_on() 
# С выводом:

# 17:10:41 
# Будильник включен  """
# from datetime import datetime
# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime("%H:%M:%S"))
# class Alarm:
#     def on(self):
#         print('Будильник включен')  
#     def off(self):
#         print("Будильник выключен")
# class AlarmClock(Clock,Alarm):
#     def alarm_on(self):
#         self.on()                  
# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()
""" Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры как — experience и languages_frontend соответственно.

Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.

Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских классов.

Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите их методы.

Ввод должен быть:

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 
Вывод:

Python разработчик, уровень: Junior, потрачено 12 часов на программирование

Javascript разработчик, уровень: Middle, потрачено 45 часов на программирование

Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование  """
from abc import ABC, abstractmethod
class Coder(ABC):
    count_code_time = 0
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def coding(self):
        pass
class Backend(Coder):
    def __init__(self,experience,languages_backend) -> None:
        self.experience = experience
        self.languages_backend = languages_backend

    def get_info(self):
        return (f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование")
    def coding(self,quantity):
        self.count_code_time += quantity

class Frontend(Coder):
    def __init__(self,experience,languages_frontend) -> None:
        self.experience = experience
        self.languages_frontend = languages_frontend

    def get_info(self):
        return (f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование")
    
    def coding(self,quantity):
        self.count_code_time += quantity  

class Fullstack(Frontend,Backend):
    pass

a = Backend("Middle","Python")
b = Frontend("Junior","JS")
c = Fullstack("Senior","Python and JS")



a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 


# obj = Backend("Middle","Python")
# obj.coding(100)
# print(obj.get_info())


