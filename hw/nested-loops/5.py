def uniques(numbers):
    uniques = []
    for n in numbers:
        if n in uniques:
            return False
        uniques.append(n)
    return True

testcases = ([1, 2, 3, 4, 4], [1, 2, 3])
for i in testcases:
    print(f"{i}: {uniques(i)}")