height_incm=int(input("enter height in cm : "))

weight_inkg=int(input("enter weight in kg : "))

height_inmeter=height_incm/100

bmi=weight_inkg/height_inmeter**2

print(bmi)

#<19 under weight
#20-25 normal weight
#25-30 pre obocity
#30-35 obecity class 1
#35-40 obecity class 2
#>40 serve obecity

if(bmi<20):
    print("under weight")
elif(bmi<25):
    print("normal weight")
elif(bmi<30):
    print("pre obicity")

    
    




