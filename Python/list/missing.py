# arr=[1,3,4,6,5]

# n=1 
# for n in arr:
#     n+=1
# print("the smallest positive missing integer is :", n)

arr=[1,2,3,5,6]

arr.sort()
if arr[0] !=1:
    print("1 is missing")
else:
  
     for i in range(0,len(arr)-1):
        cur=arr[i]
        nex=arr[i+1]
        if nex-cur !=1:
           print(cur+1,"is missing")
        break