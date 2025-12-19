# Class Marks

class Marks:
    def __init__(self):
        self.marks = []

    def get_marks(self):
        self.marks = list(map(int, input("Enter marks : ").split(",")))

    def total(self):
        t = 0
        for m in self.marks:
            t += m
        return t

    def average(self):
        return self.total() / 5

m = Marks()
m.get_marks()
print("Total =", m.total())
print("Average =", m.average())
