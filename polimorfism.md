polimorfism  - princip oop, v kototrom metody v raznyh klassah nazyvajutsya odinakovo(odin interfeis )
class Dog:
    def speak (self):
        print("roar")

class Cat:
    def speak(self):
        print("miaw")

class Frog:
    def speak(self):
        print("kwa-kwa")

animals  =[ Cat(),Frog(),Dog(),Frog(),Cat(),Dog()]
for animal in animals:
    animal.speak ()

