from re import *

gmail=input("enter mail id :")

# rule="[\w]+[@]][gmail][.][com]"
# rule="[a-z0-9]+[\W]*[@]gmail[.]com"

rule="[a-z0-9][\W\w]+[@]gmail[.]com"


matcher=fullmatch(rule,gmail)

print("invalid" if matcher==None else "valid")



# atleast one uppercase
# atleast one special characters
# minimu eight characters 