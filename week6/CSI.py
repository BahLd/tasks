"""
Instance method
class method - @classmethod
static method - @staticmethod
"""

# class Makers:
#     language_choices = 'Python', 'JavaScript'

#     def __init__(self,name):
#         self.name=name

#     def instance_method(self):
#         return f"hello. {self.name}"

#     @classmethod
#     def class_method(cls):
#         return f"Welcome to Makers! What type of language do you choose"

#     @staticmethod
#     def static_method(choice):
#         return f"Great! You choose {choice}"
    

# student1 = Makers(name='Lucas')
# print(student1.instance_method())
# print(student1.class_method())
# print(student1.static_method(choice='Python'))
# print('\n')
# student1 = Makers(name='Ashley')
# print(student1.instance_method())
# print(student1.class_method())
# print(student1.static_method(choice='JavaScript'))


# class User:
#     def __init__(self,name,email) -> None:
#         self.name=name
#         self.email=email

#     def get_info(self):
#         return f"{self.name} {self.email}"

#     @classmethod
#     def add_data(cls, user_info:list):
#         name, email = user_info
#         return cls(name, email)
# list_of_users = [
#     ['Emily', 'emi@yahoo.com'],
#     ['Boony','bon@gmail.com'],
#     ['Karen', 'karen@gmail.com']
# ]

# for info in list_of_users:
#     user=User.add_data(info)
#     print(user.get_info())

# class Lottery:
#     def __init__(self,name):
#         self.name=name


#     @staticmethod
#     def _generate_number():
#         import random
#         number=random.sample(list('123456789'), k=5)
#         number = ''.join(number)
#         return number

#     def get_number(self):
#         number = self._generate_number()
#         self.number=number
#         return f"Dear {self.name}! Your lucky number is {self.number}"
# participant1 = Lottery(name='Luca')
# print(participant1.get_number())
# print(participant1.number)
# obj=Lottery('test')
# obj.get_number()


# class Pizza:

#     def __init__(self,ingredients:list) -> None:
#         self.ingredients=ingredients

#     def __repr__(self) -> str:
#         return f"Pizza with {self.ingredients}"


# pizza=Pizza(['tomatoes', 'mozarella', 'basil'])
# print(pizza)
        


class Pizza:

    def __init__(self,ingredients:list) -> None:
        self.ingredients=ingredients

    def __repr__(self) -> str:
        return f"Pizza with {self.ingredients}"
    
    @staticmethod
    def circle_area(radius):
        #pi*r**2
        import math
        area=round(math.pi*radius**2, 2)
        return f"Pizza's area is {area} sm2"

    def area(self, radius):
        self.radius=radius
        return self.circle_area(self.radius)

    @classmethod
    def margarita(cls):
        return cls(['mazarella','tomatoes','basil'])

    @classmethod
    def pepprroni(cls):
        return cls(['pepperoni', 'cheese'])

    @classmethod
    def chilli(cls):
        return cls(['chilli peppers', 'cheese'])

pizza1=Pizza.margarita()
print(pizza1)
print(pizza1.area(4))
print('---------------------')
pizza2=Pizza.pepprroni()
print(pizza2)
print(pizza1.area(8))
print('_____________________')

pizza3=Pizza.chilli()
print(pizza3)
print(pizza1.area(10))
print('&&&&&&&&&&&&&&&&&&&&&')