orders=["veg meals","fishmeals","veg meals","fishmeals","vb","cb","vb","cb","vb","friedrice"]

order_count={}
for item in orders:
    if item in order_count:
        order_count[item]+=1
    else:
        order_count[item]=1
print(order_count)