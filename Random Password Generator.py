import random
import string

a = int(input('How many characters do you need your password to be?: '))
b = int(input('How many numbers do you want in it?: '))
c = int(input('How many special characters do you want in it?: '))
d = a - b - c
pw = ''
while len(pw) < a:
    while d > 0:
        pw += random.choice(string.ascii_letters)
        d -= 1
    if len(pw) == a:
        break
    while b > 0:
        pw += random.choice(string.digits)
        b -= 1
    if len(pw) == a:
        break
    while c > 0:
        pw += random.choice('!@#$%^&*')
        c -= 1
    if len(pw) == a:
        break
newPW = ''.join(random.sample(pw, len(pw)))

print(newPW.capitalize())
