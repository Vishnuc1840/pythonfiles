from json import load
path="C:\\Users\\DIGI HUB\\OneDrive\\Desktop\\Python\\contries\\countries.json"

with open(path,encoding="utf-8") as f:
    countries=load(f)

# number of countries 
# print(len(countries))

# print all country names

country_names=[c.get("name") for c in countries ]
# print(country_names)

# capital of china 

# country_capital=[c.get("capital") for c in countries if c.get("name")==("China")]
# print(country_capital)

# REGIONS

# country_region={c.get("region") for c in countries} 
# print(country_region)

# border of india

# country_borders=[c.get("borders") for c in countries if c.get("name")==("India")][0]
# print(country_borders)

# border_name=[c.get("name") for c in countries if c.get("alpha3Code") in country_borders]
# print(border_name)


# print independent country name 

# print currency of india

# currency=[c.get("currencies") for c in countries if c.get("name")==("India")][0][0]
# print(currency)

# independent=[c.get("name") for c in countries if c.get("independent")==True]
# print(independent)

# currency less 

# data=[c.get("name") for c in countries if ("currencies") not in c]
# print(data)


country_currencies=[c for c in countries if "currencies" in c]
currencies=[ c.get("currencies")[0].get("symbol") for c in country_currencies]
wc={}
for c in currencies:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

# print(wc)
print(max( (v,k) for k,v in wc.items()))

