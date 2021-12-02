# """5"""

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f'name: {self.name}, age: {self.age}')

# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty=faculty

#     def display_student(self):
#         print(f'name: {self.name}, age: {self.age}, faculty: {self.faculty}')

# obj_student = Student('Rick', 21, 'science' )
# obj_student.display()
# obj_student.display_student

      
# class ContactList(list):

#     def search(self, name):
#         matching_contacts = []

#         for contact in self:
#             if self.name in contact.name:
#                 matching_contacts.append(contact)
#             return matching_contacts

# class ContactList(list):

#     def search_by_name(self,name):
#         list_ = []
#         for listName in self:
#             if name in listName:
#                 list_.append(listName)
#         return list_

    
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

class SmartPhones:
    def __init__(self, name, color, memory, battery = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery
        
    def __str__(self):
        return f'{self.name} {self.memory}'
        
    def charge(self, a):
        self.a = a
        self.battery = self.battery + self.a
        
        
class Iphone(SmartPhones):
    def __init__(self, name, color, memory, ios):
        super().__init__(name, color, memory)
        self.ios = ios
        
        
    def send_imessage(self, st: str):
        return f'sending {st} from {self.name} {self.memory}'
        
class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android):
        super().__init__(name, color, memory)
        self.android = android
        
    def show_time(self):
        import datetime
        
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        return current_time

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 
print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 
samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 