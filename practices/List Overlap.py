a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

#if len(a) > len(b):
#    for x in a:
#        if x in b:
#            c.append(x)
#elif len(a) < len(b):
#    for x in b:
#        if x in a:
#            c.append(x)
#print(c)

print([x for x in set(a) if x in b])
#fancier solution/list comprehension to provide overlap without duplicates