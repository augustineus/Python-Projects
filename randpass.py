import random
import string

a = int(input('How long do you want your password to be?: '))
pw = ''
while len(pw) < a:
    pw += random.choice(string.ascii_letters)
    pw += random.choice(string.digits)
    pw += random.choice(string.punctuation)
    if len(pw) == a - 1:
        break
print(''.join(random.sample(pw, len(pw))))
