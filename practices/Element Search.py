import random

a = set(random.sample(range(1, 100), 30))

def elem_search(x):
    if x in a:
        print('yes')
    else: 
        print('no')

elem_search(30)