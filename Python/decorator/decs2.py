def decorator1(fn):
    def wrapper():
        print("decorator 1 before calling original function")
        result=fn()
        print("decorator 1 after calling original function")
        return result
    return wrapper

def decorator2(fn):

    def wrapper():
        print("decorator 2 before calling original function")
        result=fn()
        print("decorator 2 after calling original function")
        return result
    return wrapper
@decorator1
@decorator2
def original_function():
    print("this is original function")

original_function()