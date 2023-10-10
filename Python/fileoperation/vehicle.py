f=open("C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\fileoperation\\numbers.txt","r")
all_numbers=[line.rstrip("\n") for line in f]
print(all_numbers)


kerl_numbers=[num for num in all_numbers if num.startswith("kl")]
print(kerl_numbers)