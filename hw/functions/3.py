def read_ints():
    ints = []
    while (a := input("enter integer: ")):
        ints.append(int(a))
    return ints

print(read_ints())