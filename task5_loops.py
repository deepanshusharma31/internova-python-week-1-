# Task 5: Loops

# 1. Numbers 1 to 20 using for loop
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Multiplication table of any number
n = int(input("Enter a number for its multiplication table: "))
print(f"\nMultiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 3. Even numbers 1 to 50 using while loop
print("\nEven numbers from 1 to 50:")
j = 1
while j <= 50:
    if j % 2 == 0:
        print(j, end=" ")
    j += 1
print()
