num1=int(input("enter a number :"))
num2=int(input("enter a number :"))

def hcf(num1,num2):
    smaller=min(num1,num2)
    hcf=1

    for i in range(1,smaller+1):
        if num1 % i==0 and num2 % i==0:
            hcf=i

    return hcf

result=hcf(num1,num2)
print("hcf of num1",num1, "and",num2, "is",result)