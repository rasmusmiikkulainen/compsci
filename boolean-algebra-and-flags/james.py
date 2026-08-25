while (day := int(input("enter day of week (1-7): "))) not in range(1, 8):
    print("enter 1-7")

while (vacation := input("is James on vacation? (yes/no): ")) != "yes" and vacation != "no":
    print("enter yes or no")

print(vacation == "yes" or day > 5)