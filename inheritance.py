class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        print("Meow")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Frog(Animal):
    def sound(self):
        print("Qua")
animal = Animal()
animal.sound()

cat = Cat()
cat.sound()             



# class Art:
#     students_count = 100
# class Music(Art):
#     students_count = 50

#     def __init__(self):
#         Music.students_count +=1
#         Art.students_count +=1
# class Acting(Art):
#     students_count = 50
#     def __init__(self):
#         Acting.students_count += 1
#         Art.students_count +=1
# student1 = Music()
# student2 = Acting()
# student3 = Acting()
# print(Music.students_count)
# print(Acting.students_count)
# print(Art.students_count)

#super() - vozvrashaet vse metody iz roditelskogo klassa 
# class Human:
#     def __init__(self,name, last_name, id_number):
#         self.name = name
#         self.lastname = last_name
#         self.id =id_number

#     def get_info(self):
#         print(f"{self.name}{self.lastname} id:{self.id}")

# class Employee(Human):
#     def __init__(self, name, last_name, id_number, position, salary):
#         super().__init__(name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         super().get_info()
#         print(f"She works 'as {self.position} and his salary is {self.salary}")    
# employee = Employee(name ="Saliya", last_name="Karymbaeva",
# id_number=777,position="CEO",
# salary= 100000)
# employee.get_info()
# person = Human(name = "John",last_name = "Snow",id_number=678)
# person.get_info()


# class MyDict(dict):
#     def get(self,key,default = "Makers"):
#         print("This method has been changed")
#         return dict.get(self, key, default)

# dict1 = dict(a = 3,b = 5, c = 8)
# print(dict1.get("d"))

# dict2 = MyDict(a = 3,b = 5,c =8)
# print(dict2.get("d"))


# class Parent() :
#     pass 
# class Child(Parent):
#     pass 



# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# #isinstance(obj, class)
# a = A()
# b = B()
# c = C()
# print(isinstance(c,A))
# print(isinstance(c,B))
# print(isinstance(c,))






# class Polygon:

#     sides = "many"

#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         print(self.args)
#         print(self.kwargs)
        
#     def get_perimeter(self):
#         if self.args :
#             return sum(self.args)
#         elif self.kwargs: 
#             return sum(self.kwargs.values())


# class Rectangle(Polygon):

#     sides = 4   # (a+b)*2

#     def __init__(self,a, b):
#         self.a = a
#         self.b = b
#     def get_perimeter(self):
#         return (self.a + self.b) * 2



# rectangle = Rectangle(a = 7,b= 6)
# rectangle2 = Rectangle(a= 9,b= 2)
# print(rectangle.sides)
# print(rectangle.get_perimeter())
# print(rectangle2.get_perimeter())


# class Triangle(Polygon):
#     sides = 3
#     def __init__(self, a, b, c):
#         self.a = a 
#         self.b = b
#         self.c = c

#     def get_perimeter(self):
#         return (self.a +self.b+self.c) *2

# triangle1 = Triangle(a=2,b=3,c=4,)           
# print(triangle1.sides)
# print(triangle1.get_perimeter())

# class Square(Rectangle):
#     sides = "Makers"

#     def __init__(self, a):
#         self.a = a

#     def get_perimeter(self):
#         return self.a *4

# square = Square(a=5)
# print(square.sides)
# print(square.get_perimeter())



    



# polygon = Polygon(a = 9,b = 8,c = 10, d =9, e = 5)
# print(polygon.get_perimeter())
# print(polygon.sides)


# class A:
#     def method (self):
#         print("method in class A")
# object_a = A()
# #obj_a.method()
# #method v klasse a 


# class B(A):
#     pass
# obj_b = B()
# obj_b.method()
# #method. v klasse 
# class C(A):
#     def method(self):
#         print("Method v klasse C")

# obj_c = C()
# obj_c.method()
# #> class a roditelskii 
# #> class b dochernii 
# ###pereopredelenije 
# #>kogda my sozdaem method ili atribut s takim je nazvanijem,kak  i v roditelskih klassah 
# class C(A):
#     def method(self):
#         print ("method v klaase c")

# class A:
#     def method(self):
#         print("Method v klasse A")
#         return "AAA"
# class B(A):
#     def method(self):
#         print("Method v klasse B")
#         return_from_super = super().method
#         print("super().method()vernul().method()")
#         return "BBB"

# obj_a =A()
# res_a = obj_a.method()
# print("A.method vernul", res_a)  

# obj_b = B()
# res_b = obj_b.method()
# print("B.method vernul", res_b)

# class Range:
#     def create(self, n):
# #### prinomaet chislo i vozvrashaet chislo om=t 0 do dannogo chisla vkluchitelno
#         return list(range(n+1))
# class Range10(Range):
#     def create(self):
# #### vozvrashaet  spisok ot 0 do 10 vkluchitelno
#         return super().create(10)
        
# range_obj = Range()
# res = range_obj.create(5)
# print(res)        
# #[0,1 etc 5]

# range10_obj = Range10()
# res = range10_obj.create()
# print(res)
# #[0,1,10]

# # vidy nasledovanija 
# # odinochnoje (kogda odin roditel )
# #mnojestvennoe (kogda neskolko rodotelei)
# #mnogourovnevoje(kogda u roditelia est roditel)
# #ierarhocheckoe (kogda u kajdogo klassa est tolko odin roditel no u roditeljia moject but u roditelia mojet but mnogo detei )
# # gibridnoje(sovmeshenije raznyh vidov nasledovanija)
# #mainly 2 single multiple

# #how to find method or attributes
# class A:
#     attr1 = "a"
#     def method (self):
#         print("method v klasse")

# class B:
#     attr2 = "b"
# def method(self):    
#      print("method v klasse B")       
# class C (A,B):
#     pass 
# obj_c = C()
# print(obj_c.attr1)
# print(obj_c.attr2)      
# obj_c.method()#method v klasse a 

# print(C.mro())

# ### problems mojestvvennogo nasledovanija 
# #1. problema romba (reshennaja s pomoshoju MRO(s versii 2.3))
# # Method reslushion order (prostraivaet poriadok dlia poiska attributov2.3)
# # class A:
# #     pass
# # class B:
# #     pass
# # class C(A,B):
# #     pass

# if __name__ == "__main__":
#     print ("hello")

# #2.problema perekresnogo nasledovanija (ne reshennaja,
# # voznikaet kogda ne vozmojno postroit prioritet roditelei)
 
# class A:
#      pass
# class B:
#      pass
# class C(A,B):
#      pass
# class D(B,A):
#     pass    
# class E(C,D):
#     pass    

# order(mro ) for bases A,