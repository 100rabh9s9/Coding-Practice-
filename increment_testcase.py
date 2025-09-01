# A simple Beginner Program to Under the working of Loops and input using Test Cases 
# This program reads a number of test cases,
# then reads each number and prints that number + 1.

# Read number of test cases
t = int(input("Enter number of test cases: "))

# Loop over the number of test cases
for i in range(t):
    n = int(input(f"Enter number {i + 1}: "))
    print(n + 1)
