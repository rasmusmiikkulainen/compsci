while (calc := input("calculate: ")):
    [a, op, b] = calc.split()
    a = float(a)
    b = float(b)
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    print(result)