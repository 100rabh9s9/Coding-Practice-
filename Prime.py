import math #to Perform the Math operation sqrt()
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, it's prime

num = int(input("Enter a number: "))
 
if is_prime(num): #Function Call 
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

