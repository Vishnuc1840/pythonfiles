# num1=int(input("enter a nmber"))
# num2=int(input("enter a number"))

# def lcm(num1,num2):
#     large=max(num1,num2)

#     while True:
#         if larger % num==0 and larger % num2==0:
#             lcm=larger
#             break
#         larger+=1
#     return lcm
#     result=lcm(num1,num2)
# print("lcm of num1",num1, "and",num2, "is",result )




# lcm

# lcm(num1,num2)=nim1*num2/hcf(num1,num2)


# def lcm(num1,num2):
#     gcd=hcf(num1,num2)
#     res=(num1*num2)/gcd

#     return res

# print(lcm(18,24))




def least_common_multiple(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True

    while(flag):
        if max%n1==0 and max%n2==0:
           print(f"lcm of {n1},{n2} is {max}")
           break
        else:
            max+=1

least_common_multiple(30,25)

