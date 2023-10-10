from re import *

text="aabbaaabb"   
# pattern="a+"    # +means one or more
# pattern="a*"     #zero or more
pattern="a{1,2}"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())