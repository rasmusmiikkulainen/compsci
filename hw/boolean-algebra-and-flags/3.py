while (s := input("enter s: ")).isnumeric() == False and s != "0":
    print("please enter positive integer")
s = int(s)

found = False
n = 0

while not found:
    n += 1
    calculation = n**3 - 10*n**2
    if calculation > s:
        found = True

print(f"n = {n}\nn^3 - 10n^2 = {calculation}")