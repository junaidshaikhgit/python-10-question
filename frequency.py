#Write a function to count the frequency of each character in a string.
def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

# Example usage
print(char_frequency("mississippi"))
