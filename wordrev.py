#Basic Python Program from Leetcode/Hackerank 
#improvised for self learning 
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

input_str = "Hello world" #Custom String 
print(reverse_words(input_str))
