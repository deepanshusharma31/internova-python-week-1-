# Task 8: Basic File Handling
filename = "introduction.txt"

# 1 & 2. Create the file and write introduction
with open(filename, "w") as f:
    f.write("Hello! My name is Deepanshu.\n")
    f.write("I am from Delhi and I hold a B.A. in Economics from University of Delhi.\n")
    f.write("I am learning Python for Data Analytics.\n")
print(f"'{filename}' created and introduction written.\n")

# 3. Read and display the contents
print("----- File Contents -----")
with open(filename, "r") as f:
    print(f.read())
