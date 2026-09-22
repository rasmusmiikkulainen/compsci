flights = ["AY664", "BA047", "AF110", "LH554", "AY101"]
airlines = ["AY", "BA", "AF", "LH", "UA"]
for i in airlines:
    print(i, end=": ")
    for n in flights:
        if n.startswith(i):
            print(n, end=" ")
    print()