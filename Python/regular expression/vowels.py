from re import *

text="good morning sachin007"

# print all wowels udsig
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

# 