lst1=[10,11,12,13,16]
lst2=[12,13,14,20,21]
lst1.sort()
lst2.sort()

p1,p2=0,0

while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print("common",lst2[p2])
        p2+=1
    elif lst1[p1]<lst2[p2]:
        p1+=1
    else:
        p2+=1



        
# for n in lst1:
#     if n in lst2:
#         print(n)


# for i in lst1:
#     for j in lst2:
#         if i==j:
#             print(i)

# def same_objects(lst1,lst2):
#     same_objects=[]
#     for obj in lst1:
#         if obj in lst2:
#             same_objects.append(obj)
# return same_objects

