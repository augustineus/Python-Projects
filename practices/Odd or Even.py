num = int(input('Give me a number and I\'ll tell you if it\'s odd or even: '))
if num % 2 == 0 & num % 4 != 0:
    print('Your number is even.')
elif num % 2 == 0 & num % 4 == 0:
    print('Your number is even and also divisible by 4.')
else: 
    print('Your number is odd.')

num1 = int(input('Give me a number and I\'ll tell you if it\'s divisible by 2nd number of your choice: '))
num2 = int(input('Give me a 2nd number: '))
if num1 % num2 == 0:
    print(str(num1) + ' is divisible by ' + str(num2) + '.')
else: 
    print(str(num1) + ' is not divisible by ' + str(num2) + '.')