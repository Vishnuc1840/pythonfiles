from re import *
variable=input("enter a variable name")

# rule="[k-mK-M][0369][a-zA-Z\d\w_]*"
rule="[k-m][369][\w]*"  
matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")