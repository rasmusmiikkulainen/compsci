a = int(input("enter a: "))
b = int(input("enter b: "))

# 1.
if a >= 100 and b <= 50:
    print(1)
else:
    print(0)

# 2. (correct way)
if (a >= 100 and b <= 50) or (b >= 100 and a <= 50):
    print(1)
else:
    print(0)

# 2. (weird way)
if a >= 100:
    if b <= 50:
        print(1)
    else:
        print(0)
elif b >= 100:
    if a <= 50:
        print(1)
    else:
        print(0)
else:
    print(0)