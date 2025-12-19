#LARGEST NUMBER

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest is a =", a)
elif b >= a and b >= c:
    print("Largest is b =", b)
else:
    print("Largest is c =", c)

