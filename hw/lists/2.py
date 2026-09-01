positives = []
negatives = []

while True:
    while (not (v := input("enter next int: ")).isnumeric()
        and not (v.startswith("-") and v[1:].isnumeric())):
        print("please enter int")
    v = int(v)
    if v == 0:
        break
    elif v > 0:
        positives.append(v)
    else:
        negatives.append(v)

print(f"{positives}\n{negatives}")