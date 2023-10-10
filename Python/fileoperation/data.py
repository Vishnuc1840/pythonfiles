f=open("C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\fileoperation\\file.txt","r")
for line in f:
    print(line)
    # if it is back slash put it one more

words=[line.rstrip("\n") for line in f ]
print(words)