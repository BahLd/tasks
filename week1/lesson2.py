#строка- тип храняший текст
#строка -  неизменямый упорядоченый набор символов

# a1='Stroka'
# a2 =" Stroka"
# a3 = '''Stroks's '''
# a4 = """Stroks's """

# str1 = ''
# str2 = str()

#проверочный методы

#is...()

#isdigit() - проверяет что все символы в строке явля циврами
# a='sdkjhflk'
# b=' 12354'
# a.isdigit()#false
# b.isdigit()#True

# isdecimal()
# isnumeric()

# isaipha()- проверяет сто все символы явля буквенным
# a='trf'
# b='привет'
# c='Hello world'
# print(a.isalpha())
# print(b.isalpha())
# print(c.isalpha())


# isalnum()- проверяет букво или цифра
# a='test'
# b='test2
# c='tect 3'


# isupper(), islower()- проверяет все буквеные символы нижнем/ верхнем регистре

# a1='hello'
# a2='Hello123'
# a3='My string'
# a4='TEST STRING'
# a5='hello1234'

# a1.islower() True
# a1.islower() False
# a1.islower()False
# a1.islower()False
# a1.islower()False
# a1.islower()True


# a1.islower() True
# a1.islower() False
# a1.islower()False
# a1.islower()False
# a1.islower()False
# a1.islower()True

# capitalize()- преобразует первую букву в верхний регистр

# split()- разбивает строку по разделителю
# a='tilek ermek janyl'
# join()- объединяет список из строк в одну строку
# replace() - заменяет один  или несколько (группу) символов
I = ord('I')
num = int(input())
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')
if a<=num<=z or A<=num<=Z:
    print(f"Это буква {chr(num)}")
else:
    print(f"Это не буква, а символ {chr(num)}")
count = 0
number = int(input())
if number >= count:
    print(f"count = {number}")
else:
    ...