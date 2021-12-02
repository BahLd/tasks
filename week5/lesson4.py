#полиморфизм - возможность функции работать с обектами разных типов при условии того что обект
#  поддеживаает оперцию(обект обладет нужным методом)
# a = 1
# b = 2

# a+b

class A:
    def __init__(self, attr1):
        self.attr1=attr1

    def __add__(self, other):
        return self.attr1+ other.attr1


a1=A(10)
a2=A(20)

print(a1+a2)

class A:
    def __init__(self, value):
        self.value=value

a1=A(10)


class Square:
    def __init__(self, side):
        self.side=side

    def ares(self):
        return self.side ** 2


class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        from math import pi
        return pi*self.radius**2
        







def get_shape_area(shape):
    shape.area()
        
