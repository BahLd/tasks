"""Задание 2"""
# def get_string_length(string):
#     return(len(string))

# print(get_string_length('Hello'))
"""Задание 3"""
# def get_type(a, b):
#     print(type(a))
#     print(type(b))

# get_type(5, 's')
"""Задание 4"""
# def divide(a, b):
#     return a/b
    
# print(divide(5,10))
"""Задание 5"""
# dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# def dictionary(dict_):
#     return(dict_)
# for key in dict_:
#         print(key)
"""Задание 6"""
# num = 6
# def check(num):
#     if num%2==1:
#         return('It is odd number')
#     else:
#         return('It is even number')
    
# print(check(num))

"""Задание 7"""
# def is_palindrome(string):
#     a = string[::-1]
#     if string.lower() == a.lower():
#        return(True)
#     else:
#        return(False)

# print(is_palindrome('Довод')) 

"""Задание 8"""
# def max_num(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(max_num(10, 12))

"""Задание 9"""
# def multiply_list(a):
#     r = 1
#     for i in a:
#         r = r * i
#     return r
# print(multiply_list([1, 2, 3, 4, 5, 6]))
"""Задание 10"""
def sum_digits(n):
    n_lst = list( str(n) )
    n_sum = 0
    for i in range( len(n_lst) ):
        n_sum += int( n_lst[i] )
    return n_sum
print(sum_digits(105))