num1=int(input("enter num1>"))#100
num2=int(input("enter num2>"))#20
num3=int(input("enter num3>"))#15

#second largest

if(num1>num2) and (num1>num3):
    if(num2>num3):
        print("num2 is second largest")
    else:
        print("num3 is largest")
#    print("num1 is largest")

elif(num2>num1) and (num2>num3):
    if(num1>num3):
        print("num1 is second largest")
    else:
        print("num3 is second largest")

elif(num3>num2) and (num3>num1):
    if(num1>num2):
        print("second num1")
    else:
        print("second")

elif(num1==num2) and (num1==num3):
        print("all are equal")