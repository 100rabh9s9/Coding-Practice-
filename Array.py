# Initialize an empty list to store the numbers
Tarray = []


try:
    elements = int(input("Enter the number of elements: "))

    # Loop to get each element from the user
    for i in range(elements):
        element = int(input(f"Enter element {i + 1}: "))
        Tarray.append(element)

    # Check if the list is not empty before doing calculations
    if Tarray:
        # Perform calculations
        arraysum = sum(Tarray)
        min_element = min(Tarray)
        max_element = max(Tarray)
        last_element = Tarray[-1]

        # Print all the results
        print("\n--- Results ---")
        print(f"The list you entered is: {Tarray}")
        print(f"The sum of the list is: {arraysum}")
        print(f"The minimum element is: {min_element}")
        print(f"The maximum element is: {max_element}")
        print(f"The last element is: {last_element}")
    else:
        print("\nThe list is empty, no calculations to perform.")

except ValueError:
    print("Invalid input. Please enter whole numbers only.")