# A simple Beginner Program to Under the working of Loops and input using Test Cases 
# This program reads a number of test cases,
# then reads each number and prints that number + 1.
# The main of the Program is to Learn the functioning of For loop 
# Read number of test cases
t = int(input("Enter number of test cases: "))

# Loop over the number of test cases
for i in range(t):
    n = int(input(f"Enter number {i + 1}: ")) # Increment the value by just 1 
    print(n + 1)


# Read number of test cases
try:
    t = int(input("Enter the number of test cases: "))
    
    # Loop over the number of test cases
    for i in range(t):
        # Read input for each test case
        try:
            n = int(input(f"Enter number {i + 1}: "))
            print(n + 1)  # Output incremented number
        except ValueError:
            print("Please enter a valid integer.")
            
except ValueError:
    print("Invalid input. Please enter a valid number of test cases.")
