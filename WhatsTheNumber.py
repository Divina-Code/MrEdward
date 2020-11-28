
from random import randint
gameover = False
computer_number = randint (1,1000000)
lives = 50
while gameover != True:
    print ()
    a = int(input("What's the number?: "))

    if a == computer_number:
         print ("YAY")
         gameover = True

    if a > computer_number:
        lives = lives - 1
        print ("Too big. lives: ", lives)
    if a < computer_number:
        lives = lives - 1
        print("Too small. lives: ", lives)
    if lives == 0:
        print("You loose! The number was", computer_number)
