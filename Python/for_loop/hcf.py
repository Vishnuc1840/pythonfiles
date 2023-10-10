# num1=18
# num2=9

# for i in range(1,num2+1):
#     if num1 %i==0 and num2 %i==0:
#      hcf=i
# print(hcf)

#break and continue

# for i in range(1,51):
#     if i==25:
#         break
#     print(i)
# print("outside the loop")

for i in range(1,51):
    if i==25:
       continue
    print(i)


def lcm(num1,num2):
    gcd=hcf(num1,num2)
    res=(num1*num2)/gcd

    return res

print(lcm(18,24))

 