# string1 = "rsgbdh"
# string2 = "sfgdhhhfh"
# print(string1>string2)

# class MyStr:
#     str (1455764)
#     def __init__(self,string):
#         self.string = string

#     def __len__(self):
#         return len (self.string)
#     def __eq__(self,):
#         return len (self) == len(other)


#     def __ge__ (self) == len(other)



#     def __lt__(self,other):
#         return len(self) >len(other)
    


# string1  = MyStr("hello")
# string2 = MyStr("adsfbg")
# print(len(string1.string))
# print(string_obj_1)

class A:
    attr1 = "asfag"

    def __getattribute__(self, name):
       print("__getattribute__",name)
       return

    def __setattr__(self__name: str, __value: Any) -> None:
        print("__setattr__",name, value)
        return super().__setattr__(name,value)

    def __delattr__(self, __name: str) -> None:
        print("__delattr__",name)
        return super().__delattr__(name)    
        pass   
    
    
    obj = A()
    obj.attr1 #obj.__getattribute__("'attr1")
    obj.attr1 = "bbbbb" #obj.__setatttr___('atttr1',"bbbb")

    
    del


