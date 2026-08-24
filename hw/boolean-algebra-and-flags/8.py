# 1.
primes = []
for i in range(2, 100):
    is_divisible = False
    for n in range(2, i):
        if i % n == 0:
            is_divisible = True
            break
    if not is_divisible:
        primes.append(i)
print(primes)

# 2.
primes = []
n = 2
while len(primes) != 100:
    is_divisible = False
    for i in range(2, n):
        if n % i == 0:
            is_divisible = True
            break
    if not is_divisible:
        primes.append(n)
    n += 1
print(primes)