time = int(input("enter time: "))

while ((sun_shining := input("is the sun shining?: ")) != "yes"
       and sun_shining != "no"):
    print("please answer yes or no")

if time in range(10, 17) and sun_shining == "yes":
    print("please use sunscreen")
else:
    print("no need to use sunscreen")