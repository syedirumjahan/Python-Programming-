#read updated content

file=open("filehandling.txt","r")
print("updated file content:")
print(file.read())
file.close()