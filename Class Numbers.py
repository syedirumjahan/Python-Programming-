# Class Numbers

class Numbers:
    def largest(self, lst):
        max_val = lst[0]
        for x in lst:
            if x > max_val:
                max_val = x
        return max_val

lst = [3, 7, 2, 9, 5]
obj = Numbers()
print("Largest element =", obj.largest(lst))
