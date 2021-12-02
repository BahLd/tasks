
"""1"""
# list_ = [1, 2, 3, 4]
# result = sum(list_)
# print(result)

"""2"""
# # list_ = [1, 5, -9, 6, -4] 
# result = all(x > 3 for x in list_)
# print(result)

"""3"""
# list_ = [5, 8, 4, 6, 7]
# result = any(x < 0  for x in list_)
# print(result)
"""4"""
# list_ = [1, 2, 3, 4] 
# result = list(map(lambda x: x ** 2, list_))
# print(result)
"""5"""
# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x%2==0, list_))
# print(result)
"""6"""
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x)>7,list_))
# print(result)
"""7"""
# import functools

# list_ = [5, 6, 7, 8]
# result = functools.reduce(lambda x,y: x*y, list_)
# print(result)

"""8"""
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# even = list(filter(lambda n: n % 2 == 0, list_))
# odd = list(filter(lambda n: n % 2 == 1, list_))
# result = f'even: {len(even)}, odd: {len(odd)}'
# print(result)

"""9"""
# list_ = [-1, 2, 3, 5, -3, 7, ]
# result = list(map(lambda x: x > 0, list_))
# print(result)

"""10"""
# import functools

# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = functools.reduce(lambda x, y: x if len(x)>len(y) else y, list_)
# print(result)


"""
list_a = [1,2,3,4,5,6,7,8,9]
list_b = ['a','b','c','d','e','f','g']
list_c = ['makers','bootcamp','world','zip']


zipped_list = list(zip(list_a, list_b, list_c))
unzipped = list(zip(*zipped_list))
print(unzipped)
print(zipped_list)

sesons = ['spring','winter','fall','summer',]
enumerated_seasons = list(enumerate(seasons))
print(enumerated)


negative = -123
absolute = abs(negative)
print(absolute)

list_of_zeros = [1,2,3,4]
is_true = all(list_of_zeros)
print(is_true)


list_of_zeros = [1,2,3,4]
is_true = any(list_of_zeros)
print(is_true)


ыыы
"""
