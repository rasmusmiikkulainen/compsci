integers =[]
while (i := int(input("enter next int: "))) >= 0:
    integers.append(i)
print(integers)
new_lst = []
for i in integers:
    if i not in new_lst:
        new_lst.append(i)
        print(i, end=" ")
