def alternate(lst):
    iter_length = len(lst) // 2
    if len(lst) % 2 != 0:
        iter_length += 1

    alt = []
    for i in range(iter_length):
        alt.append(lst[i])
        if i == 0:
            alt.append(lst[-1])
        elif i != len(lst) // 2:
            alt.append(lst[-(i + 1)])

    return alt

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(alternate(lst))