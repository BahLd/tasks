# #модификаторы:
# class Phone:

#     def __init__(self,imei, os, battery=0):
#         self.imei=imei
#         self.os=os
#         self._battery=battery

#     def get_imfo(self):
#         self._battery-=0.5
#         return f'{self._imei} {self.os}'

#     def music(self):
#         self._battery -= 5
#         print('Прослушивется музыка')

#     def video(self):
        
#         self._battery -=7
#         print('Просматриввается видео')

    

class A:
    def method(self):
        print("a")

class B:
    def method(self)