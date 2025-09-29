def pattern_diamond(n):
    # Upper part of the diamond (including middle row)
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end=" ")
        # Print stars
        print("*" * (2 * i + 1))

    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        print(" " * (n - i - 1), end=" ")
        # Print stars
        print("*" * (2 * i + 1))
    #Take input from User to Specify the pattenr number 
n = int(input("Enter the number of rows for the diamond pattern: "))
pattern_diamond(n)

