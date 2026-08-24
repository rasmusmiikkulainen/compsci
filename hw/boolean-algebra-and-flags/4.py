integers = [0, 0]

for i in range(len(integers)):
    while (n := input(f"integer {i + 1}: ")).isnumeric() == False or n[0] == "0":
        print("please enter a positive integer")
    integers[i] = int(n)

n = 0
found = False

while not found:
    n += 1
    for i in integers:
        if not n % i == 0:
            found = False
            break
        else:
            found = True

print(n)