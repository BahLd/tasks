# class GrandPa:
#     def talant(self):
#         print('I am good at dancing')

# class GrandMa:
#     def talant(self):
#         print('I am good at singing')
# class Father:
#     last_name = 'White'
#     def talant(self):
#         print('I can build houses')

# class Mother(GrandPa,GrandMa):
#     last_name = 'Brown'


# class Child(Father, Mother):
#     pass

# child=Child()
# # print(child.last_name)
# # child.talant()
# print(Child.mro())

# class Insects:
#     def __init__(self):
#         print("I can't fly")
# class Bird:
#     def __init__(self):
#         print('I am a bird')

# class FLyMixin:
#     def fly(self):
#         print("I can fly")

# class Batterfly(Insects, FLyMixin):
#     pass

# class Hawk(Bird, FLyMixin):
#     pass

# class Eagle(Bird, FLyMixin):
#     pass
# class Pingiun(Bird,Insects):
#     pass
    
    
# hawk = Hawk()
# hawk.fly()

# eagle = Eagle()
# hawk.fly()
# ping=Pingiun()
 
class Vehicle:
    pass

class Gadgets:
    pass

class Shower:
    pass

class RadioMixin:
    def play_songs(self,station):
        print(f"Playing some song on station {station}")

class Car(Vehicle, RadioMixin):
    pass


class Phone(Gadgets, RadioMixin):
    pass

class ShowerCabin(Shower, RadioMixin):
    pass
car = Car()
phone = Phone()
showercabin = ShowerCabin()
car.play_songs(station="Europa+")
phone.play_songs(station="makers")
showercabin.play_songs(station="Retro")