class Car:
    __max_speed = 300
    __min_speed = 0
    def __init__(self,current_speed,model) -> None:
        self.current_speed =current_speed
        self.model = model
    def change_current_speed(self,speed):
        if speed > self.__max_speed:
            raise Exception('Too lol')
        self.current_speed = speed 
    def change_max_speed(self,new_speed):
        self.__max_speed = new_speed
    def get_max_speed(self):
        return self.__max_speed

car1 = Car(current_speed= 20,model="bmw")
car1.change_current_speed(40)
print(car1.current_speed)           
#print(dir(car1))
# print(car1._Car__max_speed)
# car1.__max_speed
car1.change_max_speed(555)
car1.change_current_speed(400)
print(car1.get_max_speed())

