"""
Text class with ability for:
    Reversing a string
    String to Pig Latin conversion
    Count the number of Vowels in a string
    Check if Palindrome
    Count words in a string
"""

def reverse_string():
    string_to_be_reversed = input("Input your string: ")
    print("This is your string reversed: ", string_to_be_reversed[::-1])

reverse_string()
