class Makers:
    language_choices = "Python","JavaScript"

    def __init__(self,name):
        self.name = name

    def instance_method(self):
        return f'Hello,{self.name}'

    @classmethod
    def class_method(cls):
        return f"Welcome to makers!What type of language do you choose?:{cls.language_choices}"     
    
    @staticmethod
    def static_method (choice):
        return f"Great!You chose {choice} course "

student1 = Makers(name = "Lukas")
print(student1.instance_method())
print(student1.class_method())
print(student1.static_method(choice = "Python"))


student2 = Makers(name ="Ashley")
print(student2.instance_method())
print(student2.class_method())
print(student2.static_method(choice="JavaScript"))

class User:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return f"{self.name},{self.email}"

    @classmethod
    def add_data(cls, user_info:list):
        name,email = user_info
        return cls(name, email)#user 


list_of_users = [
    ["Emily","emi@yahoo.com"],
    ["Boony","bon@yahoo.com"],
    ["Karen","karen@gmail.com"]
   
]
for info in list_of_users:
    user = User.add_data(info)
    print(user.get_info())
#user1 = User()
#user1 = User(name = "Emely",email = "emi@yahoo.com")
#print(user1.get_info())

class Lottery:

    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def generate_number():
        import random
        number = random.sample(list("123456789"), k = 5)
        number  =''.join(number)
        return number
        print(number)
        
    def get_number(self):
        number = self.generate_number() 
        self.number = number    
        return f"Dear{self.name}! Your lucky number is{self.number}"
# obj = Lottery('test')
# obj.generate_number()
participant1 = Lottery(name = "Lucas")
print(participant1.get_number())
print(participant1.number)


participant2 = Lottery(name = "Sandy")
print(participant2.get_number())
print(participant2.number)


class Pizza:
    def __init__(self,ingredients:list):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza with{self.ingredients}"
        
# pizza1 = Pizza(["tomato","cheese","basil"])
# pizza2  =Pizza (["totato","ham","pineapple"])
    @staticmethod
    def circle_area(radius):
        import math
        area = round (math.pi *radius**2,2)
        return f"Pizza's area is {area} sm2" 

    def area(self,radius):
        self.radius = radius
        return self.circle_area(self.radius)

    @classmethod
    def margarita(cls):
        return cls(["mozarella","tomato","basil"])

    @classmethod
    def pepperoni (cls):
        return cls(["pepperoni","cheese"])

    @classmethod
    def chilli(cls):
        return cls(["chilli","cheese","ham"])
pizza1 = Pizza.margarita()
print(pizza1)
print(pizza1.area(4))

print("------------")
pizza2 = Pizza.pepperoni()
print(pizza2)
print(pizza2.area(8))
print("------------")
pizza3 = Pizza.chilli()
print(pizza3)
print(pizza3.area(8))



        











# class A :
#     def instance_method(self): #  i tam i tam istance methody, 

#         print("method objecta")
#         print("self",self)

# obj = A()
# obj.instance_method()
# #self<_main_.Aobject at 035644yv0>
# # kogda my vyzyvajem methid u objekta, to nam nujno peredat v. self, on peredajetsya avtomaticheski 
# A.instance_method(obj) # not best option  v self priletit to chto 

# #method objekta 
# #self <_main_.A object at 000twgetge>
# #kogda my vyzyvajem method u klassa, to nam nujno peredat objekt 

# class A:
#     @classmethod### 
#     def class_method(cls):
#         print("method classa ")
#         print("cls",cls)

# A.class_method()
# #method klassa 
# # cls <class' __main__.A'>
# obj = A()
# obj.class_method()
# #vse ravno otkuda budete vyzyvat  object or class pervum argumentom budet prihodit clss 


# #primery 
# class C:
#     counter = 0 
#     def __init__(self):
#         ## object creates 
#         #C.counter+=1
#         self._inc_counter()
    
#     def __del__(self):
#      #   C.counter -=1
#         self._dec_counter()

#     @classmethod
#     def _inc_counter (cls):
#          cls.counter+=1
#     @classmethod

#     def _dec_counter(cls):
#         cls.counter -= 1

# obj1 = C() 
# obj2 = C()
# obj3 = C()
# obj4 = C()       
# print(C.counter)

# del obj1,obj2
# print(C.counter)

# class Pizza:
#         def __init__(self,radius,*ingredients):
#             self.r = radius
#             self.ingredients = ingredients
#         def cook(self):
#             print(f"Pizza size{self.r*2}")    
#             print(f"ingridients: {self.ingredients}")
#         @classmethod
#         def four_cheese(cls,radius):
#             pizza = cls(radius,"cheese","cheese1","cheese2","cheese3")
#             return pizza


# pizza1 = Pizza(15,"cheese","ham","cherry")
# pizza1.cook()       

# pizza2 = Pizza(10,"cheese","cheese1","cheese2","cheese3")
# pizza2.cook()


# pizza3 = Pizza(10,"cheese","cheese1","cheese2","cheese3")
# pizza3.cook()

# pizza4 = Pizza.four_cheese(10)
# pizza4.cook()

# pizza5 = Pizza.four_cheese(15)
# pizza5.cook()

# class A():
#     def static_method(self):
#         print("static method")

# obj = A()
# obj.static_method()

# class Cylinder:
#     def __init__(self,diameter,height) -> None:
#         self.di = diameter
#         self.h = height
#         self.area = self.get_area_cylinder(diameter,height)
    
#     @staticmethod
#     def get_area_cylinder(di,h):
#         from math import pi
#         circle_area =pi * di **2/4
#         side_area = pi * di * h 
#         return circle_area *2 + side_area


# #my ne sozdali objekt, no poluchili nujnuje nam rasschrty

#     def get_area(self, di,h):
#         from math import pi
#         circle_area =pi * di **2/4
#         side_area = pi * di * h 
#         return circle_area *2 + side_area

# cylinder1 = Cylinder(4,10)
# # print(cylinder1.area)
# print(cylinder1.get_area(4, 10))

# print(Cylinder.get_area_cylinder(4,10))  