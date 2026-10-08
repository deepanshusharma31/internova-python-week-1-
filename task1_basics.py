# Task 1: Python Basics - Welcome message and formatted student info
print("=" * 45)
print("  Welcome to Python for Data Analytics!")
print("=" * 45)

name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

print("\n----- Student Information -----")
print(f"Name    : {name}")
print(f"College : {college}")
print(f"Branch  : {branch}")
print("-------------------------------")
