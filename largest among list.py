#largest

lst = [1, 2, 3, 4, 5, 6]
max = lst[0]
for i in lst:
    if i > max:
        max = i
print(f" {max} among the list is largest")
