# 3.3
def all_orders(nums):
    out = []
    length = len(nums)
    for m in range(length):
        for n in range(length):
            if not m == n:
                out.append(10 * nums[m] + nums[n])
    return out

testcases = ([3, 7, 4], [5, 6, 5])
for n in testcases:
    print(f"{n}: {all_orders(n)}")