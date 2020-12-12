from random import randint
print("добро пожаловать в игру 21")
eee = int(input("Сколько игроков будет?"))
print()
players = []
for yeet in range(eee):
    name = input("Введите имя " +str(yeet+1)+"-го игрока:" )
    players.append(name)
pointss = []
for points in range(eee):
    random_points = randint(1, 10)
    print(players[points], "Ваш счёт:", random_points)

