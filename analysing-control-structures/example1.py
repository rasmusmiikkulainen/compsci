a = int(input("please give a: "))
b = int(input("please give b: "))
c = int(input("please give c: "))
ab = a - b
ac = a - c
bc = b - c

if ab * bc > 0:
    result = b
elif ab * ac < 0:
    result = c
else: 
    result = c
print(result)