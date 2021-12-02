# class X:
#     pass

# obj = X()
# print(dir(obj))
# print(dir(6))
# print(dir('makers'))


# class User:
#     def __init__(self,**kwargs) -> None:
#         print('Object is initializing...')
#         self.name = kwargs['name']
#         self.familia = kwargs['last_name']
#         print('Object is initalized')

# user = User(name='Linus', last_name='Torvalds')
# print(user.name)
# print(user.familia)

# class Human:
#     def __new__(cls,*args, **kwargs):
#         print(args)
#         print(kwargs)
#         instance = super().__new__(cls)
#         instance.heart = '4xкамерное'
#         print('Object created')
#         return instance

#     def __init__(self,name,last_name) -> None:
#         print('Object is initializing...')
#         self.name=name
#         self.familia=last_name

# human=Human(name='Linus', last_name='Torvalds')


# class Sun:
#     instance = None

#     def __new__(cls):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance

# sun1 = Sun()
# sun2 = Sun()
# print(sun1 is sun2)

# class Human:
#     def __init__(self, name,last_name) -> None:
#         self.name=name
#         self.last_name=last_name

#     def get_fullname(self):
#         return f"{self.name} {self.last_name}"


#     def __str__(self) -> str:
#         return self.get_fullname()

# human1= Human('Linus', 'Torvalds')
# print(human1)


# class Human:
#     def __init__(self, name,last_name) -> None:
#         self.name=name
#         self.last_name=last_name

#     # def get_fullname(self):
#     #     return f"{self.name} {self.last_name}"


#     def __str__(self) -> str:
#         return f"{self.name} {self.last_name} - сработал метод str"

#     def __repr__(self):
#         return f"{self.name} {self.last_name} - сработал метод repr"


# human1= Human('Linus', 'Torvalds')
# print(human1)


# class MyInt(int):
#     def __init__(self,value) -> None:
#         self.value=value

#     def __add__(self,other):
#         print('This is my addition')
#         return self.value+other/3

#     def __sub__(self,other):
#         print('This is my substraction')
#         return self.value-other+100

#     def __mul__(self,other):
#         print('This is my Multiplication')
#         return self.value*other-1

#     def __truediv__(self,other):
#         print('This is division')
#         return self.value/other+1

#     def __mod__(self,other):

#         return f"остаток от деления: {self.value%other}"

#     """Отражение арифметические операторы"""
#     # self.value+other, self.value-other
#     # other+self.value, other-self.value

#     def __radd__(self, other):
#         print('This is my r-addition')
#         return other+self.value+20

#     def __rsub__(self, other):
#         print('This is my r-substraction')
#         return other-self.value

#     def __rmul__(self, other):
#         print('This is my r-multiplication')
#         return other*self.value+5

#     def __rtruediv__(self, other):
#         print('This is my r-division')
#         return other/self.value-7    

#     """Составное присваивание"""

#     # a=7
#     # a+=7   == a=a+7

#     def __iadd__(self,other):
#         print('This is my i-addition')
#         return self.value+other

#     def __iadd__(self,other):
#         print('This is my i-substrction')
#         return self.value-other-1

#     def __iadd__(self,other):
#         print('This is my i-multiplication')
#         return self.value**other

#     def __iadd__(self,other):
#         print('This is my i-division')
#         return self.value%other
# a = MyInt()
# print(a+5)

# class Human:
#     def __init__(self, name,familia,age) -> None:
#         self.name=name
#         self.familia=familia
#         self.age=age

#     def __eq__(self,other):
 
#         return self.age==other.age
     
#     def __ne__(self,other):
#         return self.age!=other.age

#     def __gt__(self,other):
#         return len(self.name)>len(other.name) 

#     def __lt__(self,other):
#         return len(self.name)<len(other.name)   

#     def __ge__(self,other):
#         return len(self.familia)>=len(other.familia) 

#     def __ls__(self,other):
#         return len(self.name)<=len(other.name)         

# human1= Human(name='Linus', familia='Torvalds',age=14)
# human2= Human(name='Li', familia='Tolds',age=19)
# print(human1==human2)
# print(human1!=human2)
# print(human1>human2)
# print(human1<human2)
# print(human1>=human2)
# print(human1<=human2)



# class MyCLass:
#     def __init__(self):
#         self.name='makers'
#         # print(self.__dict__)

#     def __getattr__(self,item):
#         print(self.__dict__)
#         return self.__dict__.get(item,'Hello world')

#     def __getattribute__(self,item):
#         print("This is custom getattribute magic")
#         return super().__dict__.get(item)

#     def __setattr__(self,item, value):
#         self.__dict__[item]=value

#     def __delattr__(self,item):
#         self.__dict__.pop(item)
# obj = MyCLass()
# print(obj.name)