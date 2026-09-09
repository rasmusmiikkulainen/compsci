def share(a, b):
    found = False
    for i in a:
        for q in b:
            if i == q:
                found = True
                break
        if found:
            break
    return found

a = [1, 2, 3]
b = [3, 4, 5, 6]
print(share(a, b))