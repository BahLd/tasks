import random
attempts = 0
gNumber = random.randint(1,100)
Gname = input('Как вас завут: ')
stop=input("Хатите сыграть(Введите Нет или число): ")


while True:
    if stop == "Нет":
        print("Игра завершено!")
        break
    try:
        guess = int(stop)
        
        attempts += 1
        if guess < gNumber and guess >0:
            print("Больше \n")
        elif guess > gNumber and guess <=100:
            print("Меньше \n")
    except:
        stop = input("Нет допустимого ввода, пожалуйста, угадайте еще раз")
        continue
    
    if guess == gNumber:
        attempts = str(attempts)
        print(Gname + " Поздравляю, вы нашли его после  " + attempts + " попыток")
        break
    stop = input("Хатите ещё сыграть? ") 