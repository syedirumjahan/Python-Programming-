#pallindrome num

n = input("Enter number: ")
if n == n[::-1]:
    print(f"yes {n} is a Palindrome number")
else:
    print(f"No {n} is not a Palindrome number")
