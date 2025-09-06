s = input("Enter a string: ").strip()

encoded = ""
count = 1

for i in range(1, len(s) + 1):  #Traverse through the string
    if i < len(s) and s[i] == s[i - 1]:  # If current char is same as previous, increase count
        count += 1
    else:   #Otherwise, append previous char and its count to result
        encoded += s[i - 1] + str(count)
        count = 1

print("Encoded string:", encoded)

