total = int(input("enter total: "))
if total < 17:
    print("hit")
elif total in range(17, 22):
    print("stay")
elif total > 21:
    print("bust")
