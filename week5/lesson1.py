# a = 4
# b = '123'
# c = [1,2,3]



# def func1():
#     print('Hello world')

# a = func1

# a()

# Функция можно передовать в качестве аргумента и возвращать в качестве резултать
#  также внутри функции могут определяться локалные функции
# def funс1():
#     pass

# def func2():
#     pass
# func2(func1)

# def func1():
#     def func2():
#         print('Hello world')

def timer(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            total_time = 0
            for i in range(n):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                working_time = end - start
                total_time += working_time
            avg_time = total_time / n
            print(f'Время выполнения функции: {avg_time* 1000} миллисекунд')
            return result
        return wrapper 
    return decorator



@timer(100)
def func1():
    print('hello')

@timer(100)
def func2(x, y):
    print(x * y)

@timer(100)
def func3(list_):
    print(sum(list_))

func1()
func2(10, 20)
func3([1, 2, 3, 4])