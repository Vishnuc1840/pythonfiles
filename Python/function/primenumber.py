def is_prime(num):
    if num<=1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num %i==0:
            return False

    return True

num=int(input("enter the number"))

if is_prime(num):
    print(num,"is a prime number")

else:
     print(num,"is not prime number")