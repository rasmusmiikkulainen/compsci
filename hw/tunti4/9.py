largest = 1
solution = 1
previous = 1

for t in range(101):
    test = t * (t - 20) * (t - 100) + 120000
    if (previous - test) > largest:
        solution = t
    previous = test

print(solution)