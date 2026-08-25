year = int(input("please give year to check: "))

leap = False

if year % 4 == 0:
    leap = True

if year % 100 == 0:
    leap = False

if year % 400 == 0:
    leap = True

print(leap)

print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))