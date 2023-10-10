from re import *
variable=input("enter a variable name")

rule="[a-zA-Z][0-9a-zA-Z_]*"

matcher=fullmatch(rule,variable)
print("invalid" if matcher==None else "valid")


# rule k-m alphabets

# digit in second place

# divided by 3

# any number of characters