howMany = int(input('How many numbers should I generate?: '))

def fibNums(int):
    nums = [1, 1]
    first = 1
    second = 1
    newFib = 1
    i = 1
    while i <= int:
        newFib = first + second
        nums.append(newFib)
        first = second
        second = newFib
        i += 1
    print(nums)

fibNums(howMany)