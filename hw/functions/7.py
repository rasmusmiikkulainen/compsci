# 1.
def f(x):
    return 0.5*(x + 2 / x)

def iterate(f, x, n):
    output = []
    current = x
    for i in range(n):
        current = f(current)
        output.append(current)
    return output

x = 1
n = 6
print(iterate(f, x, n))

# 2.
def apply_functions(fs, x):
    for f in reversed(fs):
        x = f(x)
    return x

print(apply_functions(["...".join, str.split, str.lower], "WHAT IS THIS?"))