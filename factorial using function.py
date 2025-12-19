# Factorial using function (recursion)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

num = int(input("Enter number: "))

print(f"Factorial of {num} is {fact(num)}")
