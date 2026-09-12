def file_type(s):
    lastdot = - s[::-1].find(".")
    return s[lastdot:]

print(file_type("test.txt"))
print(file_type("another.pptx"))