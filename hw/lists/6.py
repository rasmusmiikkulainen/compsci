import random
n = 10
list_of_lists = [random.sample(list(range(n)), n) for _ in range(5)]

new_lst = []
for lst in list_of_lists:
    new_lst.extend(lst)
print(new_lst)