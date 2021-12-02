# список изменяемый упорядоченый набор произволных элементов
# a = []
# b = list()

# list1 = [1,2,3,4]
# list2 = ['Tom', 'Jack', 'John']
# list3 = [1, 2, None, True]

# В список можно добавлять элементы удалять и заменять

# list1 = [1,2,3,4,5]

# list1 = ['Мясо', "мьилапджиьэ"]

# queue = ['John', 'Tim', 'Ivan', 'Olga']


# queue[0]#'John'
# name_of_list = ['Helloworld!']
# s = name_of_list[0]
# newlist = []
# length = len(s)
# mid = length//2
# if length%2:
#     mid +=1
# f_part = s[:mid]
# s_part = s[mid:]
# newlist.append(list(s_part))
# newlist.append(list(f_part))
# new_list = s_part + f_part
# print(list(new_list))


# list_ = ['world', 'hello']

# list_.remove('world')
# list_.append('world')
# new_list = list_
# print(new_list)

# list_ = ['world', 'hello']
# list_.reverse()
# list_[::-1]
# # list_.remove('world')
# # list_.append('world')
# new_list = list_
# print(new_list)

# suitcase = []
# suitcase.append('Футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0,'панама')
# print(suitcase)
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# nums.pop(0)
# nums.pop(1)
# nums.pop(2)
# nums.pop(3)
# num = []
# num.append(1)
# num.append(1)
# num.append(2)
# num.append(3)
# print(num)
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# nums.pop(0)
# nums.pop(1)
# nums.pop(2)
# nums.pop(3)
# num = []
# num.insert(0, 1)
# num.insert(1, 1)
# num.insert(2, 2)
# num.insert(3, 3)
# print(num)
# list_ =  [1, 2, 3, 4, 5]
# new_list ="'".join(str(list_))
# print(new_list)
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# b = {"базилик"}
# ingredients.add("помидор")
# ingredients.discard("шпинат")
# ingredients.update(b)
# ingredients.pop()
# ingredients.add("сыр моцарелла")
# print(ingredients)
# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#     a[0].update(inp1)
#     a[1].update('default value')
#     a[2].update('default value')
# elif inp2 ==2:
#      a[0].update(inp1)
#      a[2].update('default value')
#      a[0].update('default value')
# elif inp2 ==3:
#      a[2].update(inp1)
#      a[1].update('default value')
#      a[0].update('default value')
# print(a)
a = {'a': 1, 'b': 2, 'c': 1}
b = {}
b = a.copy()
print(a)
