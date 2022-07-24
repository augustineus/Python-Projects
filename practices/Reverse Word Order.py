words = input('What should I reverse? ')

def reverse(str):
    split = str.split()
    rev_split = split[::-1]
    print(' '.join(rev_split))

reverse(words)