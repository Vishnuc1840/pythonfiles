def product(*args):
    res=1
    for n in args:
        res*=n
    print(res)


product(1,3,3)
product(10,20)
