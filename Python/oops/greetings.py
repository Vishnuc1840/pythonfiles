def greetings(**kwags):
    print(f"hello{kwags.get('msg')} app user{kwags.get('user name')}")

greetings(msg="good morning",user_name="geo")


def dispatch_order(**kwargs):
    item=kwargs.get("item")
    code=kwargs.get("code")
    status=kwargs.get("status")
    name=kwargs.get("name")

    print(f"hellow user {name} your order {code} {item} is ready to {status}")



dispatch_order(item="ucb shirt",code="123bc",status="delivered",name="vijay")