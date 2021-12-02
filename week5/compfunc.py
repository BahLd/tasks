# def get_formatted_name(name, middle_name: None, last_name:'Wick'):
#     """Выводит фамилия  и имя"""
#     if middle_name:
#         return name + ' '+middle_name+last_name
#     return name+' '+last_name
# print(get_formatted_name(name='John',middle_name='Antony').title())

# m=tuple(map(int, ['1','2','3','4','5']))
# print(m)

# f = tuple(filter(lambda x: x%2 ==0, [1,2,3,4,5,6]))
# print(f)

# z = dict(zip([1,2,3], ['a','b','c']))
# print(z)


# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     sum1 = sum(range(start, end+1))
#     return sum1
# print(sum_range(10, 1))


# def seasons(num):
#     months = range(1, 13)
#     if not num in months:
#         raise ValueError
#     elif num in range(3,6):
#         print('Весна')
#     elif num in range(6,9):
#         print('Лето')
#     elif num in range(9, 12):
#         print('Осень')
#     else:
#         print('Зима')
# seasons(2)

# def date(day, month, year):
#     if day <1 or day > 31:
#         raise ValueError("Wrong day")

#     if month < 1 or month > 12:
#         raise ValueError('Wrong month')
    
#     if month < 0 or month > 2022:
#         raise ValueError('Wrong year')
#     return True

# print(date(2,12,2021))

# num =[x for x in range(70,101) if x%2 ==1]
# print(num)

# names = ['kjfdsg;lj','dkjfgslkdfh','hgfdskfg','kol']
# name = [x for x in names if len(x)<=5]
# print(name)

# nums = [2,75,5,3,25]
# num = [n*2 if n< 5 else n-2 for n in nums]
# print(num)

# x = int(input("Number: "))
# nums =[str(i**2) + '\n' for i in range(0,int(x))]
# print(nums)

# list_ = list(range(1, 11))
# x = ['четные' if i%2 == 0 else i for i in list_]
# print(x)

# fruits = {'apple': 25, 'banana': 40, 'mango': 17, 'orange': 12}
# dict_ = {k:list(range(1, v+1)) for k, v in  fruits.items()}
# print(dict_)