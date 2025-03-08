def count_words(s):
    
    words = s.split()
    
    return len(words)

print(count_words("my name is junaid shaikh"))  # 5
print(count_words("   i am from solapur  "))  # 4
