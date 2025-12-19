#operations 

s1 = {1,2,3}
s2 = {2, 4, 6}
print("original set1=", s1)
print("original set2=", s2)
# add
x = int(input("Enter element to add in s1: "))
y = int(input("Enter element to add in s2: "))
s1.add(x)
s2.add(y)
print("new set1 after adding x =", s1)
print("new set2 after adding y=", s2)
# search
z = int(input("Enter element to search in s1: "))
print("Found in s1" if z in s1 else "Not Found in s1")
# remove
w = int(input("Enter element to remove in s1: "))
s1.discard(w)
v = int(input("Enter element to remove in s2: "))
s2.discard(v)
print("new set1 after removing w =", s1)
print("new set2 after removing y=", s2)
# union
print("Union =", s1.union(s2))
# intersection
print("Intersection =", s1.intersection(s2))
