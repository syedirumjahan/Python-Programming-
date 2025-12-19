# Prime number program

n = int(input("Enter number: "))
flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False
        break

print(f"{n} is a Prime number" if flag and n > 1 else f"{n} is not a Prime number")
