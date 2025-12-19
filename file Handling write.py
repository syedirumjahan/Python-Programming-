#filehandling create & write

file = open(r"C:\Users\dell\Python programs\filehandling.txt", "w")
file.write("Welcome to Python File Handling\n")
file.write("This file is created using Python.\n")
file.close()

print("File created and written successfully.")
