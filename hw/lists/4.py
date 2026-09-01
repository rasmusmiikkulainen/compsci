words = []
stage = 0

while stage < 2:
    while (a := input("enter word: ")) != "!":
        if stage == 1 and a in words:
            print("hit")
        elif stage != 1:
            words.append(a)
    stage += 1
    if stage == 1:
        print("\nsecond stage")