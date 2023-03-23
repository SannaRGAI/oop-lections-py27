









#mixins - klassy kot budut ispolzovatsya dlia nasledovanija 
# # no dlia mixinov ne sozdajutsya objekty 
# miksiny - klassy kot slujat dlia rashirenija funkcionalnogo klassa 
# ot miksinov nelzya sozdavat objekty 
# ot  miksinov nelzya. sozdavat objekty 
# 
class WalkMixin:
    def walk(self):
        print("I can walk")

class WalkMixin:
    def walk(self):
        print(" i can walk")


class SwimMixin:
    def swim(self):
        print("i can swim")   

class FlyMixin:
    def fly(self):
        print("i can fly")
class Human(WalkMixin , SwimMixin):
    name = "dude"

    def talk(self):
        print("i can speak ")

class Exocoetidae(SwimMixin):
    name = " can fly"

class Fish(SwimMixin):
    name = "rybka"

class Duck(WalkMixin,SwimMixin,FlyMixin):
    name = "utka"
objects = [Human(),Fish(),Exocoetidae(),Duck()]    
obj =Human()
obj = Exocoetidae
obj.talk()
obj.walk() 
# #print(hasattr(obj,"fly"))
# for obj in objects :
#     #print(obj.name)

#     attrs = ['fly','swim','walk','talk']
#     for attr in attrs:
#         if hasattr(obj,attr):
#             method = getattr(obj, attr)
#             method()


obj = Human()
setattr(obj,"new_attribute","hello world") 
print(dir(obj))
print(obj.new_attribute)
#
#hassattr - function kot prinimaet object i nazv Attribututa vozvrashsaet true esli u objecta est kakoi to attribute (metod)
#getattr - funkciaj kot prinimaet object i nazv attributa 
#setattr  funcia kot prinimaet object nazvanije attributa  i znachenije attributa, dobavliaet novyi atttribut ili perezaprashivaet odnoimennyi attribut







