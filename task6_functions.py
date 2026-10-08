# Task 6: Functions

def square(num):
    """Return the square of a number."""
    return num * num


def average(a, b, c):
    """Return the average of three numbers."""
    return (a + b + c) / 3


n = float(input("Enter a number to find its square: "))
print(f"Square of {n} = {square(n)}")

print("\nEnter three numbers to find their average:")
x = float(input("First number : "))
y = float(input("Second number: "))
z = float(input("Third number : "))
print(f"Average of {x}, {y}, {z} = {average(x, y, z):.2f}")
