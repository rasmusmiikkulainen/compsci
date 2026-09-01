integers = [0, 0]

for i in range(len(integers)):
    while (n := input(f"integer {i + 1}: ")).isnumeric() == False or n == "0":
        print("please enter a positive integer")
    integers[i] = n

lastdigit = integers[0][-1]
integers.pop(0)
samedigit = True

for i in integers:
    if i[-1] != lastdigit:
        samedigit = False
        break

print(samedigit)