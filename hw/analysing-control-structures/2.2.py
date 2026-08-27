def fun(x):
    flag = True
    i = 2
    print(len(x))
    while flag and i < len(x):
        result1 = x[i] - x[i - 1]
        result2 = x[i - 1] - x[i - 2]
        if result1 != result2:
            flag = False
        else:
            i += 1
    print(i)
    print(result1)
    print(result2)
    print(flag and i < len(x))
    return flag

k = [2, 4, 6, 8, 10]
print(fun(k))