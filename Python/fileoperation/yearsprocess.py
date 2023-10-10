f_read=open("C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\fileoperation\years.txt","r")
l_write=open("C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\fileoperation\leapyear.txt","w")

for year in f_read:
    year=int(year)
    if (year%100==0) and (year%400==0):
        l_write.write(str(year)+"\n")
    elif(year  %100!=0) and (year%4==0):
        l_write.write(str(year)+"\n")
