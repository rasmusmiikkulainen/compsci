lst = []
while (i := int(input("enter int: "))) >= 0:
    if i in lst:
        lst.remove(i)
    lst.insert(0, i)

print(lst)