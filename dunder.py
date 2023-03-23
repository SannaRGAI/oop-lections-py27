#dunder(double underscore) metody u kot. 2 _ v nachale i v konce
#  magia. v. tom. chto. my ne vyzyem ih na. priamuju,
#  za kajdum metodom chto ot zakrepleno
#  (magic is about that (plas and minus etc happens it self )
class A:
    def __new__(cls):
        print("__NEW__")
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print("__init__")
        pass
A() 
#__NEW__,INIT__ vyzyvajutsya pri sozdanii objekta
print(dir(object))   

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __add__ +
# __sub__ - 
# __floordiv__ /
#__truediv__//
# binarnyje vychislenija 

#__str__ str, print
print(A())

class A:
    def __str__(self) -> str:
            return"Good morinig Sunshine"
    print(A())

class A:
    def __init__(self) -> None:
        self.number = number
    def __eq__(self,other):
        return self.number == other.number

class A:
    def __str__(self) -> str:
            return"A__STR__"

    def__repp__(self):
    return"A__REPR__"

print(A())
            

  

obj1 =A(5)
obj2 =A(5)

print(obj1 == obj2)
print(obj1.__eq__(obj2))

