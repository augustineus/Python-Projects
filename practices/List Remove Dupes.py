import random

a = random.sample(range(0, 25), 20)

def no_dupes(x):
    print(set(x))

no_dupes(a)