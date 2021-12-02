

# hello_makers()
# makers = hello_makers
# makers
#определит функции внутри функции

# def outer_func():
#     def inner_func():
#         print('hello, Makers')
#     inner_func()

# outer_func()

# def main_func(func):
#     print(f'Я получила функцию {func} в качестве аргумента')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers!')


# print(main_func(hello_makers))

"""Декораторы"""
# def func1():
#     print("I'm called inside other function")

# def func2(func):
#     print("I'll do something before func calling")
#     func()

# def func3():
#     print('Hello, Makers!!!!!!!')

# func2(func3)


# def decorator(func):
#     print("Я - функция-декоратор")
#     def wrapper():
#         print("Я - функция-обертка")
#         print("Вызываем обертнутую функцию")
#         func()
#         print("Выхажу из обертки")
#         return func

#     return wrapper

# @decorator
# def hello_makers():
#     print("Hello Makers")

# @decorator
# def hello_bootcamp():
#     print("This is bootcamp")

# hello_makers()


# def check_password(func):
#     def wrapper():
#         return func().strip()
#     return wrapper


# @check_password
# def get_password():
#     password = input('Enter password: ')
#     return password


# @check_password
# def get_email():
#     email = input('Enter email: ')
#     return email


# print(get_password())


# def bread(func):
#     def wrapper(*args):
#         print("</-------\>")
#         func(*args)
#         print('<\_______/>')
#     return wrapper


# def ingredients(func):
#     def wrapper(*args):
#         print('#tomato#')
#         func(*args)
#         print("--salad--")
#     return wrapper


# @bread
# @ingredients
# def get_sandwich(*fillers):
#     for filler in fillers:
#         print(filler)

# get_sandwich('--ham--', '**sausages', '&ketchup&')


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"See what I got: {args}")
#         print(f"See what I got: {kwargs}")
#         func(*args, **kwargs)
#     return wrapper

# @decorator
# def func_without_params():
#     print("I'm a poor func without params")
# func_without_params()
# @decorator
# def func_with_params(name, last_name):
#     print("I'm a happy func with params")
#     print(f"Hello, {name} {last_name}")

# func_with_params('Sam', last_name='White')


from requests.api import get


def benchmark(iters: int) -> int:
    def actual_decorater(func):
        import time
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                func_call = func(*args, **kwargs)
                end  = time.time()
                total  = total + (end - start)


            print(f'Average complate time: {total}')
            return func_call
        return wrapper
    return actual_decorater

@benchmark(iters=10)
def get_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

get_webpage(url='http://yandex.ru')


