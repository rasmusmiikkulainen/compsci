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