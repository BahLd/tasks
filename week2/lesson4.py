# comprehension

#  '''исползуется когда необходимо обойти последователность
# (строка, список, кортеж, словарь, renge), 
# сделать определенное действие и результат сохранить в новый список.'''
# a = [1,2,3,4]
# res = []
# for i in a:
#      res.append(i * 10)

"""[действие(элемент)  for элемент in последователность]"""
# res = [i * 10 for i in a]

# print(res)

"""Филтировать элементы последователности втновый список"""

# litt1 = [20,65,44,66,5,33,55,73,88]
# # [235505065]
# new_lisst = []
# for num in litt1:
#     if num %3 == 0:
#         new_lisst.append(num)
#         print(new_lisst)

"""[действия(элемент) for элемент in последователность if условие]"""
# new_lisst = [num for num in litt1 if num % 3 == 0]
# print(new_lisst)
# a = [-10, 29, 0, 21, -2, 94, -21, 101,-99]
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [num for num in string_ if num.isdigit]
# print(list_)
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# b = {a : subject for a, marks in dict_.items() for subject, score in marks.items()
# if score == max(marks.values())}
# print(b)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {key: innervalue['a':] for innervalue in my_dict.items()}
# print(dict_)
# list_ = [i / 2 for i in range(1, 11) if i % 2 == 0]
# print(list_)
# b = {1 : 'Hello', 2 : 'World', 3 : 'John'}
# dict_ = {key: len(value) if key % 2 == 0 else len(value) ** 3 for (key, value) in b.items()}
# print(dict_)

# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1/num2
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# else:
#     print(result)
# finally:
#     print('end')
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError
#         print('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')
# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError('Сумма не может быть отрицательной!')
# except ValueError:
#     print('Сумма не может быть отрицательной!')
# else:
#     print(cash)
# inp1 = input()
# inp2 = input()
# try:
#     if inp1.isdigit inp2.isdifit:
#         print(inp1+inp2)
#     else:
    
# except:
#     result+result
# print(result)
# inp1 = input().split()
# list_ = []
# for i in inp1:
#     try:
#         list_.append(int(i))
#         print(list_)
#     except:
#         print('Данный элемент не является числом!')
   
# inp1 = input().split()
# list_ = []
# try:
#     for i in inp1:
#         if i.isdigit():
#             list_.append(int(i))
#         else:
#             raise ValueError
# except ValueError:
#         raise Exception('Данный элемент не является числом!')
import random
attempts = 0
gNumber = random.randint(1,100)
Gname = input('Как вас завут: ')
stop=input("Хатите сыграть(Введите Нет или число): ")


while True:
    if stop == "Нет":
        print("Игра завершино!")
        break
    try:
        guess = int(stop)
        attempts += 1
        if guess < gNumber and guess >0:
            print("Больше \n")
        elif guess > gNumber and guess <=100:
            print("Меньше \n")
    except:
        stop = input("У вас не осталось попыток!")
    if guess == gNumber:
        attempts = str(attempts)
        print(Gname + " Поздравляю, вы нашли его после  " + attempts + " попыток")
        break
    stop = input("Хатите ещё сыграть? ") 