```py
class A:
    def method (self):
        print("method in class A")
object_a = A()
obj_a.method()
#method v klasse a 


class B(A):
    pass
obj_b = B()
obj_b.method()
#method. v klasse a 
````
class C(A):
    def method(self):
        print("Method v klasse C")

obj_c = C()
obj_c.method()
```py
class A:
    pass
class B:
    pass
class C(A,B):
    pass
```
# do mro [C,A]
if __name__ == "__main__':
    print("hello")
    
 ```.py
 class A:
     pass
class B:
     pass
class C(A,B):
     pass
class D(B,A):
    pass    
class E(C,D):
    pass    
```
   
