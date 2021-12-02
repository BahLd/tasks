# file1 = open('/home/bayaman/python_15/week4/files/lesson.txt', 'r')
# print(file1.read())


# file_ = open('task.txt', 'w')
# file_.writelines(['1', '2', '3', '4',
#  '5', '6', '7', '8', '9', '10']) 
# for line in file_.readlines(5):
#     print(line)


# with open('files.txt', 'w+') as my_file:
#     print(my_file.read())
#     my_file.write('helo wear')
#     print(my_file.closed)


#math, random, datetime
# from math import *
# def rectangle(a, b):
#     return round(a*b, 2)
# def triangle(a, h):
#     return round(0.5*a*h, 2)

# file_ = open('/home/bayaman/python_15/week4/task1.txt', 'r')
# for i in file_.readlines(8):
#     print(i)

with open('task3.txt', 'w') as file:
    file.writelines(range(10)).replace(',','*')
    for line in file.write():
        print(line)