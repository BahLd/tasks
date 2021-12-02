# Словари

# служит для писания обектов

#  словар неупорядечная изменяемая последовательност элементов вида ключ: значение

# ключи в словаре должен быть уникальным 

# a = {}
# b = set{}
# c = dict()

# a = {'a': 1, 'b': 2}

# b = {[1,2,3]: 'value'} #ошибка

#  dict1 = {'a': 1, 'b': 2}
#  dict2 = {1: 'value1', 2:'value2'}
#  dict3 = {(1,2,3): '1',  }

# some_dict = {'a': 1, 'b': 2, 'a': 3}
# print(some_dict) # {'a': 3, 'b': 2}

# headphones = {'brand': 'hoco', 'model': 'Air v28', 'color': 'white', 'type': 'wireless'}

# headphones['brand'] # 'Hoco'
# headphones['type'] # 'wireless'
# headphones['volume'] # KeyError



n = int(input())
dict_ = {num: num**2 for num in range(1, 501) if n % n == 0}
print(dict_)