# Dictionary using functions

d = {
    "Name": "Irum Jahan Indrabi",
    "College": "IUST Awantipora",
    "Roll No": "16",
    "Residence": "J&K"
}

def add():
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

def search():
    k = input("Search key: ")
    print(d[k] if k in d else "Not found")

def display():
    print(d)

add()
search()
display()
