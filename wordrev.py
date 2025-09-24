 def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

input_str = "Hello world"
print(reverse_words(input_str))
