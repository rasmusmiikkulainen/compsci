n = 1
found = False
while not found:
    if (n ** 3 - 16) % 47:
        n += 1
    else:
        found = True
print(n)
