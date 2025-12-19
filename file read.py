#fie read

file = open("filehandling.txt", "r")
print("Reading file content:")
print(file.read())
content=file.read()
print(content)
file.close()