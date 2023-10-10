# for row in range(1,7):
#     for sp in range(7-row,1.-1):
#         print(end=" ")
#     for st in range(row):
#         print("*",end=" ")
#     print()

for i in range(1,7):
    for j in range(7-i+1):
        print(end=" ")
    for j in range(2*i+1):
        if i==0 or i == 7-1 or j==0 or j == 2*i:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()