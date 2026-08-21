# 1.
for i in range(10, 38):
    if i != 37:
        end = ", "
    else:
        end = "\n"
    print(i, end=end)

# 2.
for i in range(998, 899, -2):
    if i != 900:
        end = ", "
    else:
        end = "\n"
    print(i, end=end)

# 3.
for i in range(1, 21):
    if i != 20:
        end = ", "
    else:
        end = "\n"
    if i % 2:
        print(1, end=end)
    else:
        print(-1, end=end)

# 4.
for i in range(1, 61):
    if i != 60:
        end = ", "
    else:
        end = "\n"
    if i % 3:
        print(7, end=end)
    else:
        print(9, end=end)
