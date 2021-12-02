"""
dump(), dumps()
"""
# import json
# info = {
#     "name": "Alice",
#     "age": 79,
#     "book":"Chamber of Secrets"

# }
# with open('info.json','w')as my_file:
#     json.dump(info, my_file)

# json_object=json.dumps(info)
# print(json_object)
import json


# json_str = '{"a":[1,"a"],"b":[2,"b"]}'
# file_ = open("main.json","w")
# #json.dump()-->работает с файлом записывает python обект в этот файл
# json.dump(python)

with open('bd.json') as file:
    python_bd=json.load(file)

def login(user = input("v:\n")):
    


    if user in python_bd:
        password = input("p:\n")
        if python_bd[user] == password:
            print('vy uspeshno')
        else:
            print("vy ne uspeshno")
            login(user)
    else:
        print('Takogo user net')
        login(user = input("v:\n"))