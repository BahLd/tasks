# class SomeClass:
#     pass


# class A:
#     pass

# a = A()
# print(isinstance(a, A))

# class Dog:
#     owner = 'John'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name}, {self.age}'
        
#     def bark(self):
#         print('Gav-GAv')


#     def dog_info(self):
#         return f'This id {self.name}, he is {self.age} years old'


#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         return f'{self.name} is {self.age} now '


#     def friends(self,friend):
#         self.friend = friend
#         friend.friend = self



# dog1 = Dog(name='Rex', age=3)
# dog2 = Dog(name='Bobik', age=2)
# dog3 = Dog(name='oreo', age=2)
# dog1.friends(dog2)
# print(dog1.friend)
# print(dog1.friend.name)
# print(dog1.name)
# print(dog2.name)
# dog1.bark()
# print(dog1.birthday())
# print(dog2.dog_info())


# class Rectangle:
#     default_color = 'red'
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def area(self):
#         return self.width * self.length

# rec1 = Rectangle(4,6)
# rec2 = Rectangle(2,7)
# print(rec1.area())
# print(rec1.default_color)

class Car:
    car_count = 0


    def __init__(self):
        Car.car_count += 1
        
car1 =Car()
print(Car.car_count)
car2 = Car()
car3 = Car()
car4 = Car()
car5 = Car()
print(Car.car_count)