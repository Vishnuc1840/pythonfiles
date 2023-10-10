mobile={"name":"i phone","brand":"apple","colour":"blue","price":165000,"offer":100}

# print(mobile["name"])
# print(mobile["brand"])
# print(mobile["colour"])
# print(mobile["price"])

# adding a new key value pair
# display:amoled
# dic_obj["key"]="obj
mobile["displyay"]="amoled"
print(mobile)

# if "offer" in mobile:
#     print("offer key is present")
# else:
#     print("not exist")
 

# if offer is present add current offer price +50 else add offer as 50

if "offer" in mobile:
    mobile["offer"]+=50
else:
    mobile["offer"]=50

print(mobile)
