total = int(input("enter total: "))
if total < 17:
    action = "hit"
elif total > 21:
    action = "bust"
else:
    action = "hit"
print(action)
