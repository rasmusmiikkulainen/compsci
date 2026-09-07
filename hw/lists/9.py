# my solution:
def transpose(a):
    transpose = []
    for lst in a:
        for i in range(len(lst)):
            if i == len(transpose):
                transpose.append([])
            transpose[i].append(lst[i])
    return transpose

# ai solution w/ unpacking operator
def transpose2(a):
    transpose = [list(b) for b in zip(*a)]
    return transpose

a = [[1, 2, 3, 4, 5, "test"], [6, 7, 8, 9, 10, "test2"]]
print(transpose(a))
print(transpose2(a))