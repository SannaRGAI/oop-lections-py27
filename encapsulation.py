class Car:
    def _inject_fuel(self):
        print('Fuel injected')


    def __init__bang(self):
        print('Bang!!!')

            
    def _sent_to_ignition_system(self):
        print('Ignition started')
        self.__init__fuel()
        self.__init__bang()

    def _sent_signal_to_pc(self):
        print("Start")
        self._sent_signal_to_ignition_system()


    def start_engine(self):
        self._sent_signal_to_pc()

car = Car()
car.start_engine()

#1 underscore (private)
#protected - my eshe mojem poluchit skrytyje dannye 
#protected dannyje nasledujutsya v dochernih klassah 
class B(A):
b._say_hello()





# # # modifikatory dostupa :
# # # 1.public, (password, get_info)()
# # # 2.protected - _password, _get_info() 
# # #3.private- __password__, __get_info()
# # class User:
# #     def __init__(self,username,password):
# #         self.username  = username
# #         self.__password = password

# #     def get_password(self,username):
# #         if self.username == username:
# #             return self.__password
# #         else:
# #             return"NO!!!"    

# #     def set_password(self,old_password, new_password):
# #         if self.__password == old_password:
# #             self.self.__password  == new_password
# #         else:
# #             return "NO!!!"     
# #         self.__password = value    

# #     def get_info(self):
# #         print(f'username{self.username},password{self.password}') 

# # user1 = User(username="makers123", password="bootcamp567")
# # print(user1.username)
# # print(user1.password)
# # user1.get_info()
# # print(user1.get_password("makers123"))
# # user1.set_password( old_password == "bootcamp576",
# #                     new_password = "helloworld777")
# # print(user1.get_password(username = "qwew"))
# # print(user1.get_password(username = "makers123"))
# class Divider:
#     def __init__(self):
#         self.divide_num = 2
#     @property ### getter 
#     def divider(self):
#         return self.__divide_num
#     @divider.setter ####setter
#     def divider(self,value):
#         if not value == 0:
#             self.__divide_num = value
#             return"Successfully changed divide number"            
#         else:
#             return "NO"

#     def divide(self,value):
#         return value /self.__divide_num

# obj = Divider()
# #obj.__divide_num = 0
# print(obj.divide(7))
# #print(obj.__divide_num)
# print(obj._Divider__divide_num)
# obj.divider= 14
# print(obj.set_divider())

# class Person:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name
        
#         print('initializated')
#     @property
#     def full_name(self):
#         return f'{self.name},{self.last_name}'

# person = Person(name = "John",last_name = "Snow")
# print(person.full_name)
# person.name = "Makers"
# person.age = 2 
# print(person.name)
# print(person.age)


# class A:
#     attr1 = "public"
#     _attr2 = "protected" 
#     __attr3 = "private"   

# print(A.attr1)
# print(A._attr2)
# #print(A.attr3) takogo nazvanija uje ne sushestvujet 
# print(A._A__attr3)

# class Person:
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.__age = age
        
#     def get_age(self):
#         return self.__age

#     def set_age(self, new_age):
#         if new_age >0 and new_age <120:
#             self.__age = new_age
#         else:
#             raise Exception("Invalid age")

# obj = Person("Nastya,12", 12)
# print(obj.name)
# print(obj.get_age())

# obj = Person('Nastya',12)
# print(obj.name)
# print(obj.get_age())
# obj.set_age(45)
# print(obj.get_age())
# #obj.set_age(125)Exception 

# # Getters/Setters
# # >metody s pomoshju kot my ukazyvaem kakim obrazom my mkojem poluchat  i izmeniat kakije to attributy 
# class A :
#     @property
#     def hello(self):
#         return 5 
# # obj = A()
# print        