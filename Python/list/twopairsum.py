#  two pair sum
lst=[2,3,4,5]
sum=8
low=0
upp=len(lst)-1

while (low<upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==sum:
        print(lst[low],lst[upp],"pairs")
        break
    elif(cur_sum<sum):
        low+=1
    else:
        upp-=1




