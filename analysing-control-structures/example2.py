x = int(input("enter x: "))
y = int(input("enter y: "))

result = 1
while y > 0:
    if y % 2 == 0:
        # // or /
        y //= 2
        x *= x
    else:
        y -= 1
        result *= x
print(result)