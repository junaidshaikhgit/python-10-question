def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = ''.join(s.split()).lower()
    
    # Check if the string is the same forwards and backwards
    return cleaned_str == cleaned_str[::-1]

# Example usage:
print(is_palindrome("madam"))  # True
print(is_palindrome("word"))  # False
