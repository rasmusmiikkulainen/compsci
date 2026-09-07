lst = ["what", "a", "wonderful", "morning"]
new_lst = []

for word in lst:
    if len(word) > 4:
        new_lst.append(word)

print(new_lst)
print([word for word in lst if len(word) > 4])