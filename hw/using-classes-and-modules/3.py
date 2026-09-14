def dashify_substring(s, sub):
    if sub == "":
        return s
    dash = "-" + sub + "-"
    return s.replace(sub, dash, count=1)

testcases = [("foo", "o"), ("foobar", "oba"), ("foobar", "f"), 
             ("foobar", "bar"), ("foobar", "cat"), ("foobar", "")]
for a in testcases:
    print(a, dashify_substring(*a))