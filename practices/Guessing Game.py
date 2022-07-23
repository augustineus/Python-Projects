import random
start = input("Do you want to play a guessing game? Y/N: ")
a = random.randint(0, 10)
c = 0
if start == 'N':
     print('Done already? Ok.')
while start == 'Y':
    b = int(input("Guess a number between 0 and 10: "))
    c += 1
    if int(a) > b:
        print("You guessed too low!")
        again = input('Keep guessing? Y/N: ')
        if again == 'Y':
            start = 'Y'
        else:
            start = 'N'
    elif int(a) < b:
        print("You guessed too high!")
        again = input('Keep guessing? Y/N: ')
        if again == 'Y':
            start = 'Y'
        else:
            start = 'N'
    elif int(a) == b:
        print("You guessed correctly!")
        print('You guessed', c, 'times')
        start = input("Do you want to play again? Y/N: ")
    else:
        print("I didn\'t understand you, try again!")
    if start == 'N' or again == 'N':
        print('Done already? Ok. You guessed', c, 'times.')
        break
