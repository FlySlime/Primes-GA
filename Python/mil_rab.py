import random


def findIntegers(n):
    counter = 0
    number = n - 1
    while number % 2 == 0:
        counter += 1
        number //= 2
    return(counter, number)


def millerRabin(n, k):
    for i in range(k):
        print(i)
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return "composite"
        return "composite"
    return "probably prime"
