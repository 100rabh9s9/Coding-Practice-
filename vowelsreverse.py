# This a program from Leetcode. Problem no 345.
# It has been improvised to take in User Input and execute rather than test cases;
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []  
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # List of vowels
        for i in s:
            if i in vowels:  
                l.append(i)
        l.reverse()  
        result = list(s)  
        j=0
        for i in range(len(result)):
            if result[i] in vowels:  
                result[i] = l[j]  ##To loop and check can be with for j in range 
                j=j+1
        return ''.join(result)  
#For user to enter a String 
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    sol = Solution()
    result = sol.reverseVowels(input_string)
    print("Output with reversed vowels:", result)