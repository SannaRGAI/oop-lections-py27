#Accociation eto princip oop v kot 2 klassa, svyazanany s drug drugom 
#delitsya na 2 principa:
#1 agregacia (weak one)
#2 komposition (stonger one )

class Battery:
    power = 100
    def charge(self):
        if self.power< 100:
            self.power = 100

class Iphone:
    def __init__(self,color) -> None:
        self.color = color
        self.battery = Battery()

# kogda my. sozdaem object ot drugogo klassa priam vnutri drugogo klassa = kompozicija 
#battery = Battery()
# #print(battery.power)
# iphone = Iphone("gold")
# print(iphone.battery.power)

# del iphone
# print(iphone)
iphone =  Iphone("gold")
del iphone 
#bojekt batareiki udaliaetsya vmeste s objektom iphone 

class Nokia :
    def __init__(self,color,battery,) -> None:
        self.color = color
        self.battery = battery 
#kogda my prinimaem uje sozdannyi vne klassa objekt - agregacia 

battery = Battery()
nokia = Nokia("black",battery)

print(nokia.battery.power)

del nokia
# udaliaetsya tolko objekt nokia 
#objekt batarreiki soxraniaetsya 
print(nokia.power)
print(battery.power)

#oop - eto princip pri kot 
