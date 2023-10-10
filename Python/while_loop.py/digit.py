num=324
stri=""
while(num !=0):
    digit=num % 10
    stri+=str(digit)
num=num//10
print(stri)


