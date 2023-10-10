#grading system
#>90-A+
#>80-A
#>70-B+
#>60-B
#>50-C+
#>4O-C
#>30-D+
#>20-fail

mark=int(input("enter your mark : "))
if(mark>90):
    print("A+")
if(mark<90 and mark>=80):
    print("A")
if(mark<80 and mark>=70):
    print("B+")
if(mark<70 and mark>=60):
    print("B")
if(mark<60 and mark>=50):
    print("C+")
if(mark<50 and mark>=40):
    print("c")
if(mark<40 and mark>=30):
    print("D+")
if(mark<30):
    print("fail")