def symm_diff(a, b):
    # you could remove duplicates from everything by doing set() for a, b and masterlist
    # this would be more efficient
    masterlist = a + b
    out = []
    for n in masterlist:
        if (n in b and n not in a) or (n in a and n not in b):
            out.append(n)
    return out

a = [4, 4, 6, 11, -2, 3]
b = [5, 11, 11, -3, 3, 5]
print(symm_diff(a, b))