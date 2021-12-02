# class Soda:
#     def __init__(self, drink):
#         self.drink=drink

#     def show_my_drink(self):
#         if self.drink:
#             print(f'Газировка и {self.drink}')
#         else:
#             print('Обычная газировка')
# soda=Soda('Вода')
# soda.show_my_drink()

# class Nikola:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_name(self,name2):
#         self.name2=name2
#         if self.name == 'Николай':
#             print(self.name)
#         else:
#             print(f'меня зовут не {self.name2}, a Николай')

# nik = Nikola('m',23)
# nik.get_name('bnm')

# class House:
#     def __init__(self, type_h, total_area, remain_area):
#         self.type_h = type_h                    
#         self.total_area = total_area             
#         self.remain_area = remain_area         
#         self.lst_fur = []                      
 
#     def rem_area(self):
#         self.remain_area = self.total_area
#         for fur in self.lst_fur:
#             self.remain_area -= fur.space
 
#     def inform(self):
#         print(self.type_h, self.total_area, self.remain_area, sep=', ')
#         for fur in self.lst_fur:
#             print(fur.name)

# class Furniture:
#     def __init__(self, name, space):
#         self.name = name          
#         self.space = space        
 
# if __name__ == '__main__':
#     f = [Furniture('кравать', 4), Furniture('шкаф-купе', 2), Furniture('стол', 1.5)]

# house1 = House('деревянный', 25)
# house1.lst_fur += [f[0], f[2]]
# house1.rem_area()
# house2 = House('кирпичный', 30)
# house2.lst_fur += [f[0], f[2], f[1]]
# house2.rem_area()
# house3 = House('блочный', 35)
# house3.lst_fur += [f[0], f[0], f[1], f[2]]
# house3.rem_area()
# house4 = House('шлакобетонный', 40)

# house1.inform()
# print()
# house2.inform()
# print()
# house3.inform()
# print()
# house4.inform()
# print()
# student_data_base={}
# class Group:
#     def __init__(self,name_group,mentor,starttime,endtime, leng):
#         self.name=name_group
#         self.mentor=mentor
#         self.starttime=starttime
#         self.endtime=endtime
#         self.leng=leng
#     def add_student(self, student_list):
#         if type(student_list) is list:
#             self.student_list.extend(student_list)
#         else:
#             self.student_list.append(student_list)
    

# class Student:
#     def __init__(self, sum_,man, women):
#         self.sum_=sum_
#         self.man=man
#         self.women=women


"""
Задача 1. Дана функция:
def say_hi ():
    вернуть "питон - хороший язык"
печать (say_hi ())

Написать и применить к ней три декоратора:
Первый декоратор - для приведения всех символов к верхнему регистру
Второй декоратор - для разделения строки
Третий декоратор - для объединения в одно предложение
В результате должно получиться: "PYTHON - ХОРОШИЙ ЯЗЫК"
"""
def верхний (функция):
    def wrapper ():
        вернуть func (). upper ()
    возвратная обертка

def split (func):
    def wrapper ():
        вернуть func (). split ()
    возвратная обертка

def join (func):
    def wrapper ():
        возврат '' .join (func ())
    возвратная обертка
@upper
@присоединиться
@расколоть
def say_hi ():
    вернуть "питон - хороший язык"
печать (say_hi ())



"""Задача 2. Калькулятор
Напишите программу с классом Math. Создайте два атрибута - a и b.
Напишите методы сложение - сложение, умножение - умножение, деление - деление, вычитание - вычитание. 
При передаче в методы параметров a и b с ними нужно выполнять соответствующие действия и печатать ответ.

# класс Math:

# def __init __ (self, a, b):
# self.a = a
# self.b = b

# def add_ (self):
# return self.a + self.b

# num1 = Math (3,3)
# print (num1.add_ ())



"""
Задача 3. Профиль 
Создайте класс профиля из соц сети. У профиля должен быть никнейм, эл. почта и возраст.
Также создайте метод get_info, который выводит информацию о профиле в следующем виде: 
Прозвище: girl_hunter 
Электронная почта: your_hero@gmail.com
Возраст: 12 лет
Объявите экземляр класса и вызовите метод.
"""
# Профиль класса:
#     def __init __ (я, ник, адрес электронной почты, возраст):
#         self.nickname = ник
#         self.email = электронная почта
#         self.age = возраст

#     def get_info (сам):
#         print (f'nickname: {self.nickname} \ nEmail: {self.email} \ nAge: {self.age} ')


# profile = Профиль ('girl_hunter', 'your_hero', '12 лет')
# profile.get_info ()    

"""
Задача 4. Напишите программу с классом Автомобиль. Создайте конструктор класса Автомобиль.
Создайте атрибуты класса Автомобиль - цвет (цвет), марка (тип), год (год). Напишите пять методов.
Первый - запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй - отключение автомобиля - выводит сообщение «Автомобиль заглушен». 
Третий - присвоение автомобилю года выпуска. 
Четвертый метод - присвоение автомобилю бренда. 
Пятый - присвоение автомобилю цвета.
"""
# класс Автомобиль:
# def __init __ (я, цвет, марка, год) -> Нет:
# self.brand = brand
# self.color = цвет
# self.year = год

# def car_on (self):
# print ("Автомобиль заведен")

# def car_off (self):
# print ("Автомобиль заглушен")

# def set_year (self, new_year):
# self.year = new_year

# def set_brand (self, new_brand):
# self.brand = new_brand

# def set_color (self, new_color):
# self.color = new_color

# car1 = Автомобиль («синий», «Хонда», 2010 г.)
# car1.car_off ()
# car1.set_year (2020)
# print (car1.year)

"""
Задача 5. Спортсмены
Создайте классы футболиста и сноубордиста с одинаковым методом skill_info. Для футболиста он печатать "Я могу забить штрафной с 30 метров", для сноубордиста должен "В прыжке я делаю разворот на 360 градусов".
Объявите для каждого из классов по экземпляру. Объявить функцию show_skills, которая будет принимать спортсмена и вызвать у него метод skill_info.
"""
# класс Футболист:
    
# def skill_info (self):
# print ('Я могу забить штрафной с 30 метров')


# class Snowboarder:

# def skill_info (self):
# print ('В прыжке я делаю разворот на 360 градусов')

# foot = Футболист ()
# snow = Сноубордист ()

# def show_skills (a):
# a.skill_info () 

# show_skills (фут)
# show_skills (снег)