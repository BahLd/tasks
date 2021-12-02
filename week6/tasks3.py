"""1"""
# class Product:
#     base_price = 20000
    
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
        
#     def has_garantiya(self, gar):
#         self.gar = gar
#         if self.gar - self.year == 2:
#             return 'Гарантия действительна' 
#         else:
#             return 'Ваша гарантия истекла'
            
#     @classmethod
#     def change_price(cls, price):
#         cls.base_price *= price
        
        
# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price)