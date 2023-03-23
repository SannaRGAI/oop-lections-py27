#class/static/instance methods 
# static - ne privyazony 
>instsance methods - eto method kot. perb=vum orgumentom prinimajut ssylku naobject(instance,self)
accepring object ,blia chego ---- chto by chto to delat i rabotat s nim 
ispolzujutsya oni dlia raboty s objektom i ego attributom 
```pyclass A :
    def instance_method(self):
        print("method objecta")
        print("self",self)

obj = A()
obj.instance_method()
#self<_main_.Aobject at 035644yv0>
# kogda my vyzyvajem methid u objekta, to nam nujno peredat v. self,
 on peredajetsya avtomaticheski 
A.instance_method(obj) # not best option  v self priletit to chto 

#method objekta 
```
>**class methods** - methody kot pervym argumentom prinimajut klass (cls)
 use dlia raboty s klassom i ego atttributom 

 in python everything are  objects 

 class kak shablon --- main target for class sozdanije objekta po shablonu 

class A :
    def instance_method(self):
        print("method objecta")
        print("self",self)

obj = A()
obj.instance_method()
#self<_main_.Aobject at 035644yv0>
# kogda my vyzyvajem methid u objekta, to nam nujno peredat v. self, on peredajetsya avtomaticheski 
A.instance_method(obj) # not best option  v self priletit to chto 

#method objekta 

#primery 
class C:
    counter = 0 
    def __init__(self):## object creates 
        C.counter+=1
    def __del__(self):
        C.counter -=1


        @class methods
        def _inc_counter +=1


# dlia sozdanija class methoda nujno ispolzovat decorator "classmethod"
####static methods -- method ,kotoryi ne vzaimodeistvujet. s. objektom ,
#  no pri etom nahoditsya vnutri klassa po principy inkapculiacii.(vse chto nujno dlia )


