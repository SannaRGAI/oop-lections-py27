# class Language:
#     def __init__(self,level,type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self,func_name,arg):
#         return f"def {func_name}({arg}):"

#     def create_variable(self,var_name,value):
#         if type(value) == str:
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"

# class JavaScript(Language):
#     def write_function(self,func_name,arg):
#         skobki = "{     }"
#         return f"function {func_name}({arg}) {skobki};"
        
#     def create_variable(self,var_name,value):
#         if type(value) == str:
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"

# py = Python('high-level', 'interpreted')
# print(py.write_function('len', 'list_'))
# print(py.create_variable('list_', [1, 2, 3, 4]))

# js = JavaScript('high-level', 'interpreted')
# print(js.write_function('len', 'list_'))
# print(js.create_variable('list_', [1, 2, 3, 4]))

# # py = Python('high-level', 'interpreted')
# # print(py.write_function('get_info', 'a'))
# # print(py.create_variable('name', 'Jaanger'))

# # js = JavaScript('high-level', 'interpreted')
# # print(js.write_function('get_info', 'a'))
# # print(js.create_variable('name', 'Jaanger'))



# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = name

#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1

#     def get_level(self):
#         return self.__level

# game = Game('igra')
# print(game.get_level())
# game.play(3)
# game.play(3)
# print(game.get_level())



class Game:
    __level = 0

    def __init__(self, name):
        self.name = self.__validate_name(name)

    def set_level(self, level):
        if self.name == 'Tolik':
            self.__level = level
        else:
            print(f'"{self.name}" ты не Tolik!')
    
    def __validate_name(self, name):
        return name.capitalize()

game = Game('Raychel')
game.set_level(5)
print(game._Game__level)

game2 = Game("TOLIK")
game2.set_level(5)
print(game2._Game__level)