s = input("Enter a string: ").strip()

encoded = ""
count = 1

for i in range(1, len(s) + 1):
    if i < len(s) and s[i] == s[i - 1]:
        count += 1
    else:
        encoded += s[i - 1] + str(count)
        count = 1

print("Encoded string:", encoded)
