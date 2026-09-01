lst = []

while (v := int(input("please give next int: "))) >= 0:
    i = 0
    while i < len(lst) and lst[i] < v:
        i += 1
    lst.insert(i, v)
print(lst)