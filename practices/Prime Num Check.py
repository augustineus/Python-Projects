def check_prime(x):
    y = range(2, x)
    z = []
    for i in y:
        if x % i == 0:
            z.append(i)
    if z == []:
        print('Prime.')
    else:
        print('Not a prime, your number is divisible by', z)

num = check_prime(int(input('Give me a number to check for primality: ')))