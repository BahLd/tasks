        
"""
Модификатор доступа:
1. public- password, get_info()
2. protected- _password, _get_info()
3. private- __password, __get_info()

"""



# class User:
#     def __init__(self,username, password):
#         self.username=username
#         self.__password=password


#     def get_password(self,username):
#         if self.username == username:
#             return self.__password
#         else:
#             return "NO!!!"

#     def set_rassword(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#         else:
#             return "NO"

#     def __get_info(self):
#         print(f"Username: {self.username},  password: {self.__password}")

# user1=User(username='bah',password='dsgvf')
# print(user1.username)
# print(user1.get_password(username='bah'))
# user1.set_rassword(old_password='qwerty', new_password="12653112")
# print(user1.get_password(username="ytrewq"))
# print(user1.get_password(username='bah'))


# class Divider:
    # def __init__(self):
    #     self.__divide_num = 1
    #@property
    # def get_divider(self):
    #     return self.__divide_num
    #divider.setter
    # def set_divider(self, value):
    #     if not value == 0:
    #         self.__divide_num = value
    #         return "Successfully change divide number"
    #     else:
    #         return "NO"


    # def divide(self, value):
    #     return value / self.__divide_num

# obj = Divider()
# print(obj.divide)
# print(obj.divide(7))
# print(obj.get_divider)
#obj.divider=14
# print(obj.get_divider)


# from os import name


# class Person:
#     def __init__(self,name, last_name):
#         self.name=name
#         self.last_name = last_name
#     @property
#     def full_name(self):
#         return f"{self.name}, {self.last_name}"

# person= Person(name='john', last_name='snow')
# print(person.full_name())


# class Car:
#     def _inject_fuel(self):
#         print('Fuel injected')


#     def _init_bang(self):
#         print('bang!!')


#     def _send_signal_to_ignition_system(self):
#         print('Ignition started')
#         self._inject_fuel()
#         self._init_bang()


#     def _send_signal_to_pc(self):
#         print('Start')
#         self._send_signal_to_ignition_system()


#     def stat_engine(self):
#         self._send_signal_to_pc()

# car =Car()
# car.stat_engine()
# car._init_bang()

"""
1. underscore
2. protected - мы еще можем получить скрытые данные
3. protected данные наследубтся в дочерних классах
"""