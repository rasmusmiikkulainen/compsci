for i in range(1, 10001):
    factors = []
    for n in range(1, i):
        if i % n == 0:
            factors.append(n)
    if sum(factors) == i:
        print(i)