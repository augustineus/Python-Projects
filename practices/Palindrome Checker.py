pal = input('Give me a word and I\'ll check if it\'s a palindrome: ')
check = pal[::-1]
if pal == check:
    print('Your word is a palindrome.')
else:
    print('Your word is not a palindrome.')