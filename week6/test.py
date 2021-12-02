# #1
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year =year

#     def show_info(self):
#         print(f'Название песни {self.title},Автор: {self.author}, вышла в {self.year} году')

# song = Song('Happy', 'Pharrel Williams', 2013)
# song.show_info()




# """"2"""
# class Circle:
#     pi=3.14
#     color='синий'

#     def __init__(self, raduis):
#         self.radius=raduis

#     def get_area(self):
#         return self.pi*self.radius**2

    
# circle= Circle(2)
# print(circle.get_area())
#print(circle.color)


# 3 Task
# class MyString:
#     def __init__(self, string) -> None:
#         self.string = string

#     def append(self, string2):
#         self.string = self.string + string2

#     def pop(self):
#         popped = self.string[-1]
#         self.string = self.string[:-1]
#         return popped

#     def __str__(self) -> str:
#         return self.string

# example = MyString('String')
# example.append('hello')
# example.pop()
# print(example)


# 4
# class MyDict(dict):
#     def get(self, key, default = 'Are you kidding?'):
#         return super().get(key, default)

# obj_dict = MyDict({'a':1})
# print(obj_dict.get('b'))


#Task 5

# class ContactList(list):

# list_ = ['John', 'Denny']

#     def __init__(self, name):
#         self.name = name

#     def search_by_name(self):
#         return list_

# all_contacts = Contact_list()
# all_contacts.search_by_name


# 6
# class Car:
#     def get_speed(self, speed):
#         self.speed = 0

#     def show_speed(self):
#         return sel



# 7
class RadioMixIn():
    def play_music(self, title):
        self.title = title


class Auto(RadioMixIn):
    pass


class Boat(RadioMixIn):
    pass


class Amphibian(Auto, Boat):
    pass

auto = Auto('hello')
auto.play_music()
boat = Boat('tt')
boat.play_music()
obj = Amphibian('hh')
obj.play_music()



class MyList(list):
    def gh(self, index):
        self
