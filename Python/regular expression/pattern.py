from re import *

# text="ababbbaaabab"

# pattern="aba"

# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())




text="python @ 14323"

# pattern="[a-z]"
# pattern="[A-Z]"
# pattern="a-zA-Z"
# pattern="[0-9]"
# pattern="[a-zA-z0-9]"

#   "[^]"  is used to remove
# pattern="[^a-z]"  
# predifined characters
# pattern="\d"  #"[0-9]"
# pattern="\D"   #to exclude digit

# patten="\w"   alphabets and numbers [a-zA-Z0-9]

# pattern='\W'  special characters



matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
