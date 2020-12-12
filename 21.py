from random import randint
print("добро пожаловать в игру 21")
eee = int(input("Сколько будет игроков? "))
print()
players = []
for yeet in range(eee):
    name = input("Введите имя " +str(yeet+1)+"-го игрока: " )
eee = int(input("Сколько игроков будет?\t"))
print()
players = []
for yeet in range(eee):
    name = input("Введите имя " +str(yeet+1)+"-го игрока:\t" )
    players.append(name)
print("Игроки: ", players)
pointss = []
for points in range(eee):
    random_points = randint(1, 10)
    pointss.append(random_points)
    print(players[points], "Ваш счёт: ", random_points)
print("Очки:",pointss)
game = True
while game:
    for a in range(eee):
        answer = input(players[a]+" Будите брать карту? [Да/Нет] \n")
        answer = answer.upper()
        answer = answer.strip()
        if answer == "ДА":
            pass
        elif answer == "НЕТ":
            pass
        else:
            print("А я не понял так да или нет? \n") 



