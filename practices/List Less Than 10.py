a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
#for i in a:
#    if i < 5:
#        x.append(i)
# print(x)

#above is the mutliline way of solving this challenge, below is single line
print([x for x in a if x < 5])