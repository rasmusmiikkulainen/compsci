integers = ["a", "b", "c"]

# list comprehension would be more elegant
for i in range(len(integers)):
    while ((n := input(f"enter {integers[i]}: ")).isnumeric() == False
           and not (n.startswith("-") and n[1:].isnumeric())
           or n in integers):
        print("please enter a distinct int")
    integers[i] = n

a = int(integers[0])
b = int(integers[1])
c = int(integers[2])

result = a
if b > result:
    result = b
if c > result:
    result = c

print(result)