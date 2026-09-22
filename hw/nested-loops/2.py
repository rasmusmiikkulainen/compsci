# 2.3
a = [1, 2, 3, 4, 5]
b = [6]
flag = False
if len(a) >= len(b):
    bigger = a
    smaller = b
else:
    bigger = b
    smaller = a
for n in smaller:
    if n in bigger:
        flag = True
        break
print(flag)