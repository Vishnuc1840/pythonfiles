def smart_div(fn):
    def wrapper(n1,n2):
        if(n2==0):
            print("/ by zero nop")
            return
        return fn(n1,n2)
    return wrapper


@smart_div
def div(n1,n2):
    return n1/n2

print(div(5,0))
