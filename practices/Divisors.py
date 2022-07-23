num = int(input('Give me a number to find divisors for: '))
x = range(2, num)
y = []
for i in x:
    if num % i == 0:
        y.append(i)
print(y)