def hello_makers():
    print("Hello,Makers!")

# makers =  hello_makers
# print(id(makers))
# print(id(hello_makers))
# opredelit f vnutri drugoi funkcii 

def outer_func():
    def inner_func():
        print('Hello,Makers')
    inner_func()

    #peredovat funkcii v kachestve argumenta 
    # i vozvrashat ix iz drugih funkcii
def main_func(func):
    print(f'ja poluchila funkciju{func}v kachestve argumenta')
    func()
    return func

    print(main_func(hello_makers))
    ### decoratory -- eto f kot helps to use another f without root changes 
 # f kot oborachivaet druguju funkciju  bez izm samogo koda f

def func1():
    print("I'm called inside other function")

def func2(func):
    print("I'll do something before func calling")
    func()

def func3():
    print('Hello,Makers!!!!')

func2(func3)

def decorator(func):
    print("ja - funcija - decorator")
    def wrapper():
        print("ja - funcija- obertka")
        print("vyzyvajem obernutuju funkciju")
        func()
        print("vyhoju iz obertki")
        return func1
    return wrapper     
@decorator
def hello_makers():
    print("Hello,Makers")  

hello_makers()      