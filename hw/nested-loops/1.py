# 1.
for i in range(5):
    print(1, 2, 3, 4, 5)

print()
# 2.
for i in range(1, 6):
    for i in range(i, i+5):
        print(i, end=" ")
    print()