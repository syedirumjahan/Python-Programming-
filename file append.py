#file append

file = open("filehandling.txt", "a")
file.write("This context is added via append")
print("new content appended.\n")
file.close()