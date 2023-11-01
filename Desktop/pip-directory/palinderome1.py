import string
import re
punctuation = string.punctuation
# TODO - Repeat the previous exercise but ignore case sensitivity and punctuation.


def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False