# Read dimensions of the first matrix
rows1 = int(input("Enter number of rows for first matrix: "))
cols1 = int(input("Enter number of columns for first matrix: "))

# Read first matrix
print("Enter elements of first matrix (each row with space-separated values):")
mat1 = []
for i in range(rows1):
    while True:
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols1:
            print(f"Please enter exactly {cols1} values.")
        else:
            mat1.append(row)
            break

# Read dimensions of the second matrix
rows2 = int(input("Enter number of rows for second matrix: "))
cols2 = int(input("Enter number of columns for second matrix: "))

# Check if matrix multiplication is possible
if cols1 != rows2:
    print("Error: Cannot multiply the two matrices due to dimension mismatch.")
    exit()

# Read second matrix
print("Enter elements of second matrix (each row with space-separated values):")
mat2 = []
for i in range(rows2):
    while True:
        row = list(map(int, input(f"Row {i+1}: ").split())) #f string (Formatted String)
        if len(row) != cols2:
            print(f"Please enter exactly {cols2} values.")
        else:
            mat2.append(row)
            break

# Initialize product matrix with zeros
product = [[0 for _ in range(cols2)] for _ in range(rows1)]

# Multiply matrices
for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):  # same as rows2
            product[i][j] += mat1[i][k] * mat2[k][j]

# Display product matrix
print("\nProduct matrix:")
for row in product:
    print(" ".join(map(str, row)))
