#Pascals Triangle 
n = 5 // Fixed Size 
for i in range(n):
    print(" " * (n - i), end="")
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1) //Floor Division 
    print() //For Proper Spacing 
