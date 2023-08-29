import random
words = ['word','ahmad','ali','mohammad','omid','wather','notebook']
word = random.choice(words)
def hangman():
    turn = 6
    guses = []
    while turn>0:
        guse = str(input('enter your guse'))
        guses.append(guse)  
        failed =0
        for char in word:
            if char in guses:
                print(char,end='')
            else:
                print("-",end="")
                failed += 1
        if failed ==0:
            print('\n you win')
            break


        guse = str(input('enter your guse'))
        guses.append(guse)    

        if guse not in word:
            turn -= 1
            print('worng guse')
            print('you have ', turn, 'chanse')
            if turn ==0:
                print('you lose ', word)




hangman()