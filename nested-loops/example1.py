howmany = 7
for i in range(howmany + 1, 1, -1):
    numbers = []
    for n in range(1, i):
        numbers.append(n)
    print(*numbers)

k = howmany
for row in range(howmany):
    for number in range(1, k + 1):
        print(number, end=" ")
    k -= 1
    print()