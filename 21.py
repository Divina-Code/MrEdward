from random import randint
print("добро пожаловать в игру 21")
eee = int(input("Сколько будет игроков? "))
players = []
for yeet in range(eee):
    name = input("Введите имя " +str(yeet+1)+"-го игрока: " )
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
            pointss[a] = pointss[a] + randint (1,10)

        elif answer == "НЕТ":
            pass
        else:
            print("А я не понял так да или нет? \n")
    print("__________________________________________")
    for why in range(eee):
        print(players[why],"У вас очков:", pointss[why])
    print("__________________________________________")
