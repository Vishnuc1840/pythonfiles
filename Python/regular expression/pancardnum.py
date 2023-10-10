from re import *

pan_num=input("enter pancard number:")

rule="[A-Z]{3}[PCFHTA]{1}[A-Z]{1}[\d]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_num)

print("invalid" if matcher==None else "valid")

# FIRST THREE CASES MUST BE UPPER CASE RANDOM LETTERS 
# 4TH PLACE MUST BE ALPHABETS [PCFHTA]
# FIFTH PLACE ANY RANDOM UPPERCASE ALPHABETS
# four digits 
# random uppercase 1