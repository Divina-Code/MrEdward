from random import randint
words  = ["австралия", "индия", "китай", "англия", "германия"]
random_index = randint(0, 4)
word = words[random_index]
game = True 
lives = 10 
letters = []
while game:
    mark = 0
    MarkPrinting = ''
    while mark < len(word):
        if word[mark] in letters:
            MarkPrinting = MarkPrinting + word[mark]
        else:
            MarkPrinting = MarkPrinting + " __ "
        mark = mark + 1
    print (MarkPrinting)    
    letter = input("Введите букву или слово: ")

    if len(letter)<1:
        print("Пробел - это пустота")
    elif len(letter) == 1:
        if letter in word:
            if letter not in letters:
                print("Есть такая буква!")            
                letters.append(letter)
            else:
                print("У тебя дежавю.")
                lives = lives - 1 
        else:
            print("Такой буквы нет.")
            lives = lives - 1    
    else:
        if letter == word:
            print("ТЫ ПОБЕДИЛ! Игра окончена.")
        else:
            print("Не угадал! Игра окончена, ТЫ ПРОИГРАЛ")
            print("Слово было ", word, ".")
        game = False
    print("Осталось", lives, "жизней", "Угаданные буквы: ", letters)
    if lives == 0:
        print("Жизни закончились, ты проиграл")
        print("Слово было ", word, ".")
        game = False
