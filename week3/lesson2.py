"""1"""
# def foo():
#     var = "переменная foo"
#     def bar():
#         global var
#         var = "переменная bar"
#     print("переменная в foo: ", var)
#     bar()
# foo()
# print("переменная в foo: ", var)
"""2"""
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу изменяться'
#     print(x)
# print(x)
# my_func() 
# print(globals())
"""3"""
# num = 3
# def mul():
#     global num
#     num = num ** 2
# mul()
# mul()
# mul()
# print(num)
"""4"""
# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount


# def pay_bills(amount, log_name):
#     global balance 
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
    
# def get_balance():
#     global balance
#     n = balance
#     print(f'У вас на счету {n} сом')
    
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()
"""5"""
# result = 0
# def pow_first(x,y):
#     global result
#     result=x ** y
# def pow_second(z):
#     global result
#     result = result % z
    
# pow_first(2, 3)
# pow_second(3)
# print(result)
"""6"""
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control():
#     global a
#     for k,v in a.items():
#         if v >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control'
#             )
# age_control()
"""7"""
# a = ['pipi', 'papa', 'mama']
# b = []
# def slov():
#     global a, b
#     b = [x.title() for x in a]
# slov()
# print(b)
"""8"""
# def count_symbols(string):
#     volwes = 'аеуиоыэёяю'
#     count_volwes = 0
#     count_other = 0
    
#     for i in string.lower():
#         if i in volwes and i.isalpha():
#             count_volwes += 1
#         elif not i.isalpha():
#             count_other += 1
            
#     cunt= len(string) - count_volwes - count_other

#     return f'Количество гласных: {count_volwes}, согласных:{cunt} , остальных символов:{count_other} '    
# print(count_symbols('Мурат супер!'))    
"""9"""
# a = []
# for i in range(0, 11):
#     a.append(i)
# print(a)

"""10"""
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def func():
#     global a
#     for i in a:
#         if i < 7:
#            print(i)
# func()
"""
a = "Это глобалная переменная"
print(a)

def func():
    a = "Это enclosed переменная"
    print(a)
    def inner_func():
        a = "Это Локалная переменная"
        print(a)
    inner_func()

func()
print(a)

num1 = 5
num2 = 4

def sum(a,b):
    global num1
    num1 = a+b
    return a+b
print(sum(num1.num2))
print(sum(num1.num2))
print(sum(num1.num2))
print(sum(num1.num2))

def outter_func():
    print("OUTER")

    def inner_func():
        print("INNER")
    return inner_func
outter_func()()


x  = 0
def counter():
    global x
    print(x)
    x += 1

counter()
counter()
counter()
counter()
"""