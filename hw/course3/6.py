# 1.
w = 4

# 2.
w = 11

# 3.
w = int(input("enter w: "))

if w <= 2:
    p = 3
elif w <= 5:
    p = 3 + (w-2) * 2
elif w > 5:
    p = 3 + 3 * 2 + (w - 5) * 3

print(p)