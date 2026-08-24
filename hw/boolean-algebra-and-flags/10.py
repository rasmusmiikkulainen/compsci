import math
import random

# 1.
r1_x = ((-1 - 1) ** 2) ** 0.5
r1_y = ((-1 - 1) ** 2) ** 0.5
r2 = math.pi * 1 ** 2
ratio = r2 / (r1_x * r1_y)
print("ratio of r1 and r2:", round(ratio, 4))

# 2.
points_in_r2 = 0
all_points = 0
for i in range(10000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        points_in_r2 += 1
    all_points += 1
ratio = points_in_r2 / all_points
print(f"{points_in_r2}/{all_points} = {ratio}")