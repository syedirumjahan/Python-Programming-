#natural numbers

n = int(input("Enter N: "))
i = 1
sum = 0
while i <= n:
    print(f"{i}", end=',')
    sum = sum + i
    i = i + 1

print("\nSum =", sum)
