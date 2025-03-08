str = "Moammed Junaid"

vowels = "aeiouAEIOU"

count = {i: str.count(i) 
for i in vowels 
if i in str}
print(count)