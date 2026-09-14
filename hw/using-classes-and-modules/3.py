def dashify_substring(s, sub):
    if not sub:
        out = s
    else:
        dash = "-" + sub + "-"
        out = s.replace(sub, dash, count=1)
    return out

testcases = [("foo", "o"), ("foobar", "oba"), ("foobar", "f"), 
             ("foobar", "bar"), ("foobar", "cat"), ("foobar", "")]
for a in testcases:
    print(a, dashify_substring(*a))