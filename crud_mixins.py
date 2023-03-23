# class Parent:
#     def who_am_i(self):
#         print("i m a parent")

# class Child(Parent):
#         def who_am_i(self):
#             super().who_am_i()
#             print("i m a child")

# child = Child()
# child.who_am_i()            
class Grandpa:
    def talant(self):
        print("i m good at dancing")
class Grandma:
    def talant(self):
        print("i m good at singing")

class Father:
    last_name = "Ekstrand"
    
    def talant(self):
        print("i can build houses")

class Mother(Grandma,Grandpa):
    last_name = "Mattias" 

class Child(Father,Mother):
    pass 
child = Child()
print(child.last_name)
child.talant1()
child.talant2()
child.talant3()



#class CreateMixin:
#     def product_create(self,title,price):
#         #self__class__ - obrashenije k klassu, kot nasledovalsya ot etogo miksina
#         model = self.__class__
#         obj = model()
#         _id = model._id
#         obj.title = title
#         obj.price = price
#         obj.id = _id
#         model.objects[_id] = obj
#         model._id += 1

# class Readmixin:
#     def product_detail(self,p_id):
#         model = self.__class__
#         obj = model.objects.get(p_id)
#         print({"id":obj.id,"obj.title":obj.title,"price":obj.price})
    
# class UpdateMixin:
#     def product_update(self,p_id, title, price):
#         model = self.__class__
#         obj = model.objects.get(p_id)
#         obj.title = title
#         obj.price = price
# class DeleteMixin:
#     def delete_product(self,p_id):
#         model = self.__class__
#         model.objects.pop(p_id)
# class ProductCrud(CreateMixin, Readmixin, UpdateMixin,DeleteMixin):
#     objects = {}
#     _id = 1

# crud  = ProductCrud()
# crud.product_create("Samsung Note 20 Ultra",50000)
# crud.product_detail(1)

# crud.product_create("Iphone 14 Pro Max", 10000)
# #crud.product_update(2,'Iphone14 pro Max',120000)
# #crud.product_detail(2)

# class ProductCrud(CreateMixin,Readmixin):
#     object  = {}
#     _id = 1

# crud = ProductCrud()


