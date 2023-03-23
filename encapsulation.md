encapsulation - princip raboty oop, kot imeet 2. traktovki
1vse, chto nujno blia raboty klassa - lejit v klasse 
2 sokrytije dannyh(ogranichenije dostupa atttributami)

### vidy dostupa: 
public  in python more 
protected more used in  JS , odin uderscore at the beginning 
private 

in python  encopsulatited relizovana na urovne soglashenija
class A:
    attr1 = "public"
    _attr2 = "protected" 
    __attr2 = "private"  

#property.deleter rabotajet kogda my pishem del obj.attr
@hello.setter
def hello(self):
    print("setter")

obj = A()
print(obj.hello)
code ..

#property setter rabotajet kogdamy pishem obj.attr = ...
@hello.deleter
def hello(self):
    print("deleter")

##property 
>decorator, kot prevrahsaet method v attribute s decoratorami getter,setter,deleter
>setter budet vyzyvatsya,kogda my. zapisyvaem v attribut znachenije 
>deleter budet vyzyzvatsya, kogda udaliaem attribut cherez del 

class Person:
    def __init__(self,name,age):
    self.name = name
    self.__age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age)
        if new_age >0 and new_age <120:
            self.__age = new_age
        else:
            raise Exception("Invalid age")

    @age.deleter
    def age(self):
        if self.__age<100:
        raise Exception("Cannot delete age)
        del self.__age


obj = Person("Nasya",12)
print(obj.age) = 34        
print(obj.age)
#obj.age = -100# exception :Invalid age
#del. obj.age = #Exception:Cannot delete age        
    