











from datetime import  datetime

class CreateMixin:
    def create(self, todo, key):
        if key in self.todos:
            return "Задача под таким ключом уже существует"
        self.todos[key] = todo

class DeleteMixin:
    def delete(self, key):
        todo = self.todos.pop(key, None)
        if todo:
            return f"удалили {todo}"
        else:
            return f"Задача под ключом {key} не существует"

class UpdateMixin:
    def update(self, key, new_value):
        if key in self.todos:
            self.todos[key] = new_value

class ReadMixin:
    def read(self):
        return sorted(self.todos.items())

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}
    
    def set_deadline(self, deadline):
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
        days_left = (deadline_date - datetime.now()).days
        return days_left


























# from datetime import datetime

# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos:
#             return "Задача под таким ключом уже существует"
#         self.todos[key] = todo

# class DeleteMixin:
#     def delete(self, key):
#         task_name = self.todos[key]
#         del self.todos[key]
#         return f"удалили {task_name}"

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.values())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, deadline):
#         deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
#         today = datetime.today()
#         delta = deadline_date - today
#         return delta.days


# # from datetime import datetime
# # class Clock:
# #     def current_time(self):
# #         print(datetime.now()strftime('%H:%M:%S'))

# # class AlarmClock:
# #     def on(self):
# #         print("Alarm on ")  






























# # class A:
# #     def method(self):
# #         print('\n'.join(' '.join(*zip(*row)) for row in ([["*" if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8 else " " for col in range(7)] for row in range(6)])))
# # class B(A):

# #     def method(self):
# #         super().method()
# #         print("Mailiponchik, s prazdnikom")

# # class C(A):
    
# #     def method(self):
# #         super().method()
# #         print("LOVE YOU")
# # b = B()
# # b.method()
# # c = C()
# # c.method()