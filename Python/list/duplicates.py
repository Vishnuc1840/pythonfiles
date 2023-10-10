# arr=[5,2,5,3,4,2,1,]

# arr.sort()
# for i in range (0,len(arr)-1):
#     current=arr[i]
#     next=arr[i+1]
#     if current==next:
#         print(current)
# # 


arr=[5,2,5,3,5,2,1,]

arr.sort()
duplicate_list=[]
for i in range (0,len(arr)-1):
    current=arr[i]
    next=arr[i+1]
    if current==next:
        if current not in duplicate_list:
            duplicate_list.append(current)
print(duplicate_list)













