while (n:= input("enter n: ")).isnumeric() == False and n[0] != "0":
    print("please enter positive integer")
n = int(n)

found = False
for i in range(2, n):
    if n % i == 0:
        found = True
        break

if found:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")