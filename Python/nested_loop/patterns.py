# for row in range(1,4):
#     for column in range(1,4):
#         print("#",end="\t")

#     print()

for row in range(1,4):
    for column in range(1,4):
        print(row,end="\t")

    print()


# for row in range(1,8 ):
#     for col in range(row):
#         print(col+1,end="\t")

#     print()


for row in range(1,6):
    for col in range(row):
        res=col+1
        if res %2==0:
            print("#",end="\t")
        else:
            print(col+1,end="\t")
    print()
        


for row in range(4,0,-1):
    for col in range(row):
        print("#",end="\t")
    print()









