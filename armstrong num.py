# whether a number is an Armstrong number

n = int(input("Enter a number: "))
s = 0
temp = n

digits = len(str(n))   # count number of digits

while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10

if s == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

