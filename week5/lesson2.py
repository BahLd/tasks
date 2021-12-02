# class Phone:
    # model = 'Xiaomi Mi 11'
    # size = 5.5
    # color = 'black'
    # ram = 6
    #Атрибуты класса
#     operating_system = 'Android'
#     def __init__(self,model, size, color, ram, memory):
#         #Атрибуты обекты экземпляра класса
#         self.model = model
#         self.size = size
#         self.color = color
#         self.ram = ram
#         self.memory = memory
#     def call(self):
#         pass
#     def play_video(self):
#         pass
# phone1 = Phone('Samsung Galaxy s21', 6.5, 'gold', 8, 256)


# phone2 = Phone('Xiaomi Mi 10', 5.0, 'black', 6, 128)

class Taxi:
    def __init__(self,name: str,cost: int,cost_km: int):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km

    def get_total_cost(self,km):
        self.km = km
        full_cost = (self.cost*km) + self.cost_km
        return f'Такси {self.name}, стоимость поездки: {full_cost} сом'
    
taxi1 = Taxi('Namba', 17, 9)
taxi2 = Taxi('Yandex', 20, 7)
taxi3 = Taxi('Jorgo', 17, 0)

print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))