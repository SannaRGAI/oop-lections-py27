# # # # class Parent:
# # # #     def who_am_i(self):
# # # #         print("i m a parent")

# # # # class Child(Parent):
# # # #     def who_am_i(self):
# # # #         super().who_am_i()
# # # #         print("i m a child")

# # # # child = Child()
# # # # child.who_am_i()

# # # # class Grandpa:
# # # #     def talant1(self):
# # # #         print("i m good at dancing")

# # # # class Grandma:
# # # #     def talant2(self):
# # # #         print("i m good at singing")        


# # # # class Father:
# # # #     last_name = "White"
# # # #     def talant(self):
# # # #         print("i can build houses")
    
        
# # # # class Mother(Grandma,Grandpa):
# # # #     last_name = 'Brown'
   
# # # #     def talant(self):
# # # #         print("i'm good at cooking")

# # # # class Child(Father,Mother):
# # # #     pass


# # # # child = Child()
# # # # print(child.last_name)
# # # # child.talant()
# # # # print(Child.mro())

# # # class A:
# # #     def __init__(self,param):
# # #         print(f"Hey,Its A class,I got {param1},{param2}parameters")
    
# # #     def get_letter(self):
# # #         print("aaa")

# # # class B:
# # #     def __init__(self,param):
# # #         print(f"Hey,Its B class, I got {param}papameter")
    
# # #     def get_letter(self):
# # #         print("BBB")

# # # class C(B,A):

# # #     def get_letter(self):
# # #         print("Ccc")
    
# # # c = C("Makers")
# # # c.get_letter()
# # # c.get_letter()
# # # c.get_letter()

# # # # print(C.mro())
# # #         A
# # #     B       C
# # #         D

class A:
    def method(self):
        print('\n'.join(' '.join(*zip(*row)) for row in ([["*" if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8 else " " for col in range(7)] for row in range(6)])))
class B(A):

    def method(self):
        super().method()
        print("")

class C(A):
    
    def method(self):
        super().method()
        print("LOVE YOU")
b = B()
b.method()
c = C()
c.method()
# # #     pass
# # #     # def method(self):
# # #     #     print("Hey, D")              
# # # d =D()
# # # d.method()
# # # # print(D.mro())
# # class Insects:
# #     def __init__(self) -> None:
# #         print ("I m an insect")

# # class Bird:
# #     def __init__(self):
# #         print("I am a bird")



# # class Flymixin:
# #     def fly(self):
# #         print("I can fly")
# # class Butterly(Insects):
# #     pass
# # class Hawk(Bird, Flymixin):
# #     pass
# # class Eagle(Bird,Flymixin):
# #     pass
# # class Piguin(Bird):
# #     pass

# # hawk = Hawk()
# # hawk.fly()

# # eagle =Eagle()
# # hawk.fly()

# # ping = Piguin()
# # butterly = Butterly()
# class Gadgets:
#     pass
# class Shower:
#     pass
# class Vehicle:
#     pass
# class RadioMixin:
#     def play_songs(self,station):
#         print(f'Playing some song on station{station}')

# class Car(Vehicle,RadioMixin):  
#     pass
# class Phone(Gadgets,RadioMixin): 
#     pass
# class ShowerCabin(Shower,RadioMixin):
#     pass

# car = Car()
# phone = Phone()
# showercabin = ShowerCabin()
# car.play_songs(station="Europa +")
# phone.play_songs(station="Makers Bootcamp")
# showercabin.play_songs(station="Karlek") 