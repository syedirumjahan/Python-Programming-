#count even numbers from list

lst=[1,4,6,12,16,22,29]
count = 0
for i in lst:
    if i % 2 == 0:
        count += 1
print(f"number of even numbers in lst is: {count}")
