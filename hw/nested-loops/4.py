linecount = 6

# 1.
for i in range(1, linecount + 1):
    print(i * "*" + (linecount - i) * "-")

# 2.
print()
import math
for i in range(linecount, 0, -1):
    asterisks = math.ceil(i / 2) * "*"
    out = "-".join(asterisks)
    if i % 2 == 0:
        out += "-"
    print(out)