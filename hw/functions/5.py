def remove(orig, x):
    out = [a for a in orig if a != x]
    while len(out) < 10:
        out.append(0)
    return out

orig = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
x = 4
out = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(remove(orig, x, out))