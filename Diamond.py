def print_diamond(n):
    
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(" " * (n - i - 1), end="")
        # Print stars
        print("*" * (2 * i + 1))

# Test the function
n = int(input("Enter the number of rows for the diamond pattern: "))
print_diamond(n)
