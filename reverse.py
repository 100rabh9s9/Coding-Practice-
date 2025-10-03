def reverseArray(arr):
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left and Right  pointers
        left += 1
        right -= 1

if __name__ == "__main__":
    # Prompt the user to input elements separated by space
    user_input = input("Enter array elements separated by space: ")
    
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))

    reverseArray(arr)

    print("Reversed array:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
