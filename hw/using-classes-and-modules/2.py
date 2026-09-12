def date_of_birth(ssn):
    year = ssn[4:6]
    c = ssn[6]
    if c == "+":
        c = "18"
    elif c == "-":
        c = "19"
    else:
        c = "20"
    y = int(c + year)
    m = int(ssn[2:4])
    d = int(ssn[:2])
    return (y, m, d)

print(date_of_birth("140598+abcd"))