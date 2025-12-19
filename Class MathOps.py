# Class MathOps

class MathOps:
    def fact(self, n):
        if n == 0:
            return 1
        return n * self.fact(n - 1)

n = int(input("Enter number: "))
obj = MathOps()
print("Factorial =", obj.fact(n))
