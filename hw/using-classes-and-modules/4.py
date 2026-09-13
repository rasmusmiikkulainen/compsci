def file_type(s):
    lastdot = s[::-1].find(".")
    if lastdot in (-1, 0):
        out = ""
    else:
        out = s[-lastdot:]
    return out

testcases = ["foo.doc", "foo.docx", "foo.bar.docx", "", "foo", "foo."]
for a in testcases:
    print((a, file_type(a)))