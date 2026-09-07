words = []
while (a := input("enter word: ")) != "!":
    words.append(a)
indices = []
while (i := int(input("enter index: "))) >= 0:
    indices.append(i)
print("original:", words)
print("indices:", indices)
print("result:", [a for a in words if words.index(a) not in indices])