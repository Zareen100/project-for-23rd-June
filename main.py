# Function to swap three numbers
def swap_three_numbers(a, b, c):
    print(f"Before swapping: a = {a}, b = {b}, c = {c}")
    # Swapping logic
    a, b, c = c, a, b
    print(f"After swapping: a = {a}, b = {b}, c = {c}")
    return a, b, c

# Taking user input
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))

# Swapping and displaying the result
swap_three_numbers(a, b, c)
