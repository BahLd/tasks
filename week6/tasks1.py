"""1"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')
        
# class Boat:
#     def swim(self):
#         print('Floating on water')
        
# class Amphibian(Auto,Boat):
#     pass
# obj = Amphibian() 
# obj.ride() 
# obj.swim() 
"""2"""
# class RadioMixin:
#     def play_music(self,title):
#         print(f"Песня называется {title}")

# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')
        
# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')
        
# class Amphibian(Auto,Boat,RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian() 
# auto.play_music(title="song")
# boat.play_music(title="ads")
# obj.play_music(title="bool")

"""3"""
# class Clock:
#     def current_time(self):
#         import time
#         print(time.strftime("%H:%M:%S"))
                
# class Alarm:
#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         print('Будильник выключен')

# class AlarmClock(Clock,Alarm):
#     def alarm_on(self):
#         super().on()

# clock=AlarmClock()
# clock.current_time() 
# clock.alarm_on() 

"""4"""

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0
    
#     @abstractmethod
#     def get_info(self):
#         pass
    
#     @abstractmethod
#     def coding(self):
#         pass
    
# class Backend(Coder):
#     def __init__(self,languages_backend, experience):
#         self.experience = experience
#         self.languages_backend = languages_backend
        
#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование\n'


#     def coding(self, t):
#         self.count_code_time += t
        

# class Frontend(Coder):
#     def __init__(self,languages_frontend,experience):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
        
#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование\n'


#     def coding(self, t):
#         self.count_code_time += t
        
        
# class Fullstack(Backend, Frontend):
#     pass


# a = Backend('Python', 'Junior')
# b = Frontend('JavaScript', 'Middle')
# c = Fullstack('Python and JS', 'Senior')

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())
"""5"""
class Square:
    def init(self, side):
        self.side = side

    def get_area(self):
        return self.side  2

class Triangle:
    def __init__(self,height, base):
        self.height = height
        self.base = base

    def get_area(self):
        return int(0.5 * self.height * self.base)


class Pyramid(Triangle, Square):
    def __init__(self, height, base):
        super().__init__(height, base)
        
    def get_volume(self):
        from math import sqrt 
        pyramid_height = sqrt(self.height**2 - (self.base / 2)**2)
        volume =int(1/3*self.base**2*self.height)
        return volume


c = Pyramid(2, 3)
print(c.get_volume())

"""6"""
class CreateMixin:
    def create(self,date,key):
        pass

class DeleateMixin:
    pass

class UpdateMixin:
    pass

class ReadMixin:
    pass

class Todo(CreateMixin,DeleateMixin,UpdateMixin,ReadMixin):
    todos = {}
    def __init__(self) -> None:
        pass


    def set_deadline(self,date):
        self. 