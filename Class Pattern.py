# Class Pattern

class Pattern:
    def square(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()

    def triangle(self, n):
        for i in range(1, n + 1):
            for j in range(i):
                print("*", end=" ")
            print()

p = Pattern()
n = int(input("Enter size: "))
p.square(n)
p.triangle(n)
