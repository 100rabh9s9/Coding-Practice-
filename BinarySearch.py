#Binary Search 
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
arr = input("Enter a sorted list of numbers (comma separated): ").split(',')
arr = [int(x.strip()) for x in arr]  # Convert input to integers

#Sort the list to meet the binary search requirement
arr.sort()
print(arr) 
#Binary search requires a sorted list
target = int(input("Enter the target value to search for: ")
index = binary_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index+1}.")
else:
    print(f"Target {target} not found in the list.")


